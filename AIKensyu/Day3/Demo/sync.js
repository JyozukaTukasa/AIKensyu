// sync.js
// 同期処理のデモ
// 制作日: 2024-06-13

// Node.jsのsetTimeoutを使い、同期的な流れを再現
console.log("1．ご飯を炊く");

setTimeout(() => {
    console.log("2．ご飯が炊けた");
    console.log("3．野菜を切る");
    console.log("4．味噌汁を作る");
    console.log("5．ご飯を盛る");
}, 3000); 