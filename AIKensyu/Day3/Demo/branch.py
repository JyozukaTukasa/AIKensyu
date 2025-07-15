# branch.py
# テストの点数による判定デモ
# 制作日: 2024-06-13

# テストの点数（int型）
score = 75

# 点数に応じて判定を出力（ログ出力: デバッグや運用時の確認用）
if score >= 80:
    print("合格です")
elif score >= 60:
    print("補習が必要です")
else:
    print("不合格です")

