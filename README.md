# Task Tracker CLI 📝

A simple command-line interface (CLI) application to manage your tasks using Python and JSON. You can add, update, delete, mark status, and list tasks with ease from the terminal.

## 📦 Features

- Add new tasks
- Update existing tasks by ID
- Delete tasks by ID
- Mark tasks as `in-progress` or `done`
- List tasks by status: `todo`, `in-progress`, or `done`
- Data is stored in a `TaskTracker.json` file

---

## 🚀 Getting Started

### Requirements

- Python 3.7+
- Git (optional, for version control)
- 
## 🔧 Installation
### Clone the Repository

```bash
git clone https://github.com/aalqudah10/TaskTrackerCLI.git
cd TaskTrackerCLI
```
### Run the Script
```bash
python Task_Tracker_CLI.py <command> [options]
```

### 🛠️ Available Commands:
➕ Add a Task
```bash
python Task_Tracker_CLI.py add "Your task description"

✅ Example:
python Task_Tracker_CLI.py add "Your task description"
```

📝 Update a Task
```bash
python Task_Tracker_CLI.py update <id> "Updated description"

✅ Example:
python Task_Tracker_CLI.py update 3 "Call the bank"
```

❌ Delete a Task
```bash
python Task_Tracker_CLI.py delete <id>

✅ Example:
python Task_Tracker_CLI.py delete 2
```

🔄 Mark Task In Progress
```bash
python Task_Tracker_CLI.py mark-in-progress <id>

✅ Example:
python Task_Tracker_CLI.py mark-in-progress 1
```

✅ Mark Task as Done
```bash
python Task_Tracker_CLI.py mark-done <id>

✅ Example:
python Task_Tracker_CLI.py mark-done 1
```

📃 List Tasks
List all tasks:
```bash
python Task_Tracker_CLI.py list
```

Filter by status (todo, in-progress, done):
```bash
python Task_Tracker_CLI.py list todo
python Task_Tracker_CLI.py list in-progress
python Task_Tracker_CLI.py list done

✅ Example:
python Task_Tracker_CLI.py list done
```

### 📂 Data File
All tasks are saved to FILENAME (Desired Output JSON File) in the same directory.

### 🙌 Contributing
Feel free to fork the repo and submit a pull request to add features or improvements.
