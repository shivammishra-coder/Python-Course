import React from 'react';

const TaskItem = ({ task, onToggle, onDelete }) => (
  <div className={`task-item ${task.priority.toLowerCase()}`}>
    <input 
      type="checkbox" 
      checked={task.status === 'Completed'} 
      onChange={() => onToggle(task.id)} 
    />
    <div className="task-info">
      <span className={task.status === 'Completed' ? 'strikethrough' : ''}>
        {task.title}
      </span>
      <span className="priority-tag">{task.priority}</span>
    </div>
    <button className="delete-btn" onClick={() => onDelete(task.id)}>Delete</button>
  </div>
);

export default TaskItem;