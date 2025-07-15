# main.py
# FastAPIによるユーザー管理APIサンプル
# 制作日: 2024-06-13

from fastapi import FastAPI  # FastAPI本体をインポート
from pydantic import BaseModel  # データバリデーション用のモデル
from typing import List  # 型ヒント（リスト型）

# FastAPIアプリケーションのインスタンスを作成
app = FastAPI()

# ユーザーデータのモデル定義（id, name, ageを持つ）
class User(BaseModel):
    id: int      # ユーザーID
    name: str   # ユーザー名
    age: int    # 年齢

# ユーザー情報を格納するリスト（メモリ上で管理）
users = []

# ルート（/）にアクセスしたときの処理
@app.get("/")
def read_root():
    # レスポンスとしてメッセージを返す
    return {"message": "Hello, World!"}

# ユーザー新規作成（Create）
@app.post("/users/", response_model=User)
def create_user(user: User):
    # 受け取ったユーザー情報をリストに追加
    users.append(user)
    return user

# ユーザー一覧取得（Read: 全件）
@app.get("/users/", response_model=List[User])
def read_users():
    # 全ユーザー情報を返す
    return users

# 特定ユーザー取得（Read: 1件）
@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    # 指定IDのユーザーを検索
    for user in users:
        if user.id == user_id:
            return user
    # 見つからなければエラーを返す
    return {"error": "User not found"}

# ユーザー情報更新（Update）
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    # 指定IDのユーザーを検索し、情報を更新
    for user in users:
        if user.id == user_id:
            user.name = updated_user.name
            user.age = updated_user.age
            return user
    # 見つからなければエラーを返す
    return {"error": "User not found"}

# ユーザー削除（Delete）
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    # 指定ID以外のユーザーだけ残す
    users = [user for user in users if user.id != user_id]
    return {"message": "User deleted"}