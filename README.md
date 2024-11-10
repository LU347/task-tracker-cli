# task-tracker-cli
*A command-line tool for managing tasks, simulating a client-server interaction with a backend API and database*

https://roadmap.sh/projects/task-tracker

## Project Structure:
```
task-tracker-cli/
├── main.py        # CLI entry point, acts as the client, allows users to add, update, delete, and view tasks
├── api.py         # Simulates server, handling client requests and interacts with database layer
├── db.py          # Simulates database, manages task data, handles data storage and retrieval
└── README.md      # Project documentation
```

## Installation:
*must have python3 installed*
```
git clone https://github.com/LU347/task-tracker-cli.git
cd task-tracker-cli
```

## Usage:
1. Adding a task
```
python3 main.py add test
or
python3 main.py add "finish this readme"
```
2. Updating a task:
```
python3 main.py update 0 "new task" #{id of task} {new task}
```
3. Marking a task as done/in-progress:
```
python3 main.py mark-done 0 #id of task
python3 main.py mark-in-progress 0
```
4. List tasks:
```
python3 main.py list {filter: done/in-progress} #filter is optional, will list all tasks if blank
```
5. Delete a task:
```
python3 main.py delete 0 #id of task
```

😀

