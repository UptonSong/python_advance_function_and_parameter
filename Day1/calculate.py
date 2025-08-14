def calculate_stats(*numbers, verbose=False):
    """
    計算輸入數字的總和與平均值
    *numbers: 可傳入任意多個數字（可變參數）
    verbose: 是否印出詳細過程（預設 False）
    """
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0

    if verbose:
        print(f"數字清單：{numbers}")
        print(f"總和：{total}")
        print(f"平均：{average:.2f}")
    
    return total, average

# 範例呼叫
result = calculate_stats(10, 20, 30, verbose=True)
print("回傳結果：", result)

# 也可以不用 verbose
print(calculate_stats(5, 15))

def calculate_stats2(*numbers, **kwargs):
    """
    計算輸入數字的總和、平均值、最大值、最小值
    *numbers: 任意多個數字
    **kwargs:
        ignore_negative (bool): 是否忽略負數
        verbose (bool): 是否顯示詳細資訊
    """
    ignore_negative = kwargs.get("ignore_negative", False)  # 預設不忽略
    verbose = kwargs.get("verbose", False)                  # 預設不顯示詳情

    # 如果設定忽略負數，就過濾掉
    if ignore_negative:
        numbers = tuple(n for n in numbers if n >= 0)

    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    max_val = max(numbers) if count > 0 else None
    min_val = min(numbers) if count > 0 else None

    if verbose:
        print(f"數字清單：{numbers}")
        print(f"總和：{total}")
        print(f"平均：{average:.2f}")
        print(f"最大值：{max_val}")
        print(f"最小值：{min_val}")

    return total, average, max_val, min_val



# --- 測試 ---
print(calculate_stats2(10, 20, -5, 30, verbose=True))
print(calculate_stats2(10, 20, -5, 30, ignore_negative=True, verbose=True))