import csv
import os
import tkinter as tk
from tkinter import filedialog
import subprocess
import platform

# 建立 Tk 視窗（隱藏）
root = tk.Tk()
root.withdraw()

# 讓使用者選檔
input_file = filedialog.askopenfilename(
    title="請選擇 HDMI CEC 原始 CSV",
    filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
)

if not input_file:
    print("未選擇檔案，程式結束。")
    exit()

# 自動產生輸出檔名
base, ext = os.path.splitext(input_file)
output_file = base + "_Parsed" + ext

groups = []
current_group = []
current_time = None

with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # skip header

    for row in reader:
        if len(row) < 3:
            continue
        if len(row) == 4:
            time, analyzer, decoded, dst = row[0], row[1], row[2], row[3]
        elif len(row) == 3:
            time, analyzer, decoded = row[0], row[1], row[2]

        # 遇到 Start Sequence 開始新組,把前一組的current_group 存進groups
        if "Start Sequence" in decoded:
            if current_group:
                groups.append((current_time, current_group))
            current_group = [decoded]
            current_time = time
        else:
            current_group.append(decoded)
            if "Header SRC" in decoded:
                print(dst)
                current_group.append(dst)

    # 收最後一組
    if current_group:
        groups.append((current_time, current_group))

# 輸出成新的 CSV，每行一條紀錄
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Group", "Time", "Details"])

    for i, (time, group) in enumerate(groups, 1):
        text_block = "\n".join(group)
        writer.writerow([i, time, text_block])

print(f"轉換完成，輸出檔案: {output_file}")

# 自動開啟資料夾並選取輸出檔案
system = platform.system()
if system == "Windows":
    subprocess.run(["explorer", "/select,", os.path.abspath(output_file)])
elif system == "Darwin":  # macOS
    subprocess.run(["open", "-R", output_file])
else:  # Linux
    subprocess.run(["xdg-open", os.path.dirname(output_file)])