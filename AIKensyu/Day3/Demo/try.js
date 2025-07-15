// try.js
// 例外処理（try-catch）のデモ
// 制作日: 2024-06-13

// 10を0で割る処理
try {
    // 0で割るとInfinityになるが、明示的に例外を投げる
    const result = 10 / 0;
    if (!isFinite(result)) {
        throw new Error('ZeroDivisionError');
    }
    // 割り算が成功した場合の出力（ログ出力: デバッグや運用時の確認用）
    console.log(`結果: ${result}`);
} catch (e) {
    // 0で割った場合のエラー処理
    console.log('0では割り算できません！');
} 