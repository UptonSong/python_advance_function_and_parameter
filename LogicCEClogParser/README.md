啟動後讀取.csv 檔

csv.reader(f) 取得資料結構
由row 組成,
用for row in reader:  抓出每一個row
每個row 再包含多個內容由","分開
可用row[0] row[1] 取值,
用if "Start Sequence" in decoded: 的格式來判斷是否包含某字串

組成巢狀結構:
groups = []
para2 = []
groups.append(para1,para2)
para2 = [XXX]
para2.append(YYY)  <<< 在para2 後面再接一個內容

        # 遇到 Start Sequence 開始新組 ,把前一組的current_group 存進groups
        if "Start Sequence" in decoded:
            if current_group:
                groups.append((current_time, current_group))
            current_group = [decoded]
            current_time = time
			
最後沒有再遇到"Start Sequence" 會漏掉一組current_group
所以要再加一段
# 收最後一組
    if current_group:
        groups.append((current_time, current_group))


最後把groups 用writer.writerow([i, time, text_block])寫到新的csv檔裡

然後再開啟儲存位置的資料夾

最後如果要打包成 exe

基本指令：

pyinstaller --onefile parsing_csv_file2.py


這樣會在 dist 資料夾裡產生一個 parsing_csv_file2.exe。

4️⃣ 如果你要有自己的 icon（選擇性）
pyinstaller --onefile --icon=youricon.ico parsing_csv_file2.py

5️⃣ 避免跳出黑色的命令視窗（建議）

因為你有用到 tkinter UI，所以最好加上 --noconsole：

pyinstaller --onefile --noconsole parsing_csv_file2.py


這樣 .exe 會只跑 GUI，不會彈出命令提示視窗。