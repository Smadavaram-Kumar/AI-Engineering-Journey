# 🚀 AI Engineering Journey — 30 Day Roadmap

**Author:** Smadavaram Kumar  
**Started:** April 2026  
**Goal:** Transition from Power Platform Developer → AI Engineer  
**Status:** In Progress

---

## 📋 Table of Contents

- [My Background](#my-background)
- [Progress Tracker](#progress-tracker)
- [Setup Guide — Complete Reference](#setup-guide--complete-reference)
  - [1. Understanding the Terminal](#1-understanding-the-terminal)
  - [2. Package Managers — Installing Software](#2-package-managers--installing-software)
  - [3. Installing Python](#3-installing-python)
  - [4. PATH — How Your Computer Finds Programs](#4-path--how-your-computer-finds-programs)
  - [5. Environment Variables](#5-environment-variables)
  - [6. App Execution Aliases — The Windows Trap](#6-app-execution-aliases--the-windows-trap)
  - [7. Installing VS Code](#7-installing-vs-code)
  - [8. Installing Git](#8-installing-git)
  - [9. Git and GitHub — Complete Guide](#9-git-and-github--complete-guide)
- [Week 1 — Python Foundations](#week-1--python-foundations)
  - [Day 1 — Python Basics](#day-1--python-basics)
- [Cheat Sheets](#cheat-sheets)

---

## My Background

Before starting this journey, I had experience with:
- **Copilot Studio** — Created agents using instructions, knowledge sources, actions, connectors, tools, orchestrator, triggers
- **Power Automate** — Created flows using triggers, different actions, data manipulations, conditional operators
- **Power Platform Administration** — Environment management, solution deployment
- **GitHub Actions** — Built CI/CD pipelines to deploy solutions from one environment to another, created SPN, Entra ID, and permissions
- **Claude Certifications** — AI Fluency Framework, 101, and Code in Action

---

## Progress Tracker

- [x] Day 1: Environment Setup + Python Basics
- [ ] Day 2: Functions & Modules
- [ ] Day 3: Data Structures Deep Dive
- [ ] Day 4: File Handling & Error Handling
- [ ] Day 5: Object-Oriented Programming
- [ ] Day 6: Essential Libraries (requests, dotenv)
- [ ] Day 7: Pandas, Matplotlib + Week 1 Project
- [ ] Day 8-14: AI/LLM Fundamentals
- [ ] Day 15-21: Building Real AI Apps
- [ ] Day 22-30: Production Skills & Job Prep

---

## Setup Guide — Complete Reference

> This section documents everything I learned about setting up a development environment from scratch on Windows. Written so that if I open this 6 months later, I can recollect everything.

---

### 1. Understanding the Terminal

A terminal is a way to talk to your computer using **text commands** instead of clicking buttons with your mouse.

**GUI (Graphical) vs Terminal (Text):**

| Action | GUI (Mouse) | Terminal (Text) |
|---|---|---|
| Open a folder | Double-click the folder | `cd foldername` |
| Create a folder | Right-click → New Folder | `mkdir foldername` |
| Create a file | Right-click → New File | `New-Item filename.py` |
| Delete a file | Drag to Recycle Bin | `Remove-Item filename.py` |
| See files in folder | Look at the window | `ls` |

**Why use the terminal?** Many developer tools (Git, pip, Docker) ONLY work through the terminal — there's no button to click. It's also much faster once you get used to it.

#### Types of Terminals on Windows

| Terminal | What It Is | Prompt Looks Like | Use It? |
|---|---|---|---|
| **Command Prompt (cmd)** | Oldest Windows terminal (since 1980s). Limited. | `C:\Users\smadavaram>` | ❌ Outdated |
| **PowerShell** | Modern replacement. More powerful. Pre-installed. | `PS C:\Users\smadavaram>` | ✅ Use this |
| **Windows Terminal** | Fancy app that holds cmd + PowerShell in tabs | Same as above | Optional |
| **Git Bash** | Linux-like terminal. Installed with Git. | `$ ` | Optional |

**I use PowerShell** — it works with everything I need.

#### Essential Terminal Commands

```
pwd                              → "Where am I?" (prints current folder path)
cd foldername                    → Go INTO a folder
cd ..                            → Go BACK one folder
cd ../..                         → Go BACK two folders
cd ~                             → Go to home folder (C:\Users\smadavaram)
cd C:\Users\smadavaram\Desktop   → Go to a specific path

ls                               → List files in current folder
ls -la                           → List ALL files including hidden ones

mkdir foldername                 → Create a new folder
New-Item filename.py             → Create a new empty file

Remove-Item filename.py          → Delete a file
Remove-Item foldername -Recurse  → Delete a folder and everything inside it

Copy-Item file.py newfile.py     → Copy a file
Move-Item file.py folder\file.py → Move a file

cat filename.py                  → Display file contents in terminal
clear                            → Clear the terminal screen
cls                              → Also clears screen (Windows shortcut)

code .                           → Open current folder in VS Code
```

**`code .` explained:** `code` refers to VS Code. `.` means "the current folder I'm in right now." So `code .` means "open VS Code and load this folder." If it doesn't work, open VS Code → press `Ctrl+Shift+P` → type "shell command" → click "Install 'code' command in PATH."

---

### 2. Package Managers — Installing Software

There are two ways to install anything:

**Method 1: Browser (The old way)**
```
Open browser → Go to website → Click Download → Wait → 
Find in Downloads → Double-click .exe → Next → Next → Next → Install → Done
(~2-3 minutes, many clicks)
```

**Method 2: Terminal using a Package Manager (The developer way)**
```
winget install Python.Python.3.12
(~30 seconds, one command)
```

**What IS a package manager?** A tool that knows where every software lives on the internet, downloads it for you, and installs it automatically. Like a personal assistant who goes shopping for you — you just say what you want.

#### Package Managers I Use

| Manager | What It Installs | Comes With | Example |
|---|---|---|---|
| **winget** | Desktop software (apps) | Windows 10/11 | `winget install Git.Git` |
| **pip** | Python libraries only | Python | `pip install anthropic` |

**winget — Windows Package Manager:**
```
winget install Python.Python.3.12    → Install Python
winget install Git.Git               → Install Git
winget install Microsoft.VisualStudioCode → Install VS Code
winget install GitHub.cli            → Install GitHub CLI

winget search python                 → Find packages with "python" in name
winget list                          → Show everything installed via winget
winget upgrade --all                 → Update ALL installed software
winget uninstall Git.Git             → Uninstall a package
winget show Python.Python.3.12       → Show details about a package
```

**pip — Python Package Manager:**
```
pip install anthropic                → Install Claude API library
pip install pandas                   → Install data manipulation library
pip install requests                 → Install HTTP calls library
pip install langchain                → Install AI framework

pip list                             → Show all installed Python libraries
pip install --upgrade pandas         → Update a specific library
pip uninstall pandas                 → Remove a library
pip freeze                           → Show all libraries with exact versions
pip freeze > requirements.txt        → Save list to file (for sharing projects!)
```

> **Key difference:** `winget` installs programs that run on your computer (like Git, VS Code). `pip` installs code libraries that run inside Python (like pandas, anthropic). There is NO browser way to install pip packages — terminal only.

**How to check if winget is available:**
```
winget --version
```
If you get "not recognized," update Windows: Settings → Windows Update → Check for updates.

---

### 3. Installing Python

**What is Python?** The #1 programming language for AI/ML. Every AI company (Anthropic, OpenAI, Google) provides Python SDKs first. It reads almost like English.

**Installation via terminal:**
```
winget install Python.Python.3.12
```

**After installation — CLOSE and REOPEN PowerShell (critical!).** Then verify:
```
python --version    → Should show: Python 3.12.10
pip --version       → Should show: pip 25.x.x from ... (python 3.12)
```

**If `python` says "not recognized":**
1. Disable App Execution Aliases (see Section 6 below)
2. Manually add Python to PATH (see Section 4 below)
3. Close and reopen PowerShell

**Where Python installs its files:**
```
C:\Users\smadavaram\AppData\Local\Programs\Python\Python312\
│
├── python.exe          ← The actual Python program
├── pythonw.exe         ← Python for GUI apps (no terminal window)
├── Lib/                ← Built-in Python libraries (json, csv, os, etc.)
│
└── Scripts/            ← Tools installed by pip live here
    ├── pip.exe         ← The pip command
    ├── pip3.exe        ← Same as pip
    ├── streamlit.exe   ← Appears after: pip install streamlit
    ├── uvicorn.exe     ← Appears after: pip install uvicorn
    └── ... (more tools appear as you pip install things)
```

**Why this folder structure matters:** See the PATH section below.

---

### 4. PATH — How Your Computer Finds Programs

When you type `python` in terminal, how does your computer know WHERE python.exe is located? Your computer has thousands of files — it can't search every folder every time.

**PATH is a list of folders where your computer looks for programs.**

```
You type: python --version
    ↓
Computer reads the PATH variable
    ↓
PATH says: "Look in these folders, in this order:"
  1. C:\Windows\System32                                    → python.exe here? No
  2. C:\Windows                                             → python.exe here? No
  3. C:\Users\smadavaram\...\Python\Python312               → python.exe here? YES!
    ↓
Runs it → Output: Python 3.12.10
```

**If the folder is NOT in PATH:** Computer searches all listed folders, finds nothing, shows: `"python is not recognized as a command"`

**See your current PATH:**
```
$env:PATH -split ";"
```
This prints every folder in your PATH, one per line.

**Find where any program lives:**
```
where.exe python    → Shows exact location of python.exe
where.exe pip       → Shows exact location of pip.exe
where.exe git       → Shows exact location of git.exe
```

#### Why Python Needs TWO Paths

```
PATH needs: C:\...\Python312           → finds python.exe ✅
            C:\...\Python312\Scripts   → finds pip.exe ✅, streamlit.exe ✅, uvicorn.exe ✅
```

The Python folder contains `python.exe` (the program itself). The Scripts subfolder contains `pip.exe` and every tool you install via pip. Your computer does NOT automatically search subfolders — you need to list both explicitly.

**Analogy:** Python312 is the main office building (where the CEO/python.exe sits). Scripts is the tools room inside the building (where pip, streamlit, uvicorn sit). You need to give directions to BOTH rooms.

#### Three Methods to Update PATH

**Method 1: GUI (Settings Window) — Permanent, many clicks**
```
1. Press Windows key → type "Environment Variables"
2. Click "Edit the system environment variables"
3. Click "Environment Variables" button
4. Select "Path" under User Variables → Click "Edit"
5. Click "New" → Type the folder path
6. Click OK → OK → OK
7. RESTART your terminal
```

**Method 2: PowerShell Command — Permanent, one command**
```powershell
[Environment]::SetEnvironmentVariable(
    "PATH",
    "$env:PATH;C:\your\new\path",
    [EnvironmentVariableTarget]::User
)
```

What each piece means:
- `[Environment]` — Accesses Windows' Environment system
- `::SetEnvironmentVariable()` — The function that sets/updates a variable
- `"PATH"` — The variable we're changing
- `"$env:PATH;C:\your\new\path"` — Keep current PATH + add new folder (`;` is the separator)
- `[EnvironmentVariableTarget]::User` — Save for my account only

**Method 3: Temporary (current session only)**
```
$env:PATH += ";C:\your\new\path"
```
Disappears when you close PowerShell. Good for testing.

| Method | Permanent? | Need to Restart Terminal? | Speed |
|---|---|---|---|
| GUI (Settings) | ✅ Yes | ✅ Yes | Slow |
| PowerShell command | ✅ Yes | ✅ Yes | Fast |
| `$env:PATH +=` | ❌ No (temporary) | ❌ No | Instant |

#### What Happens When You Install with winget?

```
winget install Python.Python.3.12
    ↓
Step 1: winget contacts Microsoft's package registry
Step 2: Registry sends download URL
Step 3: winget downloads the .exe installer
Step 4: winget runs installer SILENTLY (no GUI, automatic "Next Next Install")
Step 5: Files are placed on your computer
Step 6: Installer SHOULD add to PATH (but sometimes doesn't in silent mode!)
Step 7: winget reports "Successfully installed"
```

**The catch:** Step 6 sometimes fails with winget because silent mode might skip the "Add to PATH" checkbox. That's why browser installs can be more reliable for beginners — you SEE the checkbox.

#### After Any winget Install — The Verification Flow

```
Install something with winget
        ↓
Close and reopen PowerShell (ALWAYS!)
        ↓
Type the command (e.g., python --version)
        ↓
    ┌───────────────────┬──────────────────────┐
    │                   │                      │
 Shows version       "Not recognized"
    │                   │
    ↓                   ↓
 You're done ✅     Find where it installed:
                    where.exe python
                        │
                        ↓
                    Add that folder to PATH
                    (using any of the 3 methods above)
```

---

### 5. Environment Variables

PATH is just ONE of many **Environment Variables**. These are settings your computer stores and makes available to every program.

Think of them as your computer's personal notes:
```
PATH              = "where to find programs" (list of folders)
USERNAME          = "smadavaram"
HOMEPATH          = "\Users\smadavaram"
TEMP              = "C:\Users\...\Temp"
ANTHROPIC_API_KEY = "sk-ant-..." (we'll set this on Day 9 for Claude API)
```

**See all environment variables:**
```
Get-ChildItem env:
```

**See a specific one:**
```
$env:PATH
$env:USERNAME
$env:HOMEPATH
```

**Two types:**
- **User Variables** — Only for YOUR account. Other users can't see them.
- **System Variables** — For ALL users. Needs admin access to change.

When you type `python`, Windows combines BOTH User PATH and System PATH and searches all folders.

---

### 6. App Execution Aliases — The Windows Trap

**What happened to me:** I installed Python, but `python --version` kept saying "not found, install from Microsoft Store." Python WAS installed — Windows was blocking it!

**Why:** Windows has a special folder always in your PATH:
```
C:\Users\smadavaram\AppData\Local\Microsoft\WindowsApps\
```

Inside this folder, Windows places FAKE shortcut files:
```
WindowsApps/
├── python.exe      → NOT real Python! Redirects to Microsoft Store
├── python3.exe     → NOT real Python! Redirects to Microsoft Store
```

**The problem — order matters:**
```
PATH search order:
1. WindowsApps\python.exe     → FOUND! But it's FAKE → "Install from Store" ❌
   (Computer STOPS here — never reaches the real Python)
2. Python312\python.exe       → Real Python lives here, but never checked
```

**The fix:**
1. Press Windows key → type "App execution aliases"
2. Find **"Python (default) — python.exe"** → Turn **OFF**
3. Find **"Python (default) — python3.exe"** → Turn **OFF**
4. Close and reopen PowerShell

**After the fix:**
```
PATH search order:
1. WindowsApps\python.exe     → Removed! Skipped.
2. Python312\python.exe       → FOUND! Real Python → Python 3.12.10 ✅
```

**Analogy:** App Execution Aliases are like a receptionist who intercepts visitors and sends them to the wrong office. Turning them off removes the receptionist so visitors reach the right person.

---

### 7. Installing VS Code

```
winget install Microsoft.VisualStudioCode
```

Or download from **code.visualstudio.com**. During installation, check these boxes:
- ✅ Add to PATH
- ✅ Add "Open with Code" to file context menu
- ✅ Add "Open with Code" to directory context menu

**After installation, install these extensions:**
1. Open VS Code → Press `Ctrl+Shift+X` (Extensions)
2. Search **"Python"** by Microsoft → Install
3. Search **"Pylance"** → Install

**Verify:** Open new PowerShell, type `code --version`

**Useful VS Code shortcuts:**
| Shortcut | What It Does |
|---|---|
| `Ctrl+` ` | Open/close terminal inside VS Code |
| `Ctrl+S` | Save current file |
| `Ctrl+Shift+X` | Open Extensions panel |
| `Ctrl+Shift+P` | Open Command Palette (search any action) |
| `Ctrl+P` | Quick open file by name |

---

### 8. Installing Git

```
winget install Git.Git
```

Close and reopen PowerShell. Verify: `git --version`

**One-time setup — tell Git who you are:**
```
git config --global user.name "Smadavaram Kumar"
git config --global user.email "your-github-email@example.com"
```

Use the SAME email as your GitHub account. `--global` means "apply to ALL projects." You do this once, ever.

**Verify:**
```
git config --global user.name
git config --global user.email
```

---

### 9. Git and GitHub — Complete Guide

#### What Are They?

```
Git    = A save system on YOUR computer that remembers every version of your code
         (like Ctrl+S on steroids — saves history, not just current state)

GitHub = A cloud backup where others can see your work
         (like Google Drive for code — cloud storage + sharing)
```

#### Connecting Your Computer to GitHub

There are **two approaches** — both give the same result:

**Approach 1: Clone (Start from GitHub → bring to computer)**

```
cd C:\Users\smadavaram\OneDrive - Deloitte (O365D)\Desktop
git clone https://github.com/Smadavaram-Kumar/AI-Engineering-Journey.git
cd AI-Engineering-Journey
```

One command creates the folder, downloads everything, and sets up the connection. This is the easiest way.

**Approach 2: Init + Remote (Start from computer → connect to GitHub)**

Use this if clone fails (e.g., repo is completely empty):

```
mkdir AI-Engineering-Journey
cd AI-Engineering-Journey
git init                    ← "Start tracking this folder" (creates hidden .git folder)
git remote add origin https://github.com/Smadavaram-Kumar/AI-Engineering-Journey.git
                            ← "Connect to this GitHub URL"
```

What each command does:
- `mkdir` — Creates a normal folder (nothing special yet)
- `cd` — Enters the folder
- `git init` — Tells Git to start watching this folder (like hiring a secretary to track changes)
- `git remote add origin URL` — Links your folder to GitHub (`origin` is just a nickname for the URL)

**Both approaches end at the same place: a folder on your computer connected to GitHub.**

#### Checking Your Setup

```
git status      → "What's happening in my folder right now?"
                   Use DAILY — shows new/changed/staged files
                   RED files = Git sees them but isn't tracking
                   GREEN files = Ready to be committed
                   "nothing to commit" = Everything is saved

git remote -v   → "Am I connected to GitHub? Which URL?"
                   Use ONCE during setup to verify connection
                   Shows (fetch) = download URL and (push) = upload URL
```

#### The Git Flow — How Files Move

```
YOUR COMPUTER                                              GITHUB
─────────────                                              ──────

Write code      git add .       git commit        git push
    │               │               │                 │
    ▼               ▼               ▼                 ▼
┌──────────┐   ┌──────────┐   ┌───────────┐   ┌─────────────┐
│ Working  │──▶│ Staging  │──▶│  Local    │──▶│   Remote    │
│ Directory│   │ Area     │   │  History  │   │  (GitHub)   │
│          │   │          │   │           │   │             │
│ your     │   │ "packed  │   │ "sealed   │   │ "uploaded   │
│ files as │   │  in the  │   │  and      │   │  to cloud"  │
│ you edit │   │  box"    │   │  labeled" │   │             │
└──────────┘   └──────────┘   └───────────┘   └─────────────┘

                                               git pull
                                                  │
                                                  ▼
                                        Downloads changes from
                                        GitHub to your computer
```

#### SCENARIO 1: First Time Push

This is what you do ONCE — the very first time you push code:

```bash
# Step 1: Check what Git sees
git status                # Shows all new files in RED

# Step 2: Tell Git to track everything
git add .                 # All files turn GREEN (packed in box)

# Step 3: Create a save point with a description
git commit -m "Day 1: Initial setup, folder structure, and hello.py"
                          # Box is sealed and labeled

# Step 4: Name your branch (first time only!)
git branch -M main        # Names your branch "main"

# Step 5: Upload to GitHub (first time only with -u!)
git push -u origin main   # Uploads to GitHub
```

What each command does:
- `git add .` — "Track ALL files" (`.` means everything)
- `git commit -m "message"` — Create a snapshot with a description (`-m` = message)
- `git branch -M main` — Name the branch "main" (ONCE, first push only)
- `git push -u origin main` — Upload to GitHub (`-u` = "remember this setting," first push only)

After this, go to github.com/Smadavaram-Kumar/AI-Engineering-Journey and refresh — you'll see your files!

#### SCENARIO 2: Daily Push (Day 2, Day 3, Day 4... onwards)

Only 3 commands every day:

```bash
git add .
git commit -m "Day 2: Functions, modules, and utils.py practice"
git push
```

That's it! No `branch -M main`, no `-u origin main` — Git remembers from the first time.

**Good commit messages vs bad:**
```
"Day 1: Initial setup, folder structure, hello.py"  ✅ Clear, descriptive
"Day 3: Data structures — lists, dicts, sets"        ✅ Clear, descriptive
"updated stuff"                                       ❌ Vague
"asdfgh"                                              ❌ Meaningless
```

#### SCENARIO 3: Undo Mistakes

| Situation | Command | What It Does |
|---|---|---|
| Messed up a file, haven't committed | `git checkout -- filename.py` | Restores file to last commit (like Undo) |
| Committed but haven't pushed, want to undo | `git reset --soft HEAD~1` | Undoes last commit, keeps files |
| Pushed already, typo in message | Just make a new commit | Don't rewrite pushed history |

#### SCENARIO 4: Working on a Different Computer

**On the new computer:**
```bash
git clone https://github.com/Smadavaram-Kumar/AI-Engineering-Journey.git
cd AI-Engineering-Journey
code .
# Work on it, then push as usual
```

**Back on original computer:**
```bash
git pull    # Downloads latest changes from GitHub
```

**Rule:** Always run `git pull` before starting work if you pushed from another computer.

#### SCENARIO 5: See Exact Changes

```bash
git diff    # Shows what changed in every file
            # Lines with + were added (green)
            # Lines with - were removed (red)
```

---

## Week 1 — Python Foundations

### Day 1 — Python Basics

> **Goal:** Get Python running, understand variables, data types, control flow, and build your first program.

#### Variables — Storing Data

A variable is a name that stores a value. Like a labeled box.

```python
name = "Smadavaram"        # a box labeled "name" containing text
age = 25                   # a box labeled "age" containing a number
salary = 1500000.50        # a box labeled "salary" containing a decimal
is_employed = True         # a box labeled "is_employed" containing True/False
```

Python figures out the type automatically (**dynamic typing**) — you don't need to declare it.

#### The 8 Essential Data Types

**1. `str` (String) — Text data**

```python
name = "Smadavaram Kumar"
company = 'Deloitte'

# Key string operations:
len(name)                    # 16 (length)
name.upper()                 # "SMADAVARAM KUMAR"
name.lower()                 # "smadavaram kumar"
name.replace("Kumar", "K")  # "Smadavaram K"
name.split(" ")              # ["Smadavaram", "Kumar"]
name[0]                      # "S" (first character, index starts at 0)
name[0:10]                   # "Smadavaram" (slicing: index 0 to 9)
"Kumar" in name              # True (check if substring exists)
```

Strings are **immutable** — you cannot change individual characters. `name[0] = "X"` will error. You must create a new string.

**2. `int` (Integer) — Whole numbers**

```python
age = 25
big_number = 1_00_00_000    # 1 crore (underscores for readability)

age + 5       # 30 (addition)
age - 5       # 20 (subtraction)
age * 2       # 50 (multiplication)
age / 5       # 5.0 (division — ALWAYS returns float!)
age // 5      # 5 (floor division — returns int)
age % 3       # 1 (modulo — remainder)
age ** 2      # 625 (power — 25 squared)
```

> ⚠️ `/` always returns a float (5.0, not 5). Use `//` for integer division.

**3. `float` (Floating Point) — Decimal numbers**

```python
salary = 1500000.50
pi = 3.14159

# Caution — float precision:
0.1 + 0.2    # 0.30000000000000004 (NOT 0.3!) — known issue in ALL languages
round(0.1 + 0.2, 1)    # 0.3 (use round() to fix)
```

**4. `bool` (Boolean) — True or False**

```python
is_employed = True
is_student = False

# Booleans come from comparisons:
5 > 3       # True
5 == 3      # False (== checks equality, = assigns value)
5 != 3      # True (not equal)
5 >= 5      # True

# Logical operators:
True and False   # False (both must be True)
True or False    # True (at least one True)
not True         # False (flips the value)

# Truthy and Falsy (important for AI — checking API responses):
# Falsy: 0, 0.0, "", [], {}, None, False
# Everything else is Truthy
bool(0)       # False
bool("")      # False
bool("hello") # True
bool(42)      # True
```

**5. `list` — Ordered, changeable collection**

```python
skills = ["Python", "Power Platform", "GitHub Actions"]
numbers = [1, 2, 3, 4, 5]

# Access (index starts at 0):
skills[0]       # "Python" (first)
skills[-1]      # "GitHub Actions" (last)
skills[0:2]     # ["Python", "Power Platform"] (slice)

# Modify:
skills.append("LangChain")       # Add to end
skills.insert(1, "FastAPI")      # Insert at index 1
skills.remove("Power Platform")  # Remove by value
skills.pop()                     # Remove and return last item
skills.sort()                    # Sort alphabetically
len(skills)                      # Number of items
"Python" in skills               # True

# List comprehension (you'll use this daily):
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]    # [2, 4, 6, 8, 10]
squared = [n ** 2 for n in numbers]            # [1, 4, 9, 16, 25, ...]
```

**6. `dict` (Dictionary) — Key-Value pairs**

> **Most important for AI engineering** — API responses are JSON, and JSON = Python dictionaries.

```python
person = {
    "name": "Smadavaram",
    "age": 25,
    "skills": ["Python", "Power Platform"],
    "is_employed": True
}

# Access:
person["name"]              # "Smadavaram"
person.get("salary")        # None (no crash if key missing)
person.get("salary", 0)     # 0 (default value if missing)

# Modify:
person["salary"] = 1500000  # Add new key
person["age"] = 26          # Update existing
del person["is_employed"]   # Delete a key

# Useful methods:
person.keys()               # All keys
person.values()             # All values
person.items()              # All key-value pairs as tuples
"name" in person            # True (check if key exists)

# Nested dictionaries (like API responses):
api_response = {
    "content": [{"type": "text", "text": "Hello!"}],
    "model": "claude-sonnet-4-20250514",
    "usage": {"input_tokens": 10, "output_tokens": 5}
}
answer = api_response["content"][0]["text"]   # "Hello!"
```

**7. `tuple` — Ordered, UNCHANGEABLE collection**

```python
coordinates = (28.6139, 77.2090)    # Delhi
rgb_color = (255, 128, 0)

coordinates[0]     # 28.6139 (access like list)
# coordinates[0] = 30.0   # ERROR! Cannot modify tuples

# Tuple unpacking:
lat, lon = coordinates
print(f"Lat: {lat}, Lon: {lon}")

# Use tuple when data should NOT change (coordinates, RGB, DB rows)
# Use list when data WILL change (shopping cart, task list)
```

**8. `set` — Unordered, unique values only**

```python
skills = {"Python", "Python", "Java", "Python", "SQL"}
print(skills)    # {"Python", "Java", "SQL"} — duplicates removed!

frontend = {"HTML", "CSS", "JavaScript", "React"}
backend = {"Python", "Node.js", "JavaScript", "SQL"}

frontend & backend   # {"JavaScript"} — common (intersection)
frontend | backend   # All unique — combined (union)
frontend - backend   # {"HTML", "CSS", "React"} — only in frontend
```

#### Type Conversion

```python
int("25")        # String → Int: 25
str(2026)        # Int → String: "2026"
float("99.99")   # String → Float: 99.99
type("hello")    # <class 'str'> — check the type
```

#### print(), input(), type(), f-strings

```python
# print() — output to screen
print("Hello World")
print("Name:", name, "Age:", age)
print("2026", "04", "29", sep="-")    # 2026-04-29

# input() — get user input (ALWAYS returns string!)
name = input("Enter your name: ")
age = int(input("Enter your age: "))  # Convert to int immediately!

# type() — check data type
type(42)        # <class 'int'>
type("hello")   # <class 'str'>

# f-strings — THE way to format strings (always use this)
name = "Smadavaram"
age = 25
salary = 1500000

print(f"My name is {name} and I am {age} years old")
print(f"Next year I'll be {age + 1}")
print(f"Salary: ₹{salary:,}")           # Salary: ₹1,500,000
print(f"Pi: {3.14159:.2f}")              # Pi: 3.14
```

> ⚠️ `input()` ALWAYS returns a string. `"25" + 1` will crash. Always convert: `int(input(...))`

#### Control Flow — if/elif/else

```python
age = 25

if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# INDENTATION MATTERS in Python! Use 4 spaces.
# Wrong indentation = broken code.

# Combining conditions:
if age >= 21 and has_experience:
    print("Eligible")

if age < 18 or not has_experience:
    print("Not eligible")
```

#### Loops

```python
# for loop — repeat over a sequence:
skills = ["Python", "FastAPI", "LangChain"]
for skill in skills:
    print(f"I know {skill}")

# Loop with index:
for index, skill in enumerate(skills):
    print(f"{index + 1}. {skill}")

# range() — generate numbers:
for i in range(5):            # 0, 1, 2, 3, 4
for i in range(1, 6):         # 1, 2, 3, 4, 5
for i in range(0, 10, 2):     # 0, 2, 4, 6, 8

# Loop through dictionary:
for key, value in person.items():
    print(f"{key}: {value}")

# while loop — repeat while condition is true:
count = 0
while count < 5:
    print(count)
    count += 1    # Don't forget this → infinite loop!

# break = exit loop entirely
# continue = skip current iteration, go to next
```

#### Day 1 Experiment — Birth Year Calculator

```python
# birth_year_calculator.py
current_year = 2026

name = input("Enter your name: ")
age = int(input("Enter your age: "))

birth_year = current_year - age
print(f"Hello {name}! You were born in {birth_year}.")

if age < 0 or age > 150:
    print("That doesn't seem like a valid age!")
elif age < 18:
    print("You're young! Great time to start learning AI.")
elif age < 30:
    print("Perfect age to switch careers into AI engineering!")
else:
    print("It's never too late to learn something new!")
```

**Bonus challenges:**
1. Ask for birth month, calculate if they've had their birthday this year
2. Calculate days alive: `age * 365`
3. Store results in a dictionary and print with a loop

---

## Cheat Sheets

### Terminal Commands
```
pwd                     → Where am I?
cd folder               → Go into folder
cd ..                   → Go back one folder
ls                      → List files
mkdir folder            → Create folder
clear                   → Clear screen
code .                  → Open folder in VS Code
```

### Package Managers
```
winget install X        → Install software
winget search X         → Search for software
pip install X           → Install Python library
pip list                → Show installed libraries
```

### PATH & Environment
```
$env:PATH -split ";"   → See all PATH folders
$env:VARIABLENAME      → See any environment variable
where.exe python       → Find where a program lives

# Add to PATH permanently:
[Environment]::SetEnvironmentVariable("PATH", "$env:PATH;C:\new\path", [EnvironmentVariableTarget]::User)

# Add to PATH temporarily:
$env:PATH += ";C:\new\path"
```

### Git — Daily Workflow
```
# First time:
git add .
git commit -m "message"
git branch -M main
git push -u origin main

# Every day after:
git add .
git commit -m "message"
git push

# Useful:
git status              → What changed?
git diff                → Show exact changes
git pull                → Download from GitHub
git remote -v           → Am I connected? Where?
```

### Python Quick Reference
```python
# Variables & Types
name = "text"           # str
age = 25                # int
price = 9.99            # float
is_true = True          # bool
items = [1, 2, 3]       # list
data = {"key": "val"}   # dict
point = (x, y)          # tuple
unique = {1, 2, 3}      # set

# I/O
print(f"Hello {name}")
name = input("Name: ")
age = int(input("Age: "))

# Control flow
if condition:
    ...
elif other:
    ...
else:
    ...

for item in list:
    ...

while condition:
    ...
```

---

> **Note to future me:** If you're reading this after a long break, start from the [Setup Guide](#setup-guide--complete-reference) section. Everything is documented step by step with explanations of WHY, not just HOW. The cheat sheets at the bottom are your quick reference.

> **Philosophy:** The gap between "configuring AI tools" and "building AI tools" is bridged by writing code every single day. Consistency beats intensity.