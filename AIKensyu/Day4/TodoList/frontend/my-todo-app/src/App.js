import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  // タスク一覧の状態管理
  const [todos, setTodos] = useState([]);
  // 入力フォームの状態管理
  const [task, setTask] = useState('');

  // 初回マウント時にTodo一覧を取得
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/todos')
      .then(response => setTodos(response.data));
  }, []);

  // タスク追加処理
  const handleSubmit = (e) => {
    e.preventDefault();
    const newId = todos.length > 0 ? Math.max(...todos.map(t => t.id)) + 1 : 1;
    axios.post('http://127.0.0.1:8000/todos', { id: newId, task })
      .then(response => {
        setTodos([...todos, response.data]);
        setTask('');
      });
  };

  // タスク削除処理
  const handleDelete = (id) => {
    axios.delete(`http://127.0.0.1:8000/todos/${id}`)
      .then(() => setTodos(todos.filter(todo => todo.id !== id)));
  };

  return (
    <div style={{ background: '#f7f7f7', minHeight: '100vh', padding: '40px 0' }}>
      <div style={{ maxWidth: 400, margin: '0 auto', background: '#fff', borderRadius: 8, boxShadow: '0 2px 8px rgba(0,0,0,0.08)', padding: 24 }}>
        <h1 style={{ textAlign: 'center', color: '#333', marginBottom: 24 }}>Todoリスト</h1>
        {/* タスク追加フォーム */}
        <form onSubmit={handleSubmit} style={{ display: 'flex', gap: 8, marginBottom: 24 }}>
          <input
            type="text"
            value={task}
            onChange={(e) => setTask(e.target.value)}
            placeholder="タスクを入力"
            required
            style={{ flex: 1, padding: 8, borderRadius: 4, border: '1px solid #ccc', fontSize: 16 }}
          />
          <button type="submit" style={{ padding: '8px 16px', borderRadius: 4, border: 'none', background: '#1976d2', color: '#fff', fontWeight: 'bold', fontSize: 16, cursor: 'pointer' }}>追加</button>
        </form>
        {/* タスク一覧表示 */}
        <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
          {todos.map(todo => (
            <li key={todo.id} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 0', borderBottom: '1px solid #eee' }}>
              <span style={{ fontSize: 16 }}>{todo.task}</span>
              <button
                onClick={() => handleDelete(todo.id)}
                style={{ marginLeft: 12, padding: '4px 12px', borderRadius: 4, border: 'none', background: '#e53935', color: '#fff', fontWeight: 'bold', fontSize: 14, cursor: 'pointer' }}
              >削除</button>
            </li>
          ))}
        </ul>
        {todos.length === 0 && <p style={{ textAlign: 'center', color: '#aaa', marginTop: 16 }}>タスクはありません</p>}
      </div>
    </div>
  );
}

export default App;
