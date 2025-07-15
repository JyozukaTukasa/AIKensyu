// class.js
// クラス（Class型）のデモ
// 制作日: 2024-06-13

// Personクラスの定義（名前と年齢を持つ）
class Person {
    // コンストラクタ（インスタンス生成時に名前と年齢を設定）
    constructor(name, age) {
        this.name = name; // ユーザー名
        this.age = age;   // 年齢
    }

    // あいさつを出力するメソッド
    greet() {
        // 名前を使ってあいさつを出力（ログ出力: デバッグや運用時の確認用）
        console.log(`こんにちは、私は${this.name}です`);
    }
}

// Personクラスのインスタンスを作成（花子・30歳）
const p = new Person("花子", 30);
// greetメソッドを実行
p.greet(); 