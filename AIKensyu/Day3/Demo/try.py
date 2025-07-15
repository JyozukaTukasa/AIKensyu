# try.py
# 例外処理（try-except）のデモ
# 制作日: 2024-06-13

# 10を0で割る処理
try:
    result = 10 / 0  # 0で割るとZeroDivisionErrorが発生
    # 割り算が成功した場合の出力（ログ出力: デバッグや運用時の確認用）
    print(f"結果: {result}")
except ZeroDivisionError:
    # 0で割った場合のエラー処理
    print("0では割り算できません！") 