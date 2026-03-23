import React from 'react';
import TaskItem from './TaskItem';

const TaskList = ({ tasks, onToggle, onDelete }) => {
  // Check if there are any tasks to show
  if (tasks.length === 0) {
    return (
      <div className="empty-state">
        <p>No tasks found. Try adding one or changing your filters!</p>
      </div>
    );
  }

  return (
    <div className="task-list-container">
      {tasks.map((task) => (
        <TaskItem 
          key={task.id} 
          task={task} 
          onToggle={onToggle} 
          onDelete={onDelete} 
        />
      ))}
    </div>
  );
};

export default TaskList;