# dictionary.py
# 辞書（dict型）のデモ
# 制作日: 2024-06-13

# personという辞書型オブジェクトを作成（nameとageを格納）
person = {
    "name": "花子",  # ユーザー名
    "age": 30        # 年齢
}

# name＋ageを出力（ログ出力: デバッグや運用時の確認用）
print(f"{person['name']}さん（{person['age']}歳）") 