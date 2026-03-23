# 🚀 Smart Task Manager

A mini-productivity application built with **React + Vite**. This project is a "Smart Task Manager" designed to manage daily to-do items with high efficiency, featuring priority levels, real-time filtering, and a dynamic theme engine.

## ✨ Core Features

- **Add Tasks**: Create tasks by providing a **Title** and selecting a **Priority** level (High, Medium, Low).
- **Task List View**: Displays all tasks with their Title, Priority, and current Status (Completed or Pending).
- **Mark as Completed**: Toggle task status between "Completed" and "Pending" with an interactive checkbox.
- **Delete Tasks**: Permanent removal of tasks from the list via a delete button.
- **Search Functionality**: A real-time search bar that filters tasks by matching titles.
- **Filter Controls**: Quick-filter buttons to view **All**, **Completed**, or **Pending** tasks.
- **Theme Toggle**: A global switch to toggle the entire UI between **Light** and **Dark** themes using React Context.
- **Persistence**: Automatically saves and loads your tasks from **LocalStorage**, so your data is safe even after a page refresh.

## 🛠️ Tech Stack & Hooks Used

- **Framework**: [React.js](https://reactjs.org/) (via Vite)
- **Styling**: CSS3 with Custom Variables (Theming)
- **Hooks**:
  - `useState`: Manages task data, search queries, and filter states.
  - `useEffect`: Handles synchronization with Browser LocalStorage.
  - `useMemo`: Optimizes performance by memoizing the filtered task list.
  - `useContext`: Manages the global Theme state (Light/Dark mode).

## 📂 Project Structure

```text
src/
├── components/
│   ├── TaskForm.jsx       # Logic for adding new tasks and setting priority
│   ├── TaskItem.jsx       # Individual task row with toggle and delete logic
│   └── TaskList.jsx       # Container that maps tasks and handles empty states
├── context/
│   └── ThemeContext.jsx   # Global Context Provider for Light/Dark mode
├── App.jsx                # Main Logic Hub (State, Filtering, & Layout)
├── App.css                # Global styles and theme variable definitions
└── main.jsx               # Vite Entry point (Wraps App in ThemeProvider)