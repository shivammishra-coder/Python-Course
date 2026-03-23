import React, { useState, useEffect, useMemo } from 'react';
import { useTheme } from './context/ThemeContext.jsx';
import TaskForm from './components/TaskForm.jsx';
import TaskList from './components/TaskList.jsx';
import './App.css';

function App() {
  const { isDarkMode, toggleTheme } = useTheme();
  
  // 1. Initialize State (with Lazy Initializer for LocalStorage)
  const [tasks, setTasks] = useState(() => {
    const saved = localStorage.getItem('smart-tasks');
    return saved ? JSON.parse(saved) : [];
  });
  
  const [search, setSearch] = useState('');
  const [filter, setFilter] = useState('All');

  // 2. Persistence: Save to LocalStorage whenever 'tasks' changes
  useEffect(() => {
    localStorage.setItem('smart-tasks', JSON.stringify(tasks));
  }, [tasks]);

  // 3. Logic Handlers (Passed as functions to components)
  const addTask = (task) => setTasks((prev) => [...prev, task]);
  
  const deleteTask = (id) => {
    setTasks((prev) => prev.filter(t => t.id !== id));
  };

  const toggleTask = (id) => {
    setTasks((prev) => prev.map(t => 
      t.id === id ? { ...t, status: t.status === 'Pending' ? 'Completed' : 'Pending' } : t
    ));
  };

  // 4. Advanced Logic: Filtered List (useMemo prevents unnecessary re-renders)
  const filteredTasks = useMemo(() => {
    return tasks.filter(task => {
      const matchesSearch = task.title.toLowerCase().includes(search.toLowerCase());
      const matchesFilter = filter === 'All' || task.status === filter;
      return matchesSearch && matchesFilter;
    });
  }, [tasks, search, filter]);

  return (
    <div className={`app-container ${isDarkMode ? 'dark' : 'light'}`}>
      <div className="card">
        {/* --- Header Section --- */}
        <header className="app-header">
          <h1>Smart Manager</h1>
          <button className="theme-toggle" onClick={toggleTheme}>
            {isDarkMode ? '☀️' : '🌙'}
          </button>
        </header>

        {/* --- Add Task Component --- */}
        <TaskForm onAddTask={addTask} />

        {/* --- Search & Filter Controls --- */}
        <div className="controls-section">
          <input 
            type="text"
            className="search-bar"
            placeholder="Search tasks..." 
            value={search}
            onChange={(e) => setSearch(e.target.value)} 
          />
          
          <div className="filter-group">
            {['All', 'Pending', 'Completed'].map((type) => (
              <button 
                key={type} 
                className={filter === type ? 'active' : ''}
                onClick={() => setFilter(type)}
              >
                {type}
              </button>
            ))}
          </div>
        </div>

        {/* --- Task List Component (The specialist) --- */}
        <TaskList 
          tasks={filteredTasks} 
          onToggle={toggleTask} 
          onDelete={deleteTask} 
        />

        {/* --- Dashboard Footer (Visual Feedback) --- */}
        <footer className="stats-footer">
          <span>Total: {tasks.length}</span>
          <span>Done: {tasks.filter(t => t.status === 'Completed').length}</span>
        </footer>
      </div>
    </div>
  );
}

export default App;