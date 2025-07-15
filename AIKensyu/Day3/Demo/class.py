# class.py
# クラス（Class型）のデモ
# 制作日: 2024-06-13

# Personクラスの定義（名前と年齢を持つ）
class Person:
    # 初期化メソッド（インスタンス生成時に名前と年齢を設定）
    def __init__(self, name, age):
        self.name = name  # ユーザー名
        self.age = age    # 年齢

    # あいさつを出力するメソッド
    def greet(self):
        # 名前を使ってあいさつを出力（ログ出力: デバッグや運用時の確認用）
        print(f"こんにちは、私は{self.name}です")

# Personクラスのインスタンスを作成（花子・30歳）
p = Person("花子", 30)
# greetメソッドを実行
p.greet() 