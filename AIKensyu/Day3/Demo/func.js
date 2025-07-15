// func.js
// あいさつ関数のデモ
// 制作日: 2024-06-13

// var.jsから年齢(age)をインポート（ユーザー情報の利用）
const { age } = require('./var');

// 名前と現在時刻に応じてあいさつを返す関数
function greet(name) {
    // 現在の日時を取得
    const now = new Date();
    const hour = now.getHours();
    let greeting = '';
    // 時間帯によってあいさつを切り替え
    if (hour >= 5 && hour < 12) {
        greeting = 'おはようございます';
    } else if (hour >= 12 && hour < 18) {
        greeting = 'こんにちは';
    } else {
        greeting = 'こんばんは';
    }
    // あいさつ＋名前＋年齢を1行で出力（ログ出力: デバッグや運用時の確認用）
    console.log(`${greeting}、${name}さん（${age}歳）`);
}

// デモ実行（このファイルを直接実行した場合のみ）
if (require.main === module) {
    greet('太郎');
}

