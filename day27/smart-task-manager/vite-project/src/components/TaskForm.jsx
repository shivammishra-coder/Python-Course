import React, { useState } from 'react';

const TaskForm = ({ onAddTask }) => {
  const [title, setTitle] = useState('');
  const [priority, setPriority] = useState('Medium');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title.trim()) return;
    onAddTask({ id: Date.now(), title, priority, status: 'Pending' });
    setTitle('');
  };

  return (
    <form onSubmit={handleSubmit} className="task-form">
      <input 
        placeholder="Task Title..." 
        value={title} 
        onChange={(e) => setTitle(e.target.value)} 
      />
      <select value={priority} onChange={(e) => setPriority(e.target.value)}>
        <option>High</option>
        <option>Medium</option>
        <option>Low</option>
      </select>
      <button type="submit">Add</button>
    </form>
  );
};

export default TaskForm;