# func.py
# あいさつ関数のデモ
# 制作日: 2024-06-13

# var.pyから年齢(age)をインポート（ユーザー情報の利用）
from var import age
# datetimeモジュールをインポート（現在時刻取得のため）
import datetime

# 名前と現在時刻に応じてあいさつを返す関数
def greet(name):
    # 現在の日時を取得
    now = datetime.datetime.now()
    # 時間帯によってあいさつを切り替え
    if 5 <= now.hour < 12:
        greeting = "おはようございます"
    elif 12 <= now.hour < 18:
        greeting = "こんにちは"
    else:
        greeting = "こんばんは"
    # あいさつ＋名前＋年齢を1行で出力（ログ出力: デバッグや運用時の確認用）
    print(f"{greeting}、{name}さん（{age}歳）")

# デモ実行（このファイルを直接実行した場合のみ）
if __name__ == "__main__":
    greet("太郎")

