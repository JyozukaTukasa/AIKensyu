# var.py
# ユーザー情報のデモ出力
# 制作日: 2024-06-13

# ユーザー名（str型）
name = "太郎"
# 年齢（int型）
age = 25
# 身長（float型）
height = 170.5
# 学生かどうか（bool型）
is_student = False

# ユーザー情報を1行で出力（ログ出力: デバッグや運用時の確認用）
print(f"名前: {name}, 年齢: {age}歳, 身長: {height}cm, 学生: {'はい' if is_student else 'いいえ'}")
