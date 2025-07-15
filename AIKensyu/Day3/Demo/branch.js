// branch.js
// テストの点数による判定デモ
// 制作日: 2024-06-13

// テストの点数（数値）
const score = 75;

// 点数に応じて判定を出力（ログ出力: デバッグや運用時の確認用）
if (score >= 80) {
    console.log("合格です");
} else if (score >= 60) {
    console.log("補習が必要です");
} else {
    console.log("不合格です");
} 