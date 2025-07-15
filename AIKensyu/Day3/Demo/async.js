// async.js
// 非同期処理（async/await, Promise）のデモ
// 制作日: 2024-06-13

// ご飯を炊く関数（3秒非同期待機）
async function cookRice() {
    console.log("1．ご飯を炊く");
    await new Promise(resolve => setTimeout(resolve, 3000)); // 3秒非同期待機
    console.log("2．ご飯が炊けた");
}

// 野菜を切る関数
async function cutVegetables() {
    console.log("3．野菜を切る");
}

// 味噌汁を作る関数
async function makeMisoSoup() {
    console.log("4．味噌汁を作る");
}

// ご飯を盛る関数
async function serveRice() {
    console.log("5．ご飯を盛る");
}

// メイン関数（非同期で各処理を実行）
async function main() {
    // ご飯を炊く処理は時間がかかるので、他の処理と並行して実行
    await Promise.all([
        cookRice(),
        cutVegetables(),
        makeMisoSoup(),
        serveRice()
    ]);
}

// スクリプトを直接実行した場合のみmainを呼び出す
if (require.main === module) {
    main();
} 