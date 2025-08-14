def show_args_kwargs(*args, **kwargs):
    print("=== *args (tuple) ===")
    print(args)
    print("型別：", type(args))
    print()

    print("=== **kwargs (dict) ===")
    print(kwargs)
    print("型別：", type(kwargs))
    print()

# 測試不同情況
print("\n--- 測試 1：只有位置參數 ---")
show_args_kwargs(10, 20, 30)

print("\n--- 測試 2：只有關鍵字參數 ---")
show_args_kwargs(name="Alice", age=25)

print("\n--- 測試 3：混合使用 ---")
show_args_kwargs(1, 2, 3, ignore_negative=True, verbose=True)

print("\n--- 測試 4：空參數 ---")
show_args_kwargs()
