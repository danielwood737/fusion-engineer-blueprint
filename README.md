# Fusion Engineer Blueprint — Release 1 Starter

This is the first working version of Daniel Wood's Fusion Engineer Blueprint web application.

## 1. Install the required tools

Install:

- Python from python.org
- Visual Studio Code
- Git
- Create a GitHub account

During Python installation on Windows, enable the option that adds Python to PATH if it is shown.

## 2. Open the project

1. Extract this ZIP file.
2. Open Visual Studio Code.
3. Select **File > Open Folder**.
4. Choose the extracted `fusion_engineer_blueprint_release_1` folder.
5. In VS Code, select **Terminal > New Terminal**.

## 3. Create a virtual environment

In the VS Code terminal, run:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once in the same terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 4. Install the application packages

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Run the app

```powershell
fastapi dev app/main.py
```

Open the address displayed in the terminal, normally:

`http://127.0.0.1:8000`

## 6. Your first coding task

Open `data/quests.json`.

Change the first quest's status from:

```json
"status": "Not Started"
```

to:

```json
"status": "Complete"
```

Save the file and refresh the browser. Your XP and progress should update.

## Release 1 goal

By the end of Release 1, this app will support:

- Completing quests with buttons
- Persistent XP
- Levels and titles
- Skill trees
- Achievements
- A Release 1 handbook
- Your LinkedIn and GitHub walkthroughs
