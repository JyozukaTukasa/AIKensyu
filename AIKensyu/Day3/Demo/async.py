# async.py
# 非同期処理（async/await, asyncio）のデモ
# 制作日: 2024-06-13

import asyncio  # asyncioモジュールをインポート（非同期処理のため）

# ご飯を炊く関数（3秒非同期で待機）
async def cook_rice():
    print("1．ご飯を炊く")
    await asyncio.sleep(3)  # 3秒非同期で待機
    print("2．ご飯が炊けた")

# 野菜を切る関数
async def cut_vegetables():
    print("3．野菜を切る")

# 味噌汁を作る関数
async def make_miso_soup():
    print("4．味噌汁を作る")

# ご飯を盛る関数
async def serve_rice():
    print("5．ご飯を盛る")

# メイン関数（非同期で各処理を実行）
async def main():
    # ご飯を炊く処理は時間がかかるので、他の処理と並行して実行
    await asyncio.gather(
        cook_rice(),
        cut_vegetables(),
        make_miso_soup(),
        serve_rice()
    )

# スクリプトを実行したときだけmainを呼び出す
if __name__ == "__main__":
    asyncio.run(main()) 