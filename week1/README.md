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

> This section documents everything I learned about setting up a development environment from scratch on Windows. 

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




# 🚀 Day 2 — Functions & Modules

**Author:** Smadavaram Kumar
**Day:** 2 of 30
**Goal:** Stop writing the same code twice. Learn to package logic into reusable functions, organize functions into modules, and start thinking like an engineer instead of a script-writer.

---

## 📋 Table of Contents

- [Why This Day Matters](#why-this-day-matters)
- [The Power Platform Connection](#the-power-platform-connection)
- [Part 1 — Functions](#part-1--functions)
  - [1.1 What Is a Function, Really?](#11-what-is-a-function-really)
  - [1.2 Defining a Function — The `def` Keyword](#12-defining-a-function--the-def-keyword)
  - [1.3 Parameters vs Arguments](#13-parameters-vs-arguments)
  - [1.4 `return` vs `print` — The Most Important Distinction](#14-return-vs-print--the-most-important-distinction)
  - [1.5 Default Arguments](#15-default-arguments)
  - [1.6 The Mutable Default Argument Trap](#16-the-mutable-default-argument-trap)
  - [1.7 Positional vs Keyword Arguments](#17-positional-vs-keyword-arguments)
  - [1.8 `*args` — Variable Positional Arguments](#18-args--variable-positional-arguments)
  - [1.9 `**kwargs` — Variable Keyword Arguments](#19-kwargs--variable-keyword-arguments)
  - [1.10 Scope — Where Variables Live](#110-scope--where-variables-live)
  - [1.11 Docstrings](#111-docstrings)
  - [1.12 Type Hints](#112-type-hints)
  - [1.13 Lambda Functions](#113-lambda-functions)
  - [1.14 `map()` — Apply a Function to Every Item](#114-map--apply-a-function-to-every-item)
  - [1.15 `sort(key=...)` — Tell Sort What to Sort By](#115-sortkey--tell-sort-what-to-sort-by)
  - [1.16 Common Function Mistakes](#116-common-function-mistakes)
- [Part 2 — Modules and Packages](#part-2--modules-and-packages)
  - [2.1 What Is a Module?](#21-what-is-a-module)
  - [2.2 Module vs Package vs Library](#22-module-vs-package-vs-library)
  - [2.3 Built-in Modules — The Standard Library](#23-built-in-modules--the-standard-library)
  - [2.4 The Four Ways to Import](#24-the-four-ways-to-import)
  - [2.5 Creating Your Own Module](#25-creating-your-own-module)
  - [2.6 `if __name__ == "__main__":` — The Most Important Pattern](#26-if-__name__--__main__--the-most-important-pattern)
  - [2.7 Building a Real Package — Hands On](#27-building-a-real-package--hands-on)
- [Part 3 — How `import` Actually Works](#part-3--how-import-actually-works)
  - [3.1 The One Big Idea](#31-the-one-big-idea)
  - [3.2 Investigation: What `sys.path` Looks Like](#32-investigation-what-syspath-looks-like)
  - [3.3 Investigation: Look Inside the Standard Library](#33-investigation-look-inside-the-standard-library)
  - [3.4 Investigation: `__file__` Reveals Everything](#34-investigation-__file__-reveals-everything)
  - [3.5 Investigation: Watch Import Succeed](#35-investigation-watch-import-succeed)
  - [3.6 Investigation: Watch Import Fail](#36-investigation-watch-import-fail)
  - [3.7 Diagnostic Checklist for Import Errors](#37-diagnostic-checklist-for-import-errors)
- [Part 4 — PyPI and pip](#part-4--pypi-and-pip)
  - [4.1 What PyPI Is](#41-what-pypi-is)
  - [4.2 Useful pip Commands](#42-useful-pip-commands)
  - [4.3 The Connection: PyPI → site-packages → import](#43-the-connection-pypi--site-packages--import)
- [Part 5 — Environment Variables and PYTHONPATH](#part-5--environment-variables-and-pythonpath)
  - [5.1 The Connection to Day 1](#51-the-connection-to-day-1)
  - [5.2 What Environment Variables Actually Are](#52-what-environment-variables-actually-are)
  - [5.3 What `PYTHONPATH` Specifically Does](#53-what-pythonpath-specifically-does)
  - [5.4 Setting PYTHONPATH Permanently — GUI Method](#54-setting-pythonpath-permanently--gui-method)
  - [5.5 Setting PYTHONPATH Permanently — PowerShell Method](#55-setting-pythonpath-permanently--powershell-method)
  - [5.6 Diagnostic — When `$env:PYTHONPATH` is Empty](#56-diagnostic--when-envpythonpath-is-empty)
  - [5.7 The AI Engineering Payoff: API Keys](#57-the-ai-engineering-payoff-api-keys)
  - [5.8 The Full Picture](#58-the-full-picture)
- [Part 6 — The Day 2 Experiment](#part-6--the-day-2-experiment)
- [Cheat Sheets](#cheat-sheets)
- [Looking Ahead](#looking-ahead)

---

## Why This Day Matters

Yesterday you wrote code top-to-bottom — every line ran in order, once. That's fine for a 10-line script. But **every real AI app you'll build** looks like this:

```
chat_with_claude()      ← function
parse_response()        ← function
save_to_database()      ← function
send_email()            ← function
```

Functions are how working code gets organized. Modules are how working code gets shared.

### The DRY principle

**DRY = Don't Repeat Yourself.** If you've written the same 3 lines twice, those lines belong in a function. Every senior engineer follows this religiously, because copy-pasted code is where bugs go to multiply.

```python
# ❌ Bad — copy-pasted logic
celsius1 = 25
fahrenheit1 = (celsius1 * 9/5) + 32

celsius2 = 30
fahrenheit2 = (celsius2 * 9/5) + 32

# ✅ Good — one function, used twice
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(25))   # 77.0
print(celsius_to_fahrenheit(30))   # 86.0
```

If the formula is wrong, you fix it in **one place** instead of fifty. That's why functions exist.

---

## The Power Platform Connection

You already know this concept — you just called it something else:

| Power Platform | Python | What It Does |
|---|---|---|
| A flow in Power Automate | A function | Takes inputs, does something, returns output |
| An "Action" in Copilot Studio | A function | Reusable unit of work |
| A child flow | A function called by another function | Compose bigger flows from smaller ones |
| A solution (the .zip you export) | A package | Bundle of related logic you can import elsewhere |

When you built a Power Automate flow that "takes an email, extracts attachment, saves to SharePoint" — that was a function. You're not learning a new concept. You're learning new syntax for a concept you already use daily.

**Future connection:** When you build agents with Claude using "tool use" / function calling, you'll register Python functions AS tools that Claude can decide to call. Same model. The functions you write today become the tools your future Claude agent uses tomorrow.

---

## Part 1 — Functions

### 1.1 What Is a Function, Really?

A function is a **named, reusable block of code** that:
1. Optionally takes some inputs (called **parameters**)
2. Does some work
3. Optionally gives back a result (called the **return value**)

**Analogy — a vending machine:**

```
You insert ₹50 + press button "B3"            ← INPUTS (parameters)
Machine grinds, brews, drops a cup of coffee  ← WORK (function body)
You receive the coffee                         ← OUTPUT (return value)
```

You don't care HOW the machine makes coffee. You just care that it takes inputs and gives output. That's what a function offers other code: a clean interface where the messy details are hidden inside.

---

### 1.2 Defining a Function — The `def` Keyword

```python
def greet(name):
    return f"Hello, {name}!"
```

Anatomy:

```
def greet(name):
│    │      │   │
│    │      │   └── Colon — REQUIRED. Marks start of function body.
│    │      └────── Parameter — input the function expects
│    └───────────── Function name — what you'll call it later
└────────────────── "def" — keyword that says "I'm defining a function"

    return f"Hello, {name}!"
    │      │
    │      └── The value the function gives back
    └───────── 4-space indent — tells Python "this is INSIDE the function"
```

**Defining vs calling — two separate things:**

```python
def greet(name):                  # DEFINITION — Python remembers it.
    return f"Hello, {name}!"      # The function does NOT run yet.

result = greet("Smadavaram")      # CALL — NOW the function runs.
print(result)                     # Hello, Smadavaram!
```

> ⚠️ **Common beginner trap:** Defining a function does nothing visible. You won't see "Hello, Smadavaram!" appear until you actually CALL the function with `greet("Smadavaram")`.

---

### 1.3 Parameters vs Arguments

These two words get used interchangeably, but they mean different things:

```python
def greet(name):           # "name" is a PARAMETER (variable in the definition)
    return f"Hello, {name}!"

greet("Smadavaram")        # "Smadavaram" is an ARGUMENT (actual value passed in)
```

| Term | Where | Example |
|---|---|---|
| **Parameter** | In the function definition | `def greet(name):` ← `name` |
| **Argument** | When you call the function | `greet("Smadavaram")` ← `"Smadavaram"` |

Mnemonic: **P**arameter = **P**laceholder. **A**rgument = **A**ctual value.

You can have many parameters:

```python
def add(a, b):
    return a + b

result = add(5, 3)    # 8
```

---

### 1.4 `return` vs `print` — The Most Important Distinction

This is where 90% of beginners get confused. Read this section twice.

```python
def add_with_print(a, b):
    print(a + b)         # Just shows it. Function returns NOTHING.

def add_with_return(a, b):
    return a + b         # Hands the value BACK to whoever called it.
```

Watch what happens:

```python
result1 = add_with_print(5, 3)
# Screen shows: 8
# But result1 = None  (function didn't return anything!)

result2 = add_with_return(5, 3)
# Screen shows: nothing
# But result2 = 8  (the value is now usable!)

# Now look what you can do with result2 but NOT result1:
final = add_with_return(5, 3) * 10    # Works! 80
final = add_with_print(5, 3) * 10     # CRASH! Can't multiply None by 10
```

**The rule:**

| Want to... | Use |
|---|---|
| Show a value to the user | `print()` |
| Hand a value to other code | `return` |

In AI engineering you almost always use `return`. Functions feed into other functions. The text Claude returns gets passed to a parser, which passes to a database saver. `print()` is for debugging only.

**A function with no return statement returns `None` automatically:**

```python
def do_nothing():
    pass    # "pass" = "this block is intentionally empty"

x = do_nothing()
print(x)    # None
```

**You can return early to exit a function:**

```python
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"   # Function exits here. No further lines run.
    return a / b
```

**You can return multiple values (it's actually a tuple):**

```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([5, 2, 8, 1, 9])
print(low, high)    # 1 9
```

---

### 1.5 Default Arguments

Sometimes you want a parameter to have a fallback value if the caller doesn't provide one.

```python
def greet(name, greeting="Hello"):     # greeting has a default
    return f"{greeting}, {name}!"

greet("Smadavaram")                    # "Hello, Smadavaram!"     — uses default
greet("Smadavaram", "Hey")             # "Hey, Smadavaram!"       — overrides default
greet("Smadavaram", greeting="Namaste") # "Namaste, Smadavaram!"  — explicit by name
```

**Rule:** Parameters with defaults must come AFTER parameters without defaults.

```python
def good(a, b=10):       # ✅ OK
    return a + b

def bad(a=10, b):        # ❌ SyntaxError! Default before non-default.
    return a + b
```

---

### 1.6 The Mutable Default Argument Trap

This is one of the most famous "gotchas" in Python. Senior engineers catch it in code review immediately. Now you'll be able to too.

#### What you'd expect

```python
def add_skill(skill, skills=[]):
    skills.append(skill)
    return skills

print(add_skill("Python"))    # You'd expect: ['Python']
print(add_skill("FastAPI"))   # You'd expect: ['FastAPI']  (fresh empty list, right?)
```

Reasonable expectation. Wrong.

#### What actually happens

```python
print(add_skill("Python"))    # ['Python']
print(add_skill("FastAPI"))   # ['Python', 'FastAPI']  ← what?!
print(add_skill("LangChain")) # ['Python', 'FastAPI', 'LangChain']  ← growing!
```

The list keeps growing across calls. Each call sees the leftovers from previous calls.

#### Why — The Mental Model

Here's the rule that explains everything:

> **The default value `[]` is created ONCE, when the `def` line is executed (i.e., when Python first reads your file). It is then ATTACHED to the function. Every call that doesn't supply `skills` reuses the SAME list object.**

Step-by-step:

```
1. Python reads:   def add_skill(skill, skills=[]):
        ↓
2. Python evaluates the default value [] RIGHT NOW.
   Creates an empty list in memory.
        Memory: list_at_address_0x7f8 → []
        ↓
3. Python stores a reference to that list with the function.
        add_skill.__defaults__ = (list_at_address_0x7f8,)
        ↓
4. You call add_skill("Python")
   - You didn't pass skills, so Python uses the stored default.
   - skills = list_at_address_0x7f8  (the same object)
   - .append("Python") → list_at_address_0x7f8 is now ["Python"]
        ↓
5. You call add_skill("FastAPI")
   - Again, no skills argument, so Python uses the stored default.
   - skills = list_at_address_0x7f8  (STILL the same object — never changed!)
   - .append("FastAPI") → list_at_address_0x7f8 is now ["Python", "FastAPI"]
```

**The default isn't `[]`. The default is *that specific list, the one created when the function was defined*.** That list lives across all calls. Any modification persists.

#### Verify it Yourself

```python
def add_skill(skill, skills=[]):
    skills.append(skill)
    return skills

# Look at the function's stored defaults BEFORE any calls:
print(add_skill.__defaults__)    # ([],)

add_skill("Python")
print(add_skill.__defaults__)    # (['Python'],)  ← the stored default itself was modified!

add_skill("FastAPI")
print(add_skill.__defaults__)    # (['Python', 'FastAPI'],)
```

The `__defaults__` attribute literally shows the list growing. It's the same object every time.

#### Why Strings, Ints, and Tuples Don't Have This Problem

```python
def greet(name="Smadavaram"):    # ✅ SAFE
    return f"Hi {name}"
```

`"Smadavaram"` is **immutable** — you can't modify a string in place. `name + "!"` creates a *new* string; the original default is untouched. Same for `int`, `float`, `bool`, `tuple`, `None`.

The trap only fires for **mutable** defaults: `list`, `dict`, `set`, custom class instances.

| Type | Mutable? | Safe as default? |
|---|---|---|
| `int`, `float`, `str`, `bool`, `tuple`, `None` | No | ✅ Yes |
| `list` (e.g., `[]`) | Yes | ❌ DANGEROUS |
| `dict` (e.g., `{}`) | Yes | ❌ DANGEROUS |
| `set` (e.g., `set()`) | Yes | ❌ DANGEROUS |

#### The Fix — Use `None` as a Sentinel

```python
def add_skill(skill, skills=None):
    if skills is None:
        skills = []         # ← fresh list every call
    skills.append(skill)
    return skills

print(add_skill("Python"))    # ['Python']
print(add_skill("FastAPI"))   # ['FastAPI']    ✅ fresh list
print(add_skill("LangChain")) # ['LangChain']  ✅ fresh list
```

`None` is immutable, so it's safe as a default. The `if skills is None: skills = []` line creates a brand-new list on every call where the user didn't pass one.

#### Why This Matters for AI Engineering

You'll write functions that take optional **conversation history** or optional **tool lists** all the time:

```python
# ❌ BUG — every call without history shares the same list:
def chat(message, history=[]):
    history.append({"role": "user", "content": message})
    return history

# ✅ CORRECT:
def chat(message, history=None):
    if history is None:
        history = []
    history.append({"role": "user", "content": message})
    return history
```

The first version would silently leak conversations across users in a multi-user app. **This is a real bug that ships in real AI apps.** Now you'll never write it.

#### The One-Sentence Rule

> **Never put a mutable value (`[]`, `{}`, `set()`) in a function's default arguments. Use `None` and create the value inside.**

---

### 1.7 Positional vs Keyword Arguments

When you call a function, you can pass arguments two ways:

```python
def book_flight(origin, destination, passengers, seat_class):
    return f"{passengers} pax, {origin} → {destination}, {seat_class}"

# Positional — order matters, and order MUST match the definition:
book_flight("Hyderabad", "Delhi", 2, "Economy")

# Keyword — order doesn't matter, and code is self-documenting:
book_flight(
    destination="Delhi",
    passengers=2,
    origin="Hyderabad",
    seat_class="Economy"
)
```

For 1-2 parameters, positional is fine. For 4+, **always use keyword arguments** — your future self will thank you when reading the code 6 months later.

You can mix them, but positional ones must come first:

```python
book_flight("Hyderabad", "Delhi", passengers=2, seat_class="Economy")   # ✅
book_flight(origin="Hyderabad", "Delhi", 2, "Economy")                  # ❌ Error
```

---

### 1.8 `*args` — Variable Positional Arguments

Sometimes you don't know how many arguments will be passed in. Example: a function that sums up any number of numbers.

```python
def sum_all(*numbers):       # The * means "collect any extra positional args into a tuple called 'numbers'"
    total = 0
    for n in numbers:
        total += n
    return total

sum_all(1, 2)             # 3
sum_all(1, 2, 3, 4, 5)    # 15
sum_all(99)               # 99
sum_all()                 # 0  (empty tuple)
```

The name `args` is just convention. `*numbers`, `*items`, `*things` all work. But seeing `*args` is so common that everyone immediately knows what it means.

You can mix regular params with `*args`:

```python
def report(title, *items):
    print(f"=== {title} ===")
    for item in items:
        print(f"- {item}")

report("Today's Tasks", "Code", "Read docs", "Push to GitHub")
# === Today's Tasks ===
# - Code
# - Read docs
# - Push to GitHub
```

---

### 1.9 `**kwargs` — Variable Keyword Arguments

Same idea, but for keyword arguments. Collected into a **dictionary**.

```python
def build_profile(**details):     # ** means "collect extra keyword args into a dict called 'details'"
    for key, value in details.items():
        print(f"{key}: {value}")

build_profile(name="Smadavaram", age=25, role="AI Engineer", company="Deloitte")
# name: Smadavaram
# age: 25
# role: AI Engineer
# company: Deloitte
```

**Why this matters for AI engineering:** API calls take dozens of optional parameters (temperature, max_tokens, top_p, system_prompt, …). `**kwargs` lets you write wrapper functions that pass through any options without listing them all.

```python
def call_claude(prompt, **options):
    # options might be {"temperature": 0.7, "max_tokens": 500, ...}
    return anthropic_client.messages.create(
        messages=[{"role": "user", "content": prompt}],
        **options    # "unpacks" the dict back into keyword arguments
    )

call_claude("Hello", temperature=0.7, max_tokens=500)
```

**The full signature pattern (memorize this order):**

```python
def my_function(positional, default="x", *args, **kwargs):
                │           │            │      │
                │           │            │      └── ANY keyword args  → dict
                │           │            └────────── ANY positional args → tuple
                │           └─────────────────────── Has a default value
                └─────────────────────────────────── Required positional
```

---

### 1.10 Scope — Where Variables Live

Variables created **inside** a function exist only inside that function (**local scope**).

```python
def calculate():
    secret = 42         # Local — only visible inside calculate()
    return secret

result = calculate()    # 42
print(secret)           # ❌ NameError! 'secret' doesn't exist out here.
```

Variables defined **outside** any function are **global** — visible everywhere.

```python
PI = 3.14159    # Global — convention is ALL_CAPS for constants

def area(radius):
    return PI * radius ** 2     # Can READ PI from inside
```

> ⚠️ **You can read globals inside a function, but assigning to one creates a NEW local variable** unless you use the `global` keyword. In real code, `global` is almost always a sign you should be passing the value as a parameter instead.

**Why scope matters:** It's why functions are safe to use. When you call `celsius_to_fahrenheit(25)`, the function can't accidentally mess with variables in the rest of your program. Each function is its own little sandbox.

---

### 1.11 Docstrings

A docstring is a string right under the `def` line that describes what the function does. Anyone reading the code (including future-you) gets free documentation.

```python
def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32
```

You can read any function's docstring with `help()`:

```python
help(celsius_to_fahrenheit)    # Prints the docstring
```

**Habit to build:** Every function you write gets at least a one-line docstring.

---

### 1.12 Type Hints

Python doesn't *force* you to declare types, but you can hint at them. Modern AI codebases use type hints everywhere.

```python
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
```

Read this as: "celsius is a float, function returns a float."

| Hint | Meaning |
|---|---|
| `name: str` | Parameter `name` should be a string |
| `count: int` | Parameter `count` should be an int |
| `prices: list` | Parameter `prices` should be a list |
| `data: dict` | Parameter `data` should be a dict |
| `-> bool` | Function returns a bool |
| `-> None` | Function returns nothing |

> Type hints are **suggestions, not enforcement**. Python won't crash if you pass the wrong type. But your editor (VS Code with Pylance) will warn you. Start the habit now.

---

### 1.13 Lambda Functions

`lambda` is a way to write a **tiny, nameless function** in one line. These two are identical:

```python
# Long way:
def double(x):
    return x * 2

# Short way (lambda):
double = lambda x: x * 2

double(5)    # 10 either way
```

Anatomy:

```
lambda n: n ** 2
│      │  │
│      │  └── the expression that gets returned (no "return" keyword needed)
│      └───── parameter(s) — what the function takes in
└──────────── the keyword "lambda"
```

You'd use `lambda` when you need a function for ONE moment and don't want to write a full `def` for it. Lambdas shine when a function takes another function as an argument — see `map()` and `sort()` next.

---

### 1.14 `map()` — Apply a Function to Every Item

`map(function, iterable)` does exactly one thing: **applies the function to every item in the iterable**, one at a time.

Visual:

```
items = [1, 2, 3, 4, 5]

map(some_function, items)
   │
   └── runs:    some_function(1)
                some_function(2)
                some_function(3)
                some_function(4)
                some_function(5)
   
   collects results: [result1, result2, result3, result4, result5]
```

So:

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda n: n ** 2, numbers))
#         │    │   │            │
#         │    │   │            └── the input list
#         │    │   └─────────────── tiny function: "given n, return n²"
#         │    └─────────────────── apply that function to every item
#         └──────────────────────── force it to compute and give me a list

# Result: [1, 4, 9, 16, 25]
```

**Why `list(...)` around it?** For efficiency, `map()` doesn't actually compute anything until you ask. It returns a **lazy iterator** — a recipe, not the meal. Calling `list(...)` says "okay, run the recipe and give me an actual list."

```python
result = map(lambda n: n ** 2, [1, 2, 3])
print(result)         # <map object at 0x...>   ← not a list! it's a recipe
print(list(result))   # [1, 4, 9]                ← now it's actually computed
```

**The modern Pythonic alternative — list comprehension:**

```python
# These are EQUIVALENT — pick whichever you find clearer:
squared = list(map(lambda n: n ** 2, numbers))    # map + lambda
squared = [n ** 2 for n in numbers]                # list comprehension
```

You'll see both in the wild — be able to read both, but write list comprehensions by default.

**AI engineering example — extract text from a batch of API responses:**

```python
responses = [
    {"content": [{"text": "Reply 1"}]},
    {"content": [{"text": "Reply 2"}]},
    {"content": [{"text": "Reply 3"}]},
]

texts = [r["content"][0]["text"] for r in responses]
# ['Reply 1', 'Reply 2', 'Reply 3']
```

---

### 1.15 `sort(key=...)` — Tell Sort What to Sort By

When you sort numbers or strings, sorting is obvious — there's a built-in order:

```python
nums = [3, 1, 2]
nums.sort()           # [1, 2, 3]   — clear: smaller first

words = ["cherry", "apple", "banana"]
words.sort()          # ["apple", "banana", "cherry"]   — alphabetical
```

But what about a list of dictionaries?

```python
people = [{"name": "A", "age": 30}, {"name": "B", "age": 25}]
people.sort()    # ❌ TypeError: '<' not supported between dicts
```

Python doesn't know what "smaller" means for a dict. Should it sort by `name`? By `age`? Python won't guess — **you have to tell it**.

`key` takes a function. For each item in the list, sort calls that function and uses the result as the value to sort by.

```python
people.sort(key=lambda p: p["age"])
#               │
#               └── "For each person p, the thing to sort by is p['age']"
```

What sort actually does:

```
For each item, run the key function:
    {"name": "A", "age": 30}    → key returns 30
    {"name": "B", "age": 25}    → key returns 25

Sort the items by those returned values (smallest first):
    25 < 30, so B comes before A.

Result: [{"name": "B", "age": 25}, {"name": "A", "age": 30}]
```

**Other `key` patterns you'll use constantly:**

```python
# Sort strings by length:
words = ["banana", "fig", "apple"]
words.sort(key=lambda w: len(w))      # ['fig', 'apple', 'banana']

# Sort case-insensitive:
names = ["bob", "Alice", "charlie"]
names.sort(key=lambda n: n.lower())   # ['Alice', 'bob', 'charlie']

# Sort newest first:
events.sort(key=lambda e: e["date"], reverse=True)

# Sort by multiple keys (return a tuple):
students.sort(key=lambda s: (s["grade"], s["name"]))   # by grade, then by name
```

**AI engineering example — sort RAG search results by relevance:**

```python
search_results = [
    {"doc": "Article A", "score": 0.72},
    {"doc": "Article B", "score": 0.91},
    {"doc": "Article C", "score": 0.85},
]

# Most relevant first:
search_results.sort(key=lambda r: r["score"], reverse=True)
```

This is **literally how you'd post-process retrieval results** before feeding them to Claude. You will write this code.

---

### 1.16 Common Function Mistakes

```python
# ❌ Forgetting parentheses to CALL it:
greet                  # This is the function OBJECT, not a call. Does nothing.
greet()                # ✅ Calls the function.

# ❌ Forgetting return:
def add(a, b):
    a + b              # Computed and thrown away! Returns None.

def add(a, b):
    return a + b       # ✅

# ❌ Indentation off:
def add(a, b):
return a + b           # ❌ IndentationError

def add(a, b):
    return a + b       # ✅ 4 spaces

# ❌ Using a variable that doesn't exist in scope:
def show():
    print(x)           # ❌ NameError if x isn't defined inside or globally

# ❌ Mutable default argument:
def f(items=[]):       # ❌ Bug magnet — see 1.6
    ...
```

---

## Part 2 — Modules and Packages

### 2.1 What Is a Module?

**A module is just a `.py` file.** That's the entire definition.

When you have `utils.py` containing useful functions, that file IS a module. Any other Python file can `import utils` and use everything inside.

**Analogy — a toolbox:**

```
You have a wrench, hammer, screwdriver scattered on the floor → painful.
You put them in a labeled toolbox.
Now any project can grab the toolbox, use a tool, put it back.

A module = the toolbox.
A function = a tool inside it.
import = picking up the toolbox.
```

**Why modules exist:**
1. **Organize big projects** — A real AI app has 50+ files, not one giant `main.py`.
2. **Reuse across projects** — Write `database_helpers.py` once, import in every project.
3. **Share with the world** — Public modules on PyPI = the entire `pip install` ecosystem.

---

### 2.2 Module vs Package vs Library

The terms get thrown around constantly. Lock them down:

| Term | What It Is | Concrete Example |
|---|---|---|
| **Module** | A single `.py` file containing Python code | `utils.py` |
| **Package** | A folder containing multiple modules, marked by `__init__.py` | `helpers/` folder |
| **Library** | Informal — any reusable code, usually a package | `pandas` |
| **Framework** | A big library that provides structure for whole apps | `langchain`, `fastapi` |

**Important nuance:** A module isn't ONLY functions. It can hold:
- Functions (`def ...`)
- Variables / constants (`PI = 3.14`)
- Classes (`class Customer: ...`)
- Even runnable code at the top level (which runs on import)

So a more accurate definition: **A module is any `.py` file that other Python code can `import`.**

**The visual:**

```
┌─────────────────────────────────────────────────────────┐
│  PACKAGE (a folder)                                     │
│                                                         │
│   ai_toolkit/                                           │
│   │                                                     │
│   ├── __init__.py        ← marks this folder a package  │
│   │                                                     │
│   ├── text_helpers.py    ┐                              │
│   │                      │                              │
│   ├── api_helpers.py     ├── Each .py file = a MODULE   │
│   │                      │                              │
│   └── parsers.py         ┘                              │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**The Power Platform analogy:**

| Power Platform | Python |
|---|---|
| A **solution** in Power Platform (the .zip) | A **package** |
| Each component inside the solution (a flow, a connector) | A **module** inside the package |
| A single Power Automate flow | A **function** inside a module |
| Importing a solution into a new environment | `pip install` a package + `import` it |

---

### 2.3 Built-in Modules — The Standard Library

Python ships with 200+ ready-to-use modules. The ones you'll actually use:

```python
import math

math.pi              # 3.141592653589793
math.sqrt(16)        # 4.0
math.ceil(4.2)       # 5  (round up)
math.floor(4.8)      # 4  (round down)
```

```python
import random

random.randint(1, 10)              # Random int between 1 and 10 (inclusive)
random.random()                    # Random float between 0 and 1
random.choice(["A", "B", "C"])     # Random pick from a list
random.shuffle(my_list)            # Shuffles the list in place
```

```python
import datetime

datetime.datetime.now()            # 2026-04-30 14:23:01.123456
datetime.date.today()              # 2026-04-30
today = datetime.date.today()
today.strftime("%d-%b-%Y")         # "30-Apr-2026"
```

```python
import json

# Convert Python dict → JSON string (for sending to APIs):
data = {"name": "Smadavaram", "skills": ["Python"]}
json_string = json.dumps(data)

# Convert JSON string → Python dict (for reading API responses):
api_text = '{"role": "assistant", "content": "Hi!"}'
parsed = json.loads(api_text)      # {'role': 'assistant', 'content': 'Hi!'}
parsed["content"]                  # "Hi!"
```

```python
import os

os.getcwd()                        # Current folder path
os.listdir(".")                    # Files in current folder
os.path.exists("utils.py")         # True/False
os.environ.get("ANTHROPIC_API_KEY") # Read environment variable (Day 9!)
```

> 💡 **For AI work specifically, internalize `json` and `os.environ.get()`** — every API response is JSON, and every API key gets read from an environment variable. You'll use these every single day.

---

### 2.4 The Four Ways to Import

```python
# Way 1: import the whole module
import math
math.sqrt(16)             # Must prefix with module name

# Way 2: import the whole module with an alias
import math as m
m.sqrt(16)                # Shorter; used a LOT in data work (e.g., import pandas as pd)

# Way 3: import specific items from a module
from math import sqrt, pi
sqrt(16)                  # No prefix needed
pi                        # Direct access

# Way 4: import everything (USE WITH CAUTION)
from math import *
sqrt(16)                  # Works, but...
```

**When to use which:**

| Style | When |
|---|---|
| `import math` | You'll use multiple things from it; want to see clearly where they came from |
| `import pandas as pd` | The library is universally aliased (pandas = pd, numpy = np, matplotlib.pyplot = plt) |
| `from math import sqrt` | You only need 1-2 things and the name is clear |
| `from math import *` | **Almost never.** It pollutes your namespace and hides where things come from |

> ⚠️ **Why `from x import *` is bad:** If two modules both have a function called `load()`, the second `import *` silently overwrites the first. You won't know until something breaks. Be explicit.

---

### 2.5 Creating Your Own Module

There is no ceremony. Just a `.py` file.

**`my_helpers.py`:**

```python
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159
```

**`main.py` in the same folder:**

```python
import my_helpers

print(my_helpers.greet("Smadavaram"))    # Hello, Smadavaram!
print(my_helpers.add(2, 3))              # 5
print(my_helpers.PI)                     # 3.14159
```

That's it. You created a module.

---

### 2.6 `if __name__ == "__main__":` — The Most Important Pattern

You'll see this line in **every professional Python file**. Most beginners cargo-cult it without understanding it. You're going to actually understand it.

#### The problem it solves

Imagine `utils.py`:

```python
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Quick test:
print(celsius_to_fahrenheit(100))    # 212.0
```

When you run `python utils.py` directly → you see `212.0`. Good.

But now `main.py` does:

```python
import utils
print(utils.celsius_to_fahrenheit(0))    # 32.0
```

When you run `python main.py` → you see **`212.0` AND `32.0`**! Why?

Because `import utils` actually **runs the entire utils.py file from top to bottom**. The `print(...)` line at the bottom of utils.py executes during the import. Every time anyone imports your module, they get that test output. Annoying.

#### The fix

Every Python file has a hidden built-in variable called `__name__`. Its value depends on HOW the file is being used:

| How file is used | Value of `__name__` |
|---|---|
| Run directly (`python utils.py`) | `"__main__"` |
| Imported by another file (`import utils`) | `"utils"` |

So you can check it:

```python
# utils.py
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

if __name__ == "__main__":           # True only when this file is run DIRECTLY
    print(celsius_to_fahrenheit(100))  # Test code goes here
```

Now:
- `python utils.py` → prints `212.0` (we ARE running it directly)
- `import utils` from main.py → prints nothing (we're being imported, not run)

**Read the line as:** "If this file is the one being run directly, then do this stuff. If we're just being imported as a module, skip it."

You will use this pattern in every script you write going forward.

---

### 2.7 Building a Real Package — Hands On

Let's actually build a package so it stops being abstract. We're going to make `ai_toolkit/` — a tiny package with two modules — and use it from `main.py`.

#### Step 1 — Folder structure

```powershell
cd "C:\Users\smadavaram\OneDrive - Deloitte (O365D)\Desktop\AI-Engineering-Journey\week1\day2"
mkdir package_practice
cd package_practice
mkdir ai_toolkit
code .
```

#### Step 2 — Create `__init__.py` (the marker)

Inside `ai_toolkit/`, create an empty file called `__init__.py`. Just an empty file. Its mere existence is what tells Python "this folder is a package, not just a folder."

```python
# ai_toolkit/__init__.py
# (intentionally empty — this file just marks the folder as a package)
```

#### Step 3 — First module: `text_helpers.py`

Inside `ai_toolkit/`, create `text_helpers.py`:

```python
# ai_toolkit/text_helpers.py
"""Text processing helpers — the kind of things you do constantly with LLM inputs/outputs."""


def clean_prompt(text: str) -> str:
    """Strip whitespace and collapse internal newlines so prompts are consistent."""
    return " ".join(text.split())


def truncate(text: str, max_chars: int = 500) -> str:
    """Cut text down to max_chars (useful before sending to a token-limited API)."""
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "..."


def count_words(text: str) -> int:
    """Quick rough word count — handy for guessing token usage."""
    return len(text.split())
```

#### Step 4 — Second module: `api_helpers.py`

Inside `ai_toolkit/`, create `api_helpers.py`:

```python
# ai_toolkit/api_helpers.py
"""Helpers for working with API responses (mocked here — real API calls come Day 9)."""


def extract_text_from_response(response: dict) -> str:
    """
    Pull the assistant text out of a Claude-style API response.
    Real Claude responses look like:
    {
        "content": [{"type": "text", "text": "Hello!"}],
        "usage": {"input_tokens": 10, "output_tokens": 5}
    }
    """
    return response["content"][0]["text"]


def get_token_usage(response: dict) -> dict:
    """Return input + output token counts from a response."""
    usage = response.get("usage", {})
    return {
        "input": usage.get("input_tokens", 0),
        "output": usage.get("output_tokens", 0),
        "total": usage.get("input_tokens", 0) + usage.get("output_tokens", 0),
    }
```

#### Step 5 — Use the package from `main.py`

Outside `ai_toolkit/` (one level up), create `main.py`:

```python
# main.py
"""Demonstrates importing from a package."""

# Three different import styles — all valid:
from ai_toolkit import text_helpers
from ai_toolkit.api_helpers import extract_text_from_response, get_token_usage
from ai_toolkit import text_helpers as txt


def main():
    # --- Use the text helpers ---
    messy_prompt = "   Summarize    this   article \n\n  about AI engineering   "
    cleaned = text_helpers.clean_prompt(messy_prompt)
    print(f"Cleaned: '{cleaned}'")
    print(f"Word count: {txt.count_words(cleaned)}")

    # --- Use the api helpers (with a fake response) ---
    fake_response = {
        "content": [{"type": "text", "text": "AI engineering is the practice of..."}],
        "usage": {"input_tokens": 12, "output_tokens": 47},
    }

    text = extract_text_from_response(fake_response)
    usage = get_token_usage(fake_response)

    print(f"\nClaude said: {text}")
    print(f"Tokens used: {usage}")


if __name__ == "__main__":
    main()
```

#### Step 6 — Final structure & run

```
package_practice/
├── main.py
└── ai_toolkit/                  ← the package
    ├── __init__.py              ← empty, but REQUIRED
    ├── text_helpers.py          ← module
    └── api_helpers.py           ← module
```

Run it:

```powershell
python main.py
```

**You just built a Python package.** This same structure scales to apps with 100 modules.

#### What to notice

```python
from ai_toolkit.api_helpers import extract_text_from_response
     │           │             │
     │           │             └── the function inside the module
     │           └─────────────────── the module (a .py file)
     └─────────────────────────────── the package (a folder with __init__.py)
```

Read it as: "From the *ai_toolkit* package, find the *api_helpers* module, and bring me the *extract_text_from_response* function."

This is the exact pattern you'll write when you start using real AI libraries:

```python
from anthropic import Anthropic
     │            │
     │            └── a class inside the anthropic package
     └─────────────── the anthropic package (installed via pip)
```

You're not learning a special syntax for AI libraries. You're learning *the* syntax. AI libraries just happen to be packages someone else built.

---

## Part 3 — How `import` Actually Works

### 3.1 The One Big Idea

When you write `import utils` or `import pandas` or `import math`:

> Python has a list of folders. It walks the list, top to bottom, asking each folder: "Do you have a file or folder called `utils`?" The first one that says yes wins. Python loads that file. Done.

**That list of folders is called `sys.path`.** Once you internalize that, every "weird import error" you ever hit becomes solvable, because you know exactly what to check: *what folders is Python looking in, and where is the thing I'm trying to import?*

---

### 3.2 Investigation: What `sys.path` Looks Like

Run this in PowerShell:

```powershell
python -c "import sys; [print(i, ':', p) for i, p in enumerate(sys.path)]"
```

You'll see something like:

```
0 : C:\Users\smadavaram\OneDrive - Deloitte (O365D)\Desktop\AI-Engineering-Journey
1 : C:\Users\smadavaram\AppData\Local\Programs\Python\Python312\python312.zip
2 : C:\Users\smadavaram\AppData\Local\Programs\Python\Python312\Lib
3 : C:\Users\smadavaram\AppData\Local\Programs\Python\Python312\DLLs
4 : C:\Users\smadavaram\AppData\Local\Programs\Python\Python312
5 : C:\Users\smadavaram\AppData\Local\Programs\Python\Python312\Lib\site-packages
```

**That's it. `sys.path` is just a list of strings, where each string is a folder path on disk.** Six entries. When Python wants to find `requests` or `math` or `utils`, it walks down this exact list.

What each folder is for:

| # | Folder | What's there |
|---|---|---|
| 0 | (script's folder) | Files in the same folder as the script you're running |
| 1 | `python312.zip` | Compressed standard library (rarely used) |
| 2 | `Python312\Lib` | The standard library — `json`, `os`, `random`, etc. |
| 3 | `Python312\DLLs` | C-compiled standard library bits |
| 4 | `Python312` | Python's install root |
| 5 | `Python312\Lib\site-packages` | **Where pip installs things** |

> 💡 **Key insight:** sys.path is **just data**. You can print it, modify it at runtime, add folders to it. There's no magic anywhere.

---

### 3.3 Investigation: Look Inside the Standard Library

If `Python312\Lib` is where the standard library lives, that means **`json`, `random`, `os` are real files I should be able to see**.

```powershell
ls "C:\Users\smadavaram\AppData\Local\Programs\Python\Python312\Lib"
```

You'll see hundreds of files like:

```
__future__.py
abc.py
argparse.py
asyncio              ← a folder! json/asyncio are packages
base64.py
calendar.py
json                 ← a folder! json is a package
os.py                ← single file. os is a module.
random.py            ← single file. random is a module.
```

`random.py` is sitting right there as a regular Python file. You can open and read it:

```powershell
notepad "C:\Users\smadavaram\AppData\Local\Programs\Python\Python312\Lib\random.py"
```

That's the actual source code of the `random` module. The same file Python loads when you write `import random`.

#### Drilling into `json` (a folder)

```powershell
ls "C:\Users\smadavaram\AppData\Local\Programs\Python\Python312\Lib\json"
```

```
__init__.py          ← the file that makes the folder a "package"
decoder.py
encoder.py
scanner.py
tool.py
```

When you write `import json`, you're really loading `__init__.py`. That's why a folder needs `__init__.py` to be a package.

> 💡 `math` is special — it's written in C and compiled into Python's binary itself for speed. ~99% of modules are normal `.py` files like `random.py`.

---

### 3.4 Investigation: `__file__` Reveals Everything

Every Python module has a hidden attribute called `__file__` that tells you the exact path it was loaded from. **This is your most powerful debugging tool.**

```python
import json, os, random
print('json came from:', json.__file__)
print('os came from:', os.__file__)
print('random came from:', random.__file__)
```

Output:

```
json came from:     C:\...\Python312\Lib\json\__init__.py
os came from:       C:\...\Python312\Lib\os.py
random came from:   C:\...\Python312\Lib\random.py
```

After you `pip install requests`:

```python
import requests
print(requests.__file__)
# C:\...\Python312\Lib\site-packages\requests\__init__.py
```

> 🔧 **Whenever a module is misbehaving** — wrong version, weird errors — `print(modulename.__file__)` is the first thing you do. It tells you which copy on disk you're actually using.

---

### 3.5 Investigation: Watch Import Succeed

Set up two files in a folder.

**`utils.py`:**
```python
def greet(name):
    return f"Hello from utils.py, {name}!"

print("(utils.py is being loaded right now)")
```

**`main.py`:**
```python
import sys

print("=== Where is Python looking? ===")
for i, folder in enumerate(sys.path):
    print(f"  {i}: {folder if folder else '(this is the script folder)'}")

print()
print("=== Now I will: import utils ===")
import utils

print()
print(utils.greet("Smadavaram"))
print(f"  utils came from: {utils.__file__}")
```

When you run `python main.py`:

```
=== Where is Python looking? ===
  0: C:\...\my_folder       ← script folder, AUTOMATICALLY added by Python
  1: C:\...\Python312\python312.zip
  2: C:\...\Python312\Lib
  ...

=== Now I will: import utils ===
(utils.py is being loaded right now)        ← print() inside utils.py firing!

Hello from utils.py, Smadavaram!
  utils came from: C:\...\my_folder\utils.py
```

#### What to notice

1. **Folder #0 is the folder of the script being run** — Python automatically puts it first.
2. When `import utils` ran, Python walked the list, found `utils.py` in folder #0, and loaded it.
3. **The `print()` at the bottom of utils.py fired during the import** — proving "import" really means "execute this file top to bottom."
4. **`utils.__file__`** confirms the location.

---

### 3.6 Investigation: Watch Import Fail

Move `utils.py` somewhere else (or delete it) and run main.py again:

```
=== Now I will: import utils ===
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    import utils
ModuleNotFoundError: No module named 'utils'
```

What just happened, narrated:

```
Python: "OK, looking for 'utils'..."
        Folder 0: C:\...\my_folder         → utils here? No.
        Folder 1: ...python312.zip          → utils here? No.
        Folder 2: ...Lib                    → utils here? No.
        Folder 3: ...DLLs                   → utils here? No.
        Folder 4: ...Python312              → utils here? No.
        Folder 5: ...site-packages          → utils here? No.
        
        "Out of folders. ModuleNotFoundError."
```

> 🎯 **This is THE most common Python error for beginners**, and now you know exactly what causes it: the file you're trying to import is not in any folder listed in `sys.path`. The fix is always one of: (a) put the file in the right place, (b) cd to the right folder, or (c) add the folder to `sys.path` (next section).

---

### 3.7 Diagnostic Checklist for Import Errors

When something import-related breaks, walk these four steps:

```
1. Where is the file I'm trying to import?
       → Find utils.py / pandas / whatever on disk.

2. What folders is Python actually searching?
       → python -c "import sys; print(sys.path)"

3. Is the file's folder in that list?
       → If not: that's the problem.

4. If the import succeeded but is wrong:
       → python -c "import X; print(X.__file__)"
       → Tells you exactly which copy got loaded.
```

Every "weird" import problem is one of these four diagnoses. You don't need to memorize fancy fixes. You just need this checklist.

---

## Part 4 — PyPI and pip

### 4.1 What PyPI Is

**PyPI** = **Py**thon **P**ackage **I**ndex. Pronounced "pie-pee-eye."

It's a **global, public website** at [pypi.org](https://pypi.org) where developers (and companies) upload Python packages. Anyone in the world can then install those packages with `pip install`.

When you ran:

```bash
pip install pandas
```

Here's what *physically* happened:

```
Your computer                         PyPI servers (pypi.org)
─────────────                         ───────────────────────
                                      Hosts 500,000+ packages

   pip install pandas
        │
        ├──"Hey, do you have 'pandas'?"──────────►
        │                                          
        │◄──"Yes, version 2.2.3, here's the URL"──
        │
        ├──"GET https://files.pythonhosted.org/.../pandas-2.2.3.tar.gz"──►
        │                                          
        │◄────────── [file bytes streaming] ──────
        │
        Saves to: C:\...\Python312\Lib\site-packages\pandas\
        │
        Now `import pandas` works ✅
```

### What's on PyPI

Almost every Python tool you'll ever use:

| Package | What It Does | When You'll Use It |
|---|---|---|
| `anthropic` | Official Claude SDK | Day 9 onwards — every AI app |
| `openai` | Official OpenAI SDK | If you compare LLMs |
| `langchain` | Framework for building AI apps | Week 3 |
| `pandas` | Tables / data manipulation | Day 7 |
| `numpy` | Math, arrays, ML foundations | Day 7+ |
| `requests` | Make HTTP calls | Day 6 |
| `fastapi` | Build web APIs | Week 4 |
| `python-dotenv` | Load API keys from `.env` files | Day 6 |
| `streamlit` | Build quick web UIs | Week 4 |

Every single one of these lives on PyPI. Every one is a package someone else wrote and published. Every one you can read the source code of, contribute to, or fork.

---

### 4.2 Useful pip Commands

```bash
pip install pandas              # Install latest version
pip install pandas==2.2.3       # Install specific version
pip install --upgrade pandas    # Update to latest

pip uninstall pandas            # Remove a package

pip list                        # All installed packages
pip show pandas                 # Details about an installed package
pip freeze                      # All packages with exact versions
pip freeze > requirements.txt   # Save list to file (for sharing!)

pip install -r requirements.txt # Install everything from a list
```

> 💡 **`requirements.txt` is the standard way to share Python project dependencies.** When you clone someone's repo, you'll see this file — run `pip install -r requirements.txt` to get every library they used.

---

### 4.3 The Connection: PyPI → site-packages → import

```
You ran:                 pip install requests

Pip did:                 1. Asked PyPI: "got requests?"
                         2. Downloaded the .tar.gz file
                         3. Unpacked it into:
                            C:\...\Python312\Lib\site-packages\requests\

Now when you write:      import requests

Python does:             1. Walks sys.path looking for "requests"
                         2. Finds site-packages\requests\ (folder with __init__.py)
                         3. Loads __init__.py
                         4. Done.
```

**There is no internet call when you `import` something.** The internet call happened when you `pip install`ed it. Import is purely a local file lookup.

#### See it with your own eyes

After you `pip install requests`:

```powershell
ls "C:\Users\smadavaram\AppData\Local\Programs\Python\Python312\Lib\site-packages\requests"
```

You'll see all of `requests`'s `.py` files sitting there. **Real code, on your disk, that you can open.** The famous `requests` library used by millions is just a folder of `.py` files. Same as the `ai_toolkit/` you built in 2.7.

---

## Part 5 — Environment Variables and PYTHONPATH

### 5.1 The Connection to Day 1

**Day 1 problem:** "I type `python` and Windows says 'not found'." → Fix: add Python's folder to **PATH**.

**Day 2 problem:** "I type `import claude_helpers` and Python says 'No module named'." → Fix: add the folder containing `claude_helpers.py` to **PYTHONPATH** (or to `sys.path`).

| Variable | Used by | What it controls |
|---|---|---|
| **PATH** | Windows / your shell | "Where do I find programs to run? (`.exe` files)" |
| **PYTHONPATH** | Python (only) | "Where do I find modules to import? (`.py` files)" |

They're both environment variables. They both live in the same Windows Settings window. They're set the same way. The only difference is **who reads them and what they're searching for**.

---

### 5.2 What Environment Variables Actually Are

Environment variables aren't a Python thing or a Windows-special thing. They're a feature of every operating system. They're **just key-value pairs that the OS holds in memory and gives to every program when it starts.**

Real example output:

```
PATH=C:\Windows\System32;C:\...\Python312;...
PYTHONPATH=C:\Users\smadavaram\shared_python_code
HOME=C:\Users\smadavaram
ANTHROPIC_API_KEY=sk-ant-...
```

`KEY=VALUE`. That's the entire data model — a flat list of named strings.

When you start any program (Python, Word, Chrome), the OS hands it a copy of this whole list. The program can read any value by name.

#### How Python reads them

```python
import os

print(os.environ.get('HOME'))             # C:\Users\smadavaram
print(os.environ.get('PATH')[:60])        # C:\Windows\System32;...
print(os.environ.get('PYTHONPATH', 'NOT SET'))   # NOT SET if you haven't set it
```

`os.environ` is a dict-like object Python builds automatically at startup by reading whatever the OS handed it. **It is literally a dictionary of the environment variables.**

> 🎯 **For AI engineering, this is THE pattern for API keys:**
> ```python
> api_key = os.environ.get("ANTHROPIC_API_KEY")
> ```
> Your code doesn't contain the secret. The OS holds it. Anyone reading your code on GitHub sees the variable name, not the actual key.

---

### 5.3 What `PYTHONPATH` Specifically Does

Recall from Part 3: when you write `import X`, Python walks down `sys.path` looking for X. So who decides what's in `sys.path`?

**Python builds `sys.path` automatically when it starts.** The recipe:

```
sys.path = (the folder of the script being run)
         + (folders listed in the PYTHONPATH env var, if it's set)
         + (standard library folders)
         + (site-packages folders)
```

So **`PYTHONPATH` is your way to permanently inject extra folders into Python's search list, before Python even starts running your code.** Once set, every Python script you ever run on that machine picks it up.

#### The 3 levels of "set this variable" — same as Day 1's PATH

| Method | Lifetime | Use When |
|---|---|---|
| `$env:PYTHONPATH = "..."` (PowerShell) | This shell session only | Quick test |
| Windows Settings GUI → Environment Variables | Forever | "I want this folder available in every project, every time" |
| `[Environment]::SetEnvironmentVariable(...)` | Forever | Same as GUI, but via command |

---

### 5.4 Setting PYTHONPATH Permanently — GUI Method

#### Step 1 — Find the exact path of your shared folder

In PowerShell:

```powershell
cd "C:\Users\smadavaram\OneDrive - Deloitte (O365D)\Desktop\AI-Engineering-Journey\week1\day2\my_shared_code"
pwd
```

Copy the path that prints.

#### Step 2 — Open the Environment Variables window

Same window from Day 1:

```
Press Windows key → type "environment variables"
→ Click "Edit the system environment variables"
→ Click "Environment Variables..." button
```

You'll see this window:

```
┌──────────────────────────────────────────────────────────┐
│  Environment Variables                                   │
│                                                          │
│  ┌─ User variables for smadavaram ─────────────────────┐ │
│  │  Variable           Value                           │ │
│  │  Path               C:\...\Python312;C:\...\Scripts │ │  ← Day 1 lives here
│  │  TEMP               C:\Users\...\Temp               │ │
│  │  ...                                                │ │
│  │            [New...]  [Edit...]  [Delete]            │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌─ System variables ──────────────────────────────────┐ │
│  │  ...                                                │ │
│  └─────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

#### Step 3 — Add PYTHONPATH

In **User variables for smadavaram** (top section):

1. Click **New...**
2. **Variable name:** `PYTHONPATH`
3. **Variable value:** paste the path (no quotes!)
4. Click **OK** → **OK** → **OK**

#### Step 4 — Close ALL PowerShell windows and open a fresh one

> ⚠️ **This is critical.** PowerShell only reads env vars when it starts. Your existing shells still have the old (empty) PYTHONPATH frozen in memory. This includes PowerShell tabs inside VS Code — close VS Code entirely.

#### Step 5 — Verify

```powershell
$env:PYTHONPATH
```

Should print your path.

```powershell
python -c "import os; print(os.environ.get('PYTHONPATH'))"
```

Same output.

```powershell
python -c "import sys; [print(p) for p in sys.path]"
```

You'll see your folder appear in the list. Now `import` works without setting anything in this shell.

---

### 5.5 Setting PYTHONPATH Permanently — PowerShell Method

If you prefer not to click through the GUI:

```powershell
[Environment]::SetEnvironmentVariable(
    "PYTHONPATH",
    "C:\Users\smadavaram\OneDrive - Deloitte (O365D)\Desktop\AI-Engineering-Journey\week1\day2\my_shared_code",
    [EnvironmentVariableTarget]::User
)
```

What each piece means:
- `"PYTHONPATH"` — the variable we're creating/setting
- `"C:\..."` — its value (the folder)
- `[EnvironmentVariableTarget]::User` — save to User variables (the top section of the GUI)

Then close and reopen PowerShell. Verify with `$env:PYTHONPATH`.

#### Adding multiple folders

Just like PATH, separate multiple folders with `;` on Windows:

```
PYTHONPATH = C:\folder1;C:\folder2;C:\folder3
```

In PowerShell, append without overwriting:

```powershell
$existing = [Environment]::GetEnvironmentVariable("PYTHONPATH", "User")
$new = if ($existing) { "$existing;C:\new\folder" } else { "C:\new\folder" }
[Environment]::SetEnvironmentVariable("PYTHONPATH", $new, "User")
```

---

### 5.6 Diagnostic — When `$env:PYTHONPATH` is Empty

If after restarting PowerShell `$env:PYTHONPATH` is still empty, run this to bypass your shell and ask Windows directly:

```powershell
[Environment]::GetEnvironmentVariable("PYTHONPATH", "User")
```

Three possibilities:

#### Scenario A — It prints your path

**Diagnosis:** Windows saved it correctly, but your PowerShell session is stale.

**Fix:** Close **every single** PowerShell window — including:
- PowerShell tabs inside VS Code (the integrated terminal)
- Any standalone PowerShell windows
- VS Code itself if you're using its terminal

Then open a fresh PowerShell from the Start menu. Run `$env:PYTHONPATH` again.

#### Scenario B — It prints nothing

**Diagnosis:** Windows didn't actually save it.

**Fix:** Set it from PowerShell directly:

```powershell
[Environment]::SetEnvironmentVariable("PYTHONPATH", "C:\path\to\your\folder", "User")
```

Verify it saved:

```powershell
[Environment]::GetEnvironmentVariable("PYTHONPATH", "User")
```

Then close and open fresh PowerShell.

#### Scenario C — Quick path to "just make it work right now"

If you want to verify the concept works **immediately** without restarting:

```powershell
$env:PYTHONPATH = "C:\path\to\your\folder"
$env:PYTHONPATH    # Should print your path
python main.py     # Should now work
```

This proves the concept end-to-end. Once it works, do the permanent setup above.

---

### 5.7 The AI Engineering Payoff: API Keys

This is why all of this matters for AI work. **API keys for Claude, OpenAI, etc. should NEVER be hard-coded in your scripts.** They go in environment variables, exactly like the ones you just learned to set.

#### Set the key permanently

Same procedure as PYTHONPATH:

1. Windows key → "environment variables" → Edit the system environment variables
2. Environment Variables button
3. Under User variables, click **New...**
4. **Variable name:** `ANTHROPIC_API_KEY`
5. **Variable value:** your key (e.g., `sk-ant-...`)
6. OK → OK → OK
7. Close and reopen PowerShell

#### Read it from Python

```python
import os
api_key = os.environ.get("ANTHROPIC_API_KEY")

if api_key:
    print(f"✅ Key found.")
else:
    print("❌ No key found.")
```

#### The Day 9 preview

When you `pip install anthropic` and write your first Claude call, the SDK does **literally this** under the hood:

```python
self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
```

Translation: "Did you pass an api_key argument? Use it. Otherwise, read it from the env var ANTHROPIC_API_KEY."

So once you set `ANTHROPIC_API_KEY` in Windows Settings, this code just works:

```python
from anthropic import Anthropic

client = Anthropic()    # No key in source code! Reads from env var.

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}]
)
```

#### Why this is non-negotiable

Three reasons every AI engineer treats env-var API keys as gospel:

1. **Source control safety.** If you accidentally `git push` code with a hardcoded key, anyone on GitHub can use it (and rack up your bill). Env vars stay on your machine.
2. **Different keys per environment.** Dev key on your laptop, prod key on the server, neither in code. Same script, different env, different keys.
3. **Easy rotation.** Key gets leaked? Update the env var, restart. No code change.

When you actually start using Claude on Day 9, **the very first thing you'll do is set `ANTHROPIC_API_KEY` in Windows Settings** using the exact procedure above.

---

### 5.8 The Full Picture

Here's the complete flow from "Windows Settings window" to "your code runs," all in one diagram:

```
┌─────────────────────────────────────────────────────────────────┐
│  Windows Settings → Environment Variables                       │
│                                                                 │
│   PATH       = C:\...\Python312;C:\...\Scripts;...              │
│   PYTHONPATH = C:\Users\smadavaram\shared_python_code           │
│   ANTHROPIC_API_KEY = sk-ant-...                                │
└────────────────────────┬────────────────────────────────────────┘
                         │ (PowerShell starts up, reads these)
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  PowerShell session has these env vars in memory                │
└────────────────────────┬────────────────────────────────────────┘
                         │ (You type: python my_script.py)
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  PATH search → finds python.exe → starts Python                 │
└────────────────────────┬────────────────────────────────────────┘
                         │ (Python starts, builds os.environ + sys.path)
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Python's running:                                              │
│   - os.environ["ANTHROPIC_API_KEY"] = "sk-ant-..."  ← key       │
│   - sys.path = [script folder,                                  │
│                 PYTHONPATH folders,                             │
│                 stdlib,                                         │
│                 site-packages]                                  │
└────────────────────────┬────────────────────────────────────────┘
                         │ (Your code: import claude_helpers)
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│  Walks sys.path → finds claude_helpers.py → loads it ✅         │
└─────────────────────────────────────────────────────────────────┘
```

Three different env vars, three different jobs, **all set in the same place**:

| Env var | Used by | What it lets find |
|---|---|---|
| `PATH` | Windows | `python.exe`, `git.exe`, `pip.exe` |
| `PYTHONPATH` | Python interpreter | `your_module.py` files (added to `sys.path`) |
| `ANTHROPIC_API_KEY` | Your code (via `os.environ`) | The Claude API secret |

---

## Part 6 — The Day 2 Experiment

Build `utils.py` (your toolbox) and `main.py` (the program that uses it).

### Setup

```powershell
cd "C:\Users\smadavaram\OneDrive - Deloitte (O365D)\Desktop\AI-Engineering-Journey"
mkdir week1\day2
cd week1\day2
code .
```

VS Code opens. Create two files: `utils.py` and `main.py`.

### `utils.py`

```python
"""
utils.py — A small toolbox of reusable helper functions.
Day 2 of the AI Engineering Journey.
"""


def celsius_to_fahrenheit(temp: float) -> float:
    """
    Convert a temperature from Celsius to Fahrenheit.

    Formula: F = (C × 9/5) + 32

    Args:
        temp (float): Temperature in Celsius

    Returns:
        float: Temperature in Fahrenheit
    """
    return (temp * 9 / 5) + 32


def is_palindrome(text: str) -> bool:
    """
    Check whether a string reads the same forwards and backwards.
    Ignores case and spaces, so 'Race car' is considered a palindrome.

    Args:
        text (str): The text to check

    Returns:
        bool: True if palindrome, False otherwise
    """
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]    # [::-1] reverses a string


def count_vowels(text: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in a string.
    Case-insensitive.

    Args:
        text (str): The text to scan

    Returns:
        int: The number of vowels found
    """
    vowels = "aeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count


# ---- Quick self-tests — only run when this file is executed directly ----
if __name__ == "__main__":
    print("Running utils.py self-tests...")
    print(f"100°C in Fahrenheit: {celsius_to_fahrenheit(100)}")
    print(f"Is 'madam' a palindrome? {is_palindrome('madam')}")
    print(f"Vowels in 'Smadavaram': {count_vowels('Smadavaram')}")
    print("All tests done.")
```

### `main.py`

```python
"""
main.py — Demonstrates importing and using functions from utils.py
"""

# Three different import styles — pick one in real code; here all shown for learning:
import utils                                          # Style 1: whole module
from utils import is_palindrome                       # Style 2: specific function
from utils import count_vowels as vowel_count         # Style 3: with an alias


def main():
    """Run a small demo using each helper from utils."""

    print("=" * 50)
    print("  AI Engineering Journey — Day 2 Demo")
    print("=" * 50)

    # --- Temperature converter ---
    print("\n[Temperature Converter]")
    celsius_input = float(input("Enter a temperature in Celsius: "))
    fahrenheit = utils.celsius_to_fahrenheit(celsius_input)
    print(f"  {celsius_input}°C = {fahrenheit:.2f}°F")

    # --- Palindrome checker ---
    print("\n[Palindrome Checker]")
    word = input("Enter a word or phrase: ")
    if is_palindrome(word):
        print(f"  ✅ '{word}' is a palindrome!")
    else:
        print(f"  ❌ '{word}' is NOT a palindrome.")

    # --- Vowel counter ---
    print("\n[Vowel Counter]")
    sentence = input("Enter a sentence: ")
    n = vowel_count(sentence)
    print(f"  '{sentence}' contains {n} vowels.")

    print("\n" + "=" * 50)
    print("  Demo complete.")
    print("=" * 50)


if __name__ == "__main__":
    main()
```

### Run It

```powershell
python main.py
```

### What's Happening — Step by Step

```
You run: python main.py
    │
    ▼
1. Python opens main.py and starts reading from line 1
    │
    ▼
2. Hits "import utils" → opens utils.py, runs it top-to-bottom
   - Reads function definitions (memorizes them, doesn't run them)
   - Hits the bottom: "if __name__ == '__main__':"
   - But __name__ is "utils" right now (we're being imported), so it SKIPS that block
   - Comes back to main.py
    │
    ▼
3. Hits "from utils import is_palindrome" → already loaded, exposes the name directly
    │
    ▼
4. Hits "from utils import count_vowels as vowel_count" → exposes under a new local name
    │
    ▼
5. Reads the "def main():" block → memorizes the function, doesn't run it
    │
    ▼
6. Hits "if __name__ == '__main__':" → __name__ IS "__main__" now
   So it runs main()
    │
    ▼
7. main() runs, asks for input, calls each helper, prints results
    │
    ▼
8. Program ends
```

This mental model — Python reading top to bottom, treating `def` as "memorize this," running everything else immediately — will save you from countless confused moments.

### Bonus Challenges

Add these to `utils.py`:

```python
# 1. Reverse a string (use the same [::-1] trick)
def reverse_string(text: str) -> str:
    ...

# 2. Convert Fahrenheit back to Celsius — the inverse function
def fahrenheit_to_celsius(temp: float) -> float:
    ...

# 3. Count consonants (everything that's a letter but NOT a vowel)
def count_consonants(text: str) -> int:
    ...

# 4. Use *args — sum any number of temperatures and return the average in Fahrenheit
def average_temp_in_fahrenheit(*celsius_temps: float) -> float:
    ...

# 5. Use **kwargs — build a profile string from any keyword arguments passed in
def build_profile(**details) -> str:
    """e.g., build_profile(name='S', age=25) → 'name: S | age: 25'"""
    ...
```

### Push It

```bash
git add .
git commit -m "Day 2: Functions, modules, utils.py + main.py"
git push
```

---

## Cheat Sheets

### Functions

```python
def function_name(param1, param2="default"):
    """Docstring."""
    return result

# Calling:
function_name(value1)                     # Positional
function_name(param1=value1)              # Keyword
function_name(value1, param2="custom")    # Mixed

# Variable arguments:
def f(*args):     # tuple of extra positional
    ...
def f(**kwargs):  # dict of extra keyword
    ...
def f(a, b="x", *args, **kwargs):  # full pattern (memorize order)
    ...

# Type hints:
def add(a: int, b: int) -> int:
    return a + b

# Lambda:
square = lambda x: x ** 2
```

### Map, Lambda, Sort

```python
# lambda — anonymous tiny function:
double = lambda x: x * 2

# map — apply function to every item:
list(map(lambda x: x.upper(), ["a", "b", "c"]))   # ['A', 'B', 'C']

# Equivalent comprehension (preferred):
[x.upper() for x in ["a", "b", "c"]]              # ['A', 'B', 'C']

# sort with key:
items.sort(key=lambda i: i["score"])              # ascending
items.sort(key=lambda i: i["score"], reverse=True) # descending
items.sort(key=lambda i: (i["category"], i["price"]))  # multi-key
```

### Modules & Imports

```python
import math                       # whole module
import pandas as pd                # alias
from math import sqrt, pi          # specific items

# Built-in modules to know:
import math, random, datetime, json, os

# The main guard (in EVERY script):
if __name__ == "__main__":
    main()
```

### Diagnostics

```python
# Where Python looks for modules:
import sys
for p in sys.path: print(p)

# Where a module came from:
import some_module
print(some_module.__file__)

# Read environment variables:
import os
os.environ.get("ANTHROPIC_API_KEY")
```

### pip

```bash
pip install <package>
pip install <package>==<version>
pip install --upgrade <package>
pip uninstall <package>
pip list
pip show <package>
pip freeze > requirements.txt
pip install -r requirements.txt
```

### PowerShell — Environment Variables

```powershell
# Read
$env:PATH
$env:PYTHONPATH
$env:ANTHROPIC_API_KEY
Get-ChildItem env:                 # ALL env vars

# Set temporarily (this shell only)
$env:PYTHONPATH = "C:\path\here"

# Set permanently
[Environment]::SetEnvironmentVariable("PYTHONPATH", "C:\path", "User")

# Verify Windows saved it (bypasses your shell)
[Environment]::GetEnvironmentVariable("PYTHONPATH", "User")

# Verify Python sees it
python -c "import os; print(os.environ.get('PYTHONPATH'))"
python -c "import sys; [print(p) for p in sys.path]"
```

### Diagnostic Checklist for Import Errors

```
1. Where is the file I'm trying to import?    → Find it on disk.
2. What folders is Python actually searching? → python -c "import sys; print(sys.path)"
3. Is the file's folder in that list?         → If not, that's the problem.
4. If it loaded the wrong copy:               → python -c "import X; print(X.__file__)"
```

---

## Looking Ahead

**Today you learned:** How to package logic (functions) and how to package files (modules).

**Tomorrow (Day 3):** Data structures deep dive — slicing, comprehensions, nested data, JSON parsing. You'll start manipulating the kind of data structures that come back from Claude API responses.

**Connection to AI engineering:** Every API call you'll write is a function. Every API response is a dict. Every helper you write is a module. The patterns you practiced today — `def`, `return`, `import`, `if __name__ == "__main__":`, `os.environ.get()` — are in literally every Python file in every AI codebase on Earth.

The unbroken chain:

- **Day 1** → You set up Python so the `import` system works.
- **Day 2** → You learned to write functions (= Actions = Tools), package them into modules, and stack modules into packages.
- **Day 6** → You'll `pip install anthropic`. PyPI sends a package. Python drops it in `site-packages/`. `import anthropic` finds it on `sys.path`.
- **Day 9** → You'll define a function `def get_weather(city)`, give it a docstring, and register it as a Tool with Claude. Same syntax you wrote today.
- **Week 3** → You'll have your own multi-module package — exactly like the `ai_toolkit/` we built — but with real Claude calls inside.

Nothing you learned today gets thrown away. Every line is foundation.

### The Habits That Will Pay Off Forever

1. **Every reusable thing becomes a function.** No copy-paste.
2. **Every function gets a docstring.** Future-you and Claude-as-coworker both read them.
3. **Every function gets type hints.** Prevents the silent bugs.
4. **Every script has `if __name__ == "__main__":`.** Now imports are safe.
5. **Mutable defaults? Never. Use `None`.** Forever rule.
6. **API keys NEVER in code. Always in env vars.** Forever rule.
7. **When in doubt about where a module lives:** `import X; print(X.__file__)`. Done.

---

> **Note to future me:** If you're reading this after a long break, you don't need to start over. The cheat sheets at the end are your quick reference. Functions are Actions, modules are .py files, packages are folders, sys.path is just a list, env vars are key-value pairs. Five sentences. The whole day in five sentences.

> **Note to future me, part 2:** When something import-related breaks, your first move is `python -c "import sys; print(sys.path)"`. When something env-var related breaks, your first move is `python -c "import os; print(os.environ.get('VAR_NAME'))"`. Most "magic" problems disappear once you can see what Python actually sees.




## Day 3 — Data Structures Quick-Reference Cheat Sheet

> Built for fast scanning. When you forget "how do I delete a key from a dict again?" — Ctrl+F here.

---

### Pick the Right Structure

| Need | Use | Why |
|---|---|---|
| Order matters, will change | **list** `[]` | Indexed, mutable |
| Key → value lookup | **dict** `{}` | Fast lookup by name |
| Unique items only / membership tests | **set** `{}` | Auto-dedupe, instant `in` checks |
| Fixed group of values, won't change | **tuple** `()` | Immutable, hashable, lightweight |

---

### 📋 LIST — Ordered, Mutable, Allows Duplicates

```python
items = ["a", "b", "c", "d"]
```

#### Create
| Operation | Syntax | Example |
|---|---|---|
| Empty list | `items = []` | `items = []` |
| With values | `items = [v1, v2, ...]` | `items = ["a", "b", "c"]` |
| From range | `items = list(range(5))` | `[0, 1, 2, 3, 4]` |
| From string | `items = list("abc")` | `["a", "b", "c"]` |
| Repeat values | `items = [0] * 5` | `[0, 0, 0, 0, 0]` |

#### Access
| Operation | Syntax | Example | Returns |
|---|---|---|---|
| First item | `items[0]` | `items[0]` | `"a"` |
| Last item | `items[-1]` | `items[-1]` | `"d"` |
| Slice | `items[start:stop]` | `items[1:3]` | `["b", "c"]` |
| Reverse | `items[::-1]` | `items[::-1]` | `["d", "c", "b", "a"]` |
| Every Nth | `items[::N]` | `items[::2]` | `["a", "c"]` |
| Length | `len(items)` | `len(items)` | `4` |

#### Add
| Operation | Syntax | Example | Result |
|---|---|---|---|
| Add ONE to end | `items.append(x)` | `items.append("e")` | `["a","b","c","d","e"]` |
| Add MANY to end | `items.extend(other)` | `items.extend(["e","f"])` | `["a","b","c","d","e","f"]` |
| Insert at index | `items.insert(i, x)` | `items.insert(1, "X")` | `["a","X","b","c","d"]` |
| Concatenate | `items + other` | `items + ["e","f"]` | new list |

> ⚠️ `append([1,2])` adds the LIST as one item. Use `extend([1,2])` to merge.

#### Update
| Operation | Syntax | Example | Result |
|---|---|---|---|
| Replace by index | `items[i] = x` | `items[0] = "Z"` | `["Z","b","c","d"]` |
| Replace slice | `items[i:j] = list` | `items[1:3] = ["X","Y"]` | `["a","X","Y","d"]` |

#### Delete
| Operation | Syntax | Example | Notes |
|---|---|---|---|
| By value (first match) | `items.remove(x)` | `items.remove("b")` | Errors if missing |
| By index, return it | `items.pop(i)` | `items.pop(0)` | Default is last item |
| By index, no return | `del items[i]` | `del items[0]` | |
| Slice | `del items[i:j]` | `del items[1:3]` | |
| Empty the list | `items.clear()` | `items.clear()` | `[]` |

#### Search & Inspect
| Operation | Syntax | Example | Returns |
|---|---|---|---|
| Exists? | `x in items` | `"b" in items` | `True`/`False` |
| Find index | `items.index(x)` | `items.index("c")` | `2` (errors if missing) |
| Count occurrences | `items.count(x)` | `items.count("a")` | `1` |
| Min / Max | `min(items)` / `max(items)` | `max([3,1,4])` | `4` |
| Sum | `sum(items)` | `sum([1,2,3])` | `6` |

#### Sort & Reverse
| Operation | Syntax | Notes |
|---|---|---|
| Sort in place | `items.sort()` | Modifies original |
| Sort, return new | `sorted(items)` | Original unchanged |
| Sort descending | `sorted(items, reverse=True)` | |
| Sort by key | `sorted(items, key=lambda x: x["score"])` | Custom field |
| Reverse in place | `items.reverse()` | |

#### Copy
| Operation | Syntax | Notes |
|---|---|---|
| Shallow copy | `items.copy()` or `items[:]` | New list, same inner objects |
| Deep copy | `copy.deepcopy(items)` | `import copy` first |

---

### 📖 DICT — Key→Value, Mutable, Keys Must Be Unique

```python
person = {"name": "Ravi", "age": 25, "dept": "Eng"}
```

#### Create
| Operation | Syntax | Example |
|---|---|---|
| Empty dict | `d = {}` | |
| With values | `d = {"k": "v"}` | `{"name": "Ravi"}` |
| From pairs | `dict([(k,v), (k,v)])` | `dict([("a",1),("b",2)])` |
| From two lists | `dict(zip(keys, vals))` | `dict(zip(["a","b"],[1,2]))` |
| From keys, same value | `dict.fromkeys(keys, 0)` | `{"a":0,"b":0}` |

#### Access
| Operation | Syntax | Example | Returns |
|---|---|---|---|
| By key (strict) | `d[key]` | `person["name"]` | `"Ravi"` (errors if missing) |
| By key (safe) | `d.get(key)` | `person.get("salary")` | `None` if missing |
| By key, with default | `d.get(key, default)` | `person.get("salary", 0)` | `0` if missing |
| All keys | `d.keys()` | `person.keys()` | `dict_keys([...])` |
| All values | `d.values()` | `person.values()` | `dict_values([...])` |
| All pairs | `d.items()` | `person.items()` | `dict_items([(k,v)...])` |
| Length | `len(d)` | `len(person)` | `3` |

#### Add / Update
| Operation | Syntax | Example |
|---|---|---|
| Add or update key | `d[key] = value` | `person["salary"] = 800000` |
| Update many | `d.update(other_dict)` | `person.update({"age":26, "city":"NYC"})` |
| Add only if missing | `d.setdefault(key, default)` | `person.setdefault("city", "Unknown")` |
| Merge (Python 3.9+) | `d1 \| d2` | `defaults \| overrides` |
| Merge (any version) | `{**d1, **d2}` | `{**defaults, **overrides}` |

> 💡 `setdefault` is gold for grouping — `groups.setdefault(key, []).append(item)`.

#### Delete
| Operation | Syntax | Example | Notes |
|---|---|---|---|
| Remove key, return value | `d.pop(key)` | `person.pop("age")` | Errors if missing |
| Remove key, with default | `d.pop(key, None)` | `person.pop("foo", None)` | Safe |
| Remove key, no return | `del d[key]` | `del person["age"]` | Errors if missing |
| Remove last inserted | `d.popitem()` | | Returns `(key, value)` |
| Empty the dict | `d.clear()` | | `{}` |

#### Search
| Operation | Syntax | Example | Returns |
|---|---|---|---|
| Key exists? | `key in d` | `"name" in person` | `True` |
| Key missing? | `key not in d` | `"salary" not in person` | `True` |
| Value exists? | `value in d.values()` | `25 in person.values()` | `True` |

#### Iterate
| What you want | Syntax |
|---|---|
| Just keys | `for k in d:` or `for k in d.keys():` |
| Just values | `for v in d.values():` |
| Both (most common) | `for k, v in d.items():` |
| Filter while iterating | `{k: v for k, v in d.items() if v > 0}` |

---

### 🎯 SET — Unique, Unordered, Fast Membership Tests

```python
skills = {"Python", "SQL", "FastAPI"}
```

#### Create
| Operation | Syntax | Example |
|---|---|---|
| Empty set | `s = set()` | ⚠️ NOT `{}` (that's a dict!) |
| With values | `s = {v1, v2, ...}` | `{"a", "b", "c"}` |
| From list (dedupe) | `s = set(list)` | `set([1,1,2,3])` → `{1,2,3}` |
| From string | `s = set("hello")` | `{"h","e","l","o"}` |

#### Access
> Sets have **no indexing** — no `s[0]`. They're unordered.

| Operation | Syntax | Returns |
|---|---|---|
| Length | `len(s)` | int |
| Convert to list | `list(s)` | order not guaranteed |
| Iterate | `for x in s:` | order not guaranteed |

#### Add
| Operation | Syntax | Example |
|---|---|---|
| Add one | `s.add(x)` | `skills.add("Rust")` |
| Add many | `s.update(iterable)` | `skills.update(["Go", "Java"])` |

#### Delete
| Operation | Syntax | Behavior if missing |
|---|---|---|
| Remove (strict) | `s.remove(x)` | Raises `KeyError` |
| Remove (safe) | `s.discard(x)` | No error |
| Remove arbitrary | `s.pop()` | Returns removed item |
| Empty the set | `s.clear()` | |

> 💡 Use `.discard()` when you don't care if it's there, `.remove()` when you do.

#### Search
| Operation | Syntax | Example | Speed |
|---|---|---|---|
| Exists? | `x in s` | `"Python" in skills` | **O(1) — instant** |
| Not exists? | `x not in s` | | |

#### Set Operations (the whole point of sets)

| Operation | Operator | Method | Means |
|---|---|---|---|
| Union | `a \| b` | `a.union(b)` | Everything in either |
| Intersection | `a & b` | `a.intersection(b)` | In BOTH |
| Difference | `a - b` | `a.difference(b)` | In `a` but NOT `b` |
| Symmetric diff | `a ^ b` | `a.symmetric_difference(b)` | In one but not both |
| Subset? | `a <= b` | `a.issubset(b)` | All of `a` in `b`? |
| Superset? | `a >= b` | `a.issuperset(b)` | `a` contains all of `b`? |
| Disjoint? | — | `a.isdisjoint(b)` | No common items? |

**Visual:**
```
a = {1, 2, 3}    b = {3, 4, 5}

a | b → {1, 2, 3, 4, 5}    (union — everything)
a & b → {3}                (intersection — overlap)
a - b → {1, 2}             (difference — only in a)
a ^ b → {1, 2, 4, 5}       (symmetric — exclusive to each)
```

---

### 📦 TUPLE — Ordered, IMMUTABLE, Allows Duplicates

```python
point = (10, 20)
```

#### Create
| Operation | Syntax | Example |
|---|---|---|
| Empty tuple | `t = ()` | |
| With values | `t = (v1, v2, ...)` | `(1, 2, 3)` |
| Single value | `t = (v,)` | ⚠️ `(5)` is just `5`. Need the comma. |
| Without parens | `t = 1, 2, 3` | Same as `(1, 2, 3)` |
| From list | `t = tuple(list)` | `tuple([1,2,3])` |

#### Access
| Operation | Syntax | Example | Returns |
|---|---|---|---|
| By index | `t[i]` | `point[0]` | `10` |
| Slice | `t[i:j]` | `(1,2,3,4)[1:3]` | `(2, 3)` |
| Length | `len(t)` | | int |
| Unpack | `a, b = t` | `x, y = point` | `x=10, y=20` |
| Rest unpack | `first, *rest = t` | | |

#### Add / Update / Delete
> ❌ **You can't.** Tuples are immutable. Create a new tuple instead.

```python
# To "add" — create new tuple
new = old + (extra,)

# To "update" — convert, change, convert back
items = list(old)
items[0] = "X"
new = tuple(items)
```

#### Search
| Operation | Syntax | Returns |
|---|---|---|
| Exists? | `x in t` | bool |
| Find index | `t.index(x)` | int (errors if missing) |
| Count | `t.count(x)` | int |

#### Named Tuples (when you want clarity)
```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
p.x          # 10  (access by name)
p[0]         # 10  (still works by index)
```

---

### 🧠 Memory Tricks

| Trick | Remember |
|---|---|
| `[]` = list, `{}` = **dict**, `set()` = set, `()` = tuple | Empty `{}` is a dict, NOT a set! |
| `append` adds ONE, `extend` adds MANY | "extend" sounds bigger → handles multiple |
| `.remove(x)` works on **list** and **set** by VALUE | Both error if missing |
| `.pop()` works on list (index), dict (key), set (random) | Always returns the removed thing |
| `.get()` is dict's safe access | Lists don't have `.get()` |
| Set operations: \| & - ^ | Like math — union, intersect, subtract |
| Tuples can't change | Use them when data is FINAL |

---

### 🎯 Operations Comparison — One Glance

| Operation | List | Dict | Set | Tuple |
|---|---|---|---|---|
| Create empty | `[]` | `{}` | `set()` | `()` |
| Length | `len(x)` | `len(x)` | `len(x)` | `len(x)` |
| Membership | `v in list` | `key in dict` | `v in set` | `v in tuple` |
| Add | `.append()` / `.extend()` | `d[k]=v` / `.update()` | `.add()` / `.update()` | ❌ |
| Update | `list[i]=v` | `d[k]=v` | ❌ (remove + add) | ❌ |
| Delete | `.remove()` / `.pop()` / `del` | `.pop()` / `del` | `.discard()` / `.remove()` | ❌ |
| Access by index | ✅ `list[0]` | ❌ | ❌ | ✅ `tuple[0]` |
| Access by key | ❌ | ✅ `d["k"]` | ❌ | ❌ |
| Allow duplicates | ✅ | Keys: ❌ / Values: ✅ | ❌ | ✅ |
| Ordered | ✅ | ✅ (since 3.7) | ❌ | ✅ |
| Mutable | ✅ | ✅ | ✅ | ❌ |
| Iterable | ✅ | ✅ (keys) | ✅ | ✅ |

---

### 💡 The Patterns You'll Use Daily in AI Work

```python
# 1. Group items by a field (RAG chunks by source, messages by user)
groups = {}
for item in items:
    groups.setdefault(item["category"], []).append(item)

# 2. Deduplicate while preserving order (clean retrieval results)
seen = set()
unique = [x for x in items if not (x in seen or seen.add(x))]

# 3. Top-K by score (top retrievals to feed an LLM)
top_k = sorted(results, key=lambda r: r["score"], reverse=True)[:5]

# 4. Safe nested access (parsing API responses)
text = response.get("content", [{}])[0].get("text", "")

# 5. Merge configs (defaults + overrides)
config = {**defaults, **user_overrides}

# 6. Count occurrences (token frequency, model usage)
from collections import Counter
counts = Counter(item["model"] for item in api_calls)

# 7. Compare two collections (skills you have vs need)
missing = set(required) - set(have)

# 8. Filter + transform in one shot
expensive_calls = [c["id"] for c in calls if c["cost"] > 0.05]
```



### Day 3 — Data Structures Deep Dive

> **Goal:** Master the four Python collections (list, dict, set, tuple) — because every AI API response, embedding vector, conversation history, and document chunk lives inside one of them. If Day 1 was learning the alphabet, today is learning to form sentences.

#### Why This Day Matters for AI Engineering

Almost everything in AI engineering is data shuffling between collections. Get fluent with these four structures and you can wire up any LLM application.

| What you're doing | Data structure involved |
|---|---|
| Parsing Claude's API response | Nested dict |
| Storing conversation history | List of dicts |
| Chunking a PDF for RAG | List of strings |
| Embedding a document | List of floats (vector) |
| Tracking unique tokens / dedup chunks | Set |
| Returning `(answer, confidence_score)` | Tuple |
| Storing model config | Dict |
| Filtering messages by role | List comprehension |
| Counting tokens per user | Dict comprehension |
| Finding skills you have vs need | Set operations |

---

#### 1. Lists — Ordered, Mutable, Your Workhorse

A list is an ordered, changeable collection. In AI work, you'll use lists for: conversation history, document chunks, embedding vectors, batch inputs, and search results.

**Slicing — `list[start:stop:step]`**

Slicing grabs a piece of a list without writing a loop.

```python
chunks = ["intro", "chapter1", "chapter2", "chapter3", "chapter4", "summary"]

chunks[0]          # "intro"     — first
chunks[-1]         # "summary"   — last
chunks[1:4]        # ["chapter1", "chapter2", "chapter3"]   — middle slice
chunks[:3]         # ["intro", "chapter1", "chapter2"]      — first 3
chunks[3:]         # ["chapter3", "chapter4", "summary"]    — from index 3 onward
chunks[::2]        # ["intro", "chapter2", "chapter4"]      — every 2nd item
chunks[::-1]       # reversed list
```

The `start:stop:step` rule:
- `start` is inclusive
- `stop` is **exclusive**
- `step` is how many to skip

> ⚠️ This is THE most common slicing bug — `chunks[1:4]` gives you indexes 1, 2, 3 (NOT 4).

**Real AI use case — sliding context window:**
```python
conversation = [...]  # list of message dicts
recent = conversation[-10:]   # Last 10 messages — keep context window small
```

**`append` vs `extend` — Critical Difference**

Most beginners confuse these, and it causes silent bugs in AI pipelines (you accidentally end up with a list of lists instead of a flat list).

```python
history = ["hi", "hello"]

# append() — adds ONE item, whatever it is
history.append("how are you")
# ["hi", "hello", "how are you"]

history.append(["new", "messages"])
# ["hi", "hello", "how are you", ["new", "messages"]]
#                                ↑ a list INSIDE a list — usually a bug

# extend() — unpacks an iterable and adds each item
history = ["hi", "hello"]
history.extend(["new", "messages"])
# ["hi", "hello", "new", "messages"]   ← what you usually want
```

**Rule of thumb:**
- Adding ONE message? → `.append(message)`
- Merging two conversation lists? → `.extend(other_list)`

**Sorting — `sort()` vs `sorted()`**

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# sort() — modifies the original list, returns None
numbers.sort()
# numbers is now [1, 1, 2, 3, 4, 5, 6, 9]

# sorted() — returns a NEW sorted list, original unchanged
original = [3, 1, 4]
new_list = sorted(original)
# original = [3, 1, 4] (unchanged), new_list = [1, 3, 4]
```

**Sorting with a `key` function — incredibly common in AI work:**

```python
# Sort search results by relevance score (highest first)
results = [
    {"text": "doc A", "score": 0.72},
    {"text": "doc B", "score": 0.91},
    {"text": "doc C", "score": 0.65},
]

sorted_results = sorted(results, key=lambda r: r["score"], reverse=True)
top_3 = sorted_results[:3]   # Top 3 retrievals — pass to the LLM as context
```

A `lambda` is just an inline tiny function. `lambda r: r["score"]` means "given r, return r['score']."

**`filter()` and List Comprehensions**

Both filter a list, but comprehensions are the Pythonic choice.

```python
messages = [
    {"role": "user",      "content": "hi"},
    {"role": "assistant", "content": "hello"},
    {"role": "user",      "content": "how are you?"},
]

# Using filter() — works but rarely seen in modern Python
user_msgs = list(filter(lambda m: m["role"] == "user", messages))

# Using a list comprehension — preferred
user_msgs = [m for m in messages if m["role"] == "user"]
```

**List comprehension cookbook:**

```python
tokens = [10, 25, 40, 15]

# Basic transform — cost per call at $0.003 per token
costs = [t * 0.003 for t in tokens]

# With condition
expensive = [t for t in tokens if t > 20]              # [25, 40]

# Transform AND filter
high_cost = [t * 0.003 for t in tokens if t > 20]      # [0.075, 0.12]

# Nested — flatten a list of batches
batches = [["a", "b"], ["c", "d"], ["e"]]
flat = [item for batch in batches for item in batch]   # ["a", "b", "c", "d", "e"]

# With if-else (transform every item, choose between values)
labels = ["short" if t < 20 else "long" for t in tokens]
# ["short", "long", "long", "short"]
```

> ⚠️ Comprehensions are powerful, but if one needs more than one `if` and one `for`, write a regular `for` loop. Readability beats cleverness.

---

#### 2. Dictionaries — The Most Important Structure for AI

> Every Claude API response is a dict. Every JSON config is a dict. Every embedding metadata record is a dict. **Master this one.**

**Nested Dictionaries — Real Claude API Response Shape**

```python
api_response = {
    "id": "msg_abc123",
    "type": "message",
    "role": "assistant",
    "content": [
        {"type": "text", "text": "The capital of France is Paris."}
    ],
    "model": "claude-sonnet-4-20250514",
    "stop_reason": "end_turn",
    "usage": {
        "input_tokens": 12,
        "output_tokens": 8,
        "cache_read_input_tokens": 0
    }
}

# Drilling into nested structure
answer = api_response["content"][0]["text"]
# "The capital of France is Paris."

input_tokens  = api_response["usage"]["input_tokens"]
output_tokens = api_response["usage"]["output_tokens"]
total_tokens  = input_tokens + output_tokens
```

The pattern is always: `dict["key"][index]["key"][...]`. Read it left to right like a path.

**`.get()` — Defensive Coding for APIs**

API responses sometimes drop optional fields. `dict[key]` crashes; `dict.get(key)` returns `None` (or a default). Use `.get()` whenever a field is optional.

```python
# DANGEROUS — crashes with KeyError if "cache_read_input_tokens" is missing
cache_tokens = api_response["usage"]["cache_read_input_tokens"]

# SAFE — returns None if missing
cache_tokens = api_response["usage"].get("cache_read_input_tokens")

# SAFE with default — returns 0 if missing
cache_tokens = api_response["usage"].get("cache_read_input_tokens", 0)
```

**Rule:** when reading API responses, use `.get()` for optional fields and `[]` only for fields that MUST exist (where a loud crash is what you want).

**`.keys()`, `.values()`, `.items()`**

```python
config = {"model": "claude-opus-4-7", "temperature": 0.7, "max_tokens": 1024}

list(config.keys())      # ["model", "temperature", "max_tokens"]
list(config.values())    # ["claude-opus-4-7", 0.7, 1024]
list(config.items())     # [("model", "claude-opus-4-7"), ("temperature", 0.7), ...]

# .items() is what you almost always want — gives you both key AND value:
for key, value in config.items():
    print(f"{key} = {value}")
```

**Dict Comprehensions — Build Dicts on the Fly**

Same shape as list comprehensions, but with `key: value` syntax.

```python
# Basic — square each number
squared = {n: n**2 for n in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filter a dict — keep only enabled models
active_models = {"opus": True, "sonnet": True, "haiku": False}
enabled = {k: v for k, v in active_models.items() if v}
# {"opus": True, "sonnet": True}

# Invert a dict (swap keys and values)
model_codes = {"opus": "O", "sonnet": "S", "haiku": "H"}
reversed_codes = {v: k for k, v in model_codes.items()}
# {"O": "opus", "S": "sonnet", "H": "haiku"}
```

**Merging Dicts — Combining Configs**

```python
defaults  = {"temperature": 0.7, "max_tokens": 1024}
overrides = {"temperature": 0.2}

# Python 3.9+ syntax
final = defaults | overrides
# {"temperature": 0.2, "max_tokens": 1024}   ← later values win

# ** unpacking (works on any version)
final = {**defaults, **overrides}
# Same result
```

This pattern shows up constantly when building API call configs (start with defaults, override per-call).

---

#### 3. Sets — Unique, Unordered, Lightning-Fast Lookups

Sets answer two questions fast: "does X exist in this collection?" and "what's unique here?"

```python
# Creating sets
skills = {"Python", "FastAPI", "LangChain"}
empty = set()    # NOT {} — that's an empty dict!

# Adding / removing
skills.add("RAG")
skills.discard("Java")    # remove if present, no error if missing
skills.remove("Java")     # KeyError if missing — be careful
```

**Why sets matter for AI work — deduplication:**

```python
# A RAG retriever often surfaces overlapping chunks
chunks = ["Paris is the capital", "Paris is the capital", "France is in Europe"]

unique_chunks = list(set(chunks))
# ["Paris is the capital", "France is in Europe"]
```

**Set Operations — Compare Two Collections**

```python
required_skills = {"Python", "SQL", "LangChain", "FastAPI"}
my_skills       = {"Python", "Power Platform", "SQL", "GitHub Actions"}

# UNION — everything in either set
required_skills | my_skills
# {"Python", "SQL", "LangChain", "FastAPI", "Power Platform", "GitHub Actions"}

# INTERSECTION — what's in BOTH (skills I already have)
required_skills & my_skills
# {"Python", "SQL"}

# DIFFERENCE — in first but NOT in second (skills I still need)
required_skills - my_skills
# {"LangChain", "FastAPI"}

# SYMMETRIC DIFFERENCE — in either but NOT both
required_skills ^ my_skills
# {"LangChain", "FastAPI", "Power Platform", "GitHub Actions"}
```

**AI use case — find shared keywords across documents:**
```python
doc1_keywords = {"transformer", "attention", "embedding", "model"}
doc2_keywords = {"attention", "model", "fine-tuning", "lora"}

shared = doc1_keywords & doc2_keywords
# {"attention", "model"} — these documents are topically related
```

> 💡 Sets check membership in O(1) — basically instant. Lists check in O(n) — slow on big lists. If you're doing `if x in big_collection:` repeatedly, convert to a set first.

---

#### 4. Tuples — Lightweight, Immutable, Great for Returning Multiple Values

Tuples are like lists but cannot be changed. Use them when data has fixed structure.

**Creation and unpacking:**

```python
# Creation
coords = (28.6139, 77.2090)
single = (42,)    # ⚠️ Trailing comma — without it, it's just an int

# Unpacking — common Python pattern
lat, lon = coords
print(f"Lat: {lat}, Lon: {lon}")

# Functions can return multiple values via tuples
def analyze_response(text):
    word_count = len(text.split())
    char_count = len(text)
    return word_count, char_count    # returns a tuple

words, chars = analyze_response("hello world from claude")
# words = 4, chars = 23
```

**Swapping variables — Python's coolest one-liner:**
```python
a, b = 1, 2
a, b = b, a    # Now a=2, b=1
```

**The `*` rest pattern:**
```python
first, *middle, last = [1, 2, 3, 4, 5]
# first=1, middle=[2, 3, 4], last=5

# AI use case — split system prompt from rest of conversation
system_prompt, *user_messages = full_conversation
```

**Named Tuples — Tuples with Field Names**

Plain tuples are great until you forget what `result[0]` and `result[2]` mean. Named tuples fix this.

```python
from collections import namedtuple

# Define the shape ONCE
SearchResult = namedtuple("SearchResult", ["doc_id", "score", "text"])

# Create instances
r1 = SearchResult(doc_id="d_42", score=0.91, text="Paris is the capital...")
r2 = SearchResult("d_17", 0.78, "France borders Spain...")

# Access by name (clear!) OR by index (still works)
r1.score          # 0.91
r1.text           # "Paris is the capital..."
r1[0]             # "d_42"

# Still immutable
# r1.score = 0.5   # ERROR — can't modify
```

When to use what:
- **dict** — keys are dynamic / unknown ahead of time, OR you want to mutate fields
- **namedtuple** — small, fixed shape, immutable, want clean attribute access
- **tuple** (plain) — truly throwaway / 2-3 values where field names don't help

> 🤔 If you find yourself reaching for namedtuples often, look up `dataclasses` (Day 5 territory). Same idea but with defaults, type hints, and methods.

---

#### Day 3 Experiment — Employee Data Analysis

This is structured the same way you'll process API logs, RAG retrievals, or any tabular AI data. Same patterns, different domain.

```python
# day3_employees.py

employees = [
    {"name": "Ravi",    "dept": "Engineering", "salary": 800000},
    {"name": "Priya",   "dept": "Marketing",   "salary": 600000},
    {"name": "Arjun",   "dept": "Engineering", "salary": 950000},
    {"name": "Sneha",   "dept": "HR",          "salary": 550000},
    {"name": "Vikram",  "dept": "Engineering", "salary": 720000},
    {"name": "Meera",   "dept": "Marketing",   "salary": 680000},
    {"name": "Karthik", "dept": "HR",          "salary": 500000},
]


# 1. Group employees by department
def group_by_department(emps):
    """Return a dict mapping department -> list of employee names."""
    grouped = {}
    for emp in emps:
        # setdefault: if key missing, create with []; either way return the list
        grouped.setdefault(emp["dept"], []).append(emp["name"])
    return grouped

# Output: {"Engineering": ["Ravi", "Arjun", "Vikram"], "Marketing": [...], "HR": [...]}


# 2. Find the highest paid employee
def highest_paid(emps):
    """Return the dict of the highest-paid employee."""
    return max(emps, key=lambda e: e["salary"])

# max() with key= — compare items by salary, return the whole dict
# Output: {"name": "Arjun", "dept": "Engineering", "salary": 950000}


# 3. Calculate average salary per department
def avg_salary_by_department(emps):
    """Return a dict mapping department -> average salary (rounded)."""
    by_dept = {}
    for emp in emps:
        by_dept.setdefault(emp["dept"], []).append(emp["salary"])

    # Dict comprehension — turn list of salaries into average
    return {dept: round(sum(salaries) / len(salaries), 2)
            for dept, salaries in by_dept.items()}

# Output: {"Engineering": 823333.33, "Marketing": 640000.0, "HR": 525000.0}


# 4. Filter employees with salary > 700000
def high_earners(emps, threshold=700000):
    """Return a list of employees earning more than the threshold."""
    return [e for e in emps if e["salary"] > threshold]

# Output: [{"name": "Ravi", ...}, {"name": "Arjun", ...}, {"name": "Vikram", ...}]


if __name__ == "__main__":
    print("By department:    ", group_by_department(employees))
    print("Highest paid:     ", highest_paid(employees))
    print("Average per dept: ", avg_salary_by_department(employees))
    print("High earners:     ", high_earners(employees))
```

**What this teaches you that maps directly to AI work:**

| Function | Pattern | AI engineering parallel |
|---|---|---|
| `group_by_department` | Group records by a field | Group messages by user, group retrievals by source doc |
| `highest_paid` | Find max by a custom key | Find highest-confidence retrieval, longest message in a batch |
| `avg_salary_by_department` | Group + aggregate | Average tokens per model, average latency per endpoint |
| `high_earners` | Filter by threshold | Filter retrievals by score (e.g., score > 0.75) |

#### Bonus Challenges (AI-themed)

Same patterns, real LLM scenario. If you can knock these out, you've got the data-shuffling foundation for any LLM application.

```python
api_calls = [
    {"model": "claude-opus-4-7",   "tokens": 1200, "cost": 0.018,  "user": "alice"},
    {"model": "claude-sonnet-4-6", "tokens": 800,  "cost": 0.004,  "user": "bob"},
    {"model": "claude-opus-4-7",   "tokens": 2500, "cost": 0.038,  "user": "alice"},
    {"model": "claude-haiku-4-5",  "tokens": 500,  "cost": 0.0005, "user": "carol"},
    {"model": "claude-sonnet-4-6", "tokens": 1100, "cost": 0.0055, "user": "alice"},
]

# 1. Group calls by model — which models are most used?
# 2. Find the most expensive single call
# 3. Calculate total cost per user
# 4. Filter calls with > 1000 tokens (candidates for prompt caching)
# 5. Get the SET of unique users (using set())
# 6. Return (most_used_model, its_call_count) as a tuple
```

---

#### Day 3 Cheat Sheet

```python
# LIST
items[1:4]                          # slice — index 1 to 3
items[::-1]                         # reversed
items.append(x)                     # add ONE item
items.extend(other)                 # merge two lists
sorted(items, key=lambda x: x.score, reverse=True)
[x for x in items if x > 5]         # filter
[x*2 for x in items]                # transform

# DICT
d.get("key", default)               # safe access
for k, v in d.items(): ...          # standard iteration
{k: v for k, v in d.items() if v}   # dict comprehension
{**d1, **d2}                        # merge

# SET
a | b                               # union
a & b                               # intersection
a - b                               # difference
list(set(items))                    # dedupe a list

# TUPLE
lat, lon = coords                   # unpack
first, *rest = items                # rest pattern
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
```

---




# Day 4 — File Handling & Error Handling

> **Goal:** Master reading/writing files (text, CSV, JSON, JSONL), understand encoding, and gracefully handle errors. This is the foundation for every real AI application — loading prompts, saving conversation history, parsing API responses, processing datasets, and surviving when the network dies mid-call.

---

## 📋 Table of Contents

- [Why This Matters for AI Engineers](#why-this-matters-for-ai-engineers)
- [Part 1: File Handling — The Foundation](#part-1-file-handling--the-foundation)
  - [1.1 Opening Files — `open()` and Modes](#11-opening-files--open-and-modes)
  - [1.2 The `with` Statement — Why You Should ALWAYS Use It](#12-the-with-statement--why-you-should-always-use-it)
  - [1.3 Reading Files — Four Different Methods](#13-reading-files--four-different-methods)
  - [1.4 Writing Files](#14-writing-files)
  - [1.5 File Paths — Relative vs Absolute, and `pathlib`](#15-file-paths--relative-vs-absolute-and-pathlib)
  - [1.6 Encoding — UTF-8 and Why It Matters for AI](#16-encoding--utf-8-and-why-it-matters-for-ai)
- [Part 2: CSV Files — Working with Tabular Data](#part-2-csv-files--working-with-tabular-data)
  - [2.1 What is CSV?](#21-what-is-csv)
  - [2.2 Manual Reading (and Why It Breaks)](#22-manual-reading-and-why-it-breaks)
  - [2.3 The `csv` Module — Basic Usage](#23-the-csv-module--basic-usage)
  - [2.4 `csv.DictReader` and `csv.DictWriter` — The Preferred Way](#24-csvdictreader-and-csvdictwriter--the-preferred-way)
  - [2.5 Common CSV Gotchas — Deep Dive](#25-common-csv-gotchas--deep-dive)
  - [2.6 When to Stop Using `csv` and Use `pandas`](#26-when-to-stop-using-csv-and-use-pandas)
- [Part 3: JSON — The Language of APIs](#part-3-json--the-language-of-apis)
  - [3.1 Why JSON is THE Format for AI Engineers](#31-why-json-is-the-format-for-ai-engineers)
  - [3.2 Reading JSON — `json.load()` vs `json.loads()`](#32-reading-json--jsonload-vs-jsonloads)
  - [3.3 Writing JSON](#33-writing-json)
  - [3.4 Python ↔ JSON Type Mapping](#34-python--json-type-mapping)
  - [3.5 JSONL — JSON Lines (Critical for AI)](#35-jsonl--json-lines-critical-for-ai)
  - [3.6 Real Example — Parsing a Claude API Response](#36-real-example--parsing-a-claude-api-response)
- [Part 4: Error Handling — Code That Doesn't Crash](#part-4-error-handling--code-that-doesnt-crash)
  - [4.1 Why Errors Matter (Especially for AI Apps)](#41-why-errors-matter-especially-for-ai-apps)
  - [4.2 Anatomy of an Error (the Traceback)](#42-anatomy-of-an-error-the-traceback)
  - [4.3 `try / except` — The Basics](#43-try--except--the-basics)
  - [4.4 The `as e` Trap — Class vs Instance](#44-the-as-e-trap--class-vs-instance)
  - [4.5 Catching Specific Exceptions](#45-catching-specific-exceptions)
  - [4.6 Multiple `except` Blocks](#46-multiple-except-blocks)
  - [4.7 The `else` Clause](#47-the-else-clause)
  - [4.8 The `finally` Clause](#48-the-finally-clause)
  - [4.9 Full Picture — `try / except / else / finally`](#49-full-picture--try--except--else--finally)
  - [4.10 `raise` — Throwing Your Own Errors](#410-raise--throwing-your-own-errors)
  - [4.11 Custom Exception Classes](#411-custom-exception-classes)
  - [4.12 Common Built-in Exceptions Cheat Sheet](#412-common-built-in-exceptions-cheat-sheet)
  - [4.13 Real-World AI Pattern — Retry With Backoff](#413-real-world-ai-pattern--retry-with-backoff)
- [Day 4 Experiment — Mini Conversation Logger](#day-4-experiment--mini-conversation-logger)
- [Common Pitfalls I Hit](#common-pitfalls-i-hit)
- [Day 4 Cheat Sheet](#day-4-cheat-sheet)

---

## Why This Matters for AI Engineers

Every real AI app you'll build does these things constantly:

| What an AI app does | What you need from Day 4 |
|---|---|
| Load a prompt template from `prompt.txt` | File reading |
| Save conversation history between sessions | JSON write |
| Read a dataset of customer support tickets | CSV reading |
| Parse the response from `claude.messages.create()` | JSON parsing |
| Save fine-tuning data in JSONL format | JSONL write |
| Retry when the API rate-limits you | Error handling |
| Survive when a user uploads a corrupt file | Error handling |
| Log every API call for debugging | File append + JSON |
| Read API keys from a `.env` file | File reading |
| Cache expensive API responses to disk | JSON read/write |

> If you can't handle files and errors, you can't build AI apps. You can only build demos. The gap between a demo and a product is 80% error handling.

---

## Part 1: File Handling — The Foundation

### 1.1 Opening Files — `open()` and Modes

The `open()` function is how Python talks to files on your disk.

```python
file = open("notes.txt", "r")     # open for reading
content = file.read()              # read everything
file.close()                       # ALWAYS close it
```

The second argument is the **mode** — it tells Python what you want to do with the file.

| Mode | Meaning | If file doesn't exist | If file exists |
|---|---|---|---|
| `"r"` | Read (default) | ❌ Crashes (`FileNotFoundError`) | Opens for reading |
| `"w"` | Write | ✅ Creates new | ⚠️ **Overwrites everything** |
| `"a"` | Append | ✅ Creates new | Adds to end (safe) |
| `"x"` | Exclusive create | ✅ Creates new | ❌ Crashes (`FileExistsError`) |
| `"r+"` | Read + Write | ❌ Crashes | Opens for both |
| `"rb"` / `"wb"` | Binary read/write | — | For images, PDFs, audio |
| `"rt"` / `"wt"` | Text mode (default) | — | Same as `r` / `w` |

> ⚠️ **The `"w"` trap:** Opening a file in `"w"` mode **deletes its contents instantly** — even before you write anything. If you want to keep what's there, use `"a"` (append).

**Real AI engineering examples:**

```python
# Loading a system prompt
open("system_prompt.txt", "r")              # text → "r"

# Reading a PDF for RAG
open("research_paper.pdf", "rb")            # PDF is binary → "rb"

# Logging every API call
open("api_calls.log", "a")                  # append, never overwrite → "a"

# Saving an image generated by an AI model
open("generated_image.png", "wb")           # image is binary → "wb"
```

### 1.2 The `with` Statement — Why You Should ALWAYS Use It

The manual approach has a fatal flaw:

```python
# ❌ THE WRONG WAY
file = open("notes.txt", "r")
content = file.read()
# ... what if an error happens here? ...
file.close()    # Never reached → file stays open → memory leak
```

The `with` statement (called a **context manager**) auto-closes the file even if your code crashes:

```python
# ✅ THE RIGHT WAY
with open("notes.txt", "r") as file:
    content = file.read()
# File is automatically closed here, GUARANTEED.
# Even if read() crashes, the file still gets closed.
```

**Analogy:** `with` is like a self-closing door. You walk in, do your work, walk out — and the door closes itself behind you. Without `with`, you have to remember to close the door, and if you trip on the way out, the door stays open forever.

> **Rule:** From this day forward, every time you open a file, use `with`. No exceptions.

### 1.3 Reading Files — Four Different Methods

```python
# Method 1: read() — entire file as ONE string
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
# Use when: file is small (< a few MB)
# Don't use when: file is huge (loads everything into RAM)

# Method 2: readline() — ONE line at a time
with open("notes.txt", "r") as f:
    first_line = f.readline()    # gets line 1
    second_line = f.readline()   # gets line 2
# Use when: you need precise control

# Method 3: readlines() — ALL lines as a LIST
with open("notes.txt", "r") as f:
    lines = f.readlines()
    # ['First line\n', 'Second line\n', 'Third line\n']
# Use when: you need to access lines by index

# Method 4: Iteration — line-by-line, MEMORY EFFICIENT (best for big files)
with open("huge_dataset.txt", "r") as f:
    for line in f:
        process(line.strip())   # .strip() removes \n at the end
# Use when: file is large (millions of lines)
# This is THE method AI engineers use for datasets.
```

> 💡 **`.strip()` is your friend.** Each line read from a file ends with `\n` (newline character). Use `line.strip()` to remove it. Otherwise `"hello\n" == "hello"` is `False` and you'll waste hours debugging.

**Test file — create `notes.txt` with this content:**

```
Day 1: Set up Python, VS Code, Git, and GitHub.
Day 2: Learned about functions, modules, and how to organize code.
Day 3: Deep dive into lists, dicts, sets, and tuples.
Day 4: File handling and error handling — the foundation of real apps.
Day 5: Object-Oriented Programming with classes and objects.
Day 6: Working with requests and dotenv for API calls.
Day 7: Pandas and Matplotlib for data analysis.
```

Then run a small test script that exercises all four methods:

```python
# test_file_reading.py
print("=== Method 1: read() ===")
with open("notes.txt", "r", encoding="utf-8") as f:
    print(f.read())

print("=== Method 3: readlines() ===")
with open("notes.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f.readlines(), 1):
        print(f"{i}. {line.strip()}")

print("=== Method 4: Iteration (search for keyword) ===")
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "Pandas" in line:
            print(f"Found: {line.strip()}")

print("=== Bonus: Why .strip() matters ===")
with open("notes.txt", "r", encoding="utf-8") as f:
    raw = f.readline()
    print(f"Without strip: {repr(raw)}")        # shows the \n
    print(f"With strip:    {repr(raw.strip())}")  # \n removed
```

### 1.4 Writing Files

```python
# Single string
with open("output.txt", "w") as f:
    f.write("Hello, AI world!\n")
    f.write("Line 2\n")            # \n = newline (you must add it manually)

# Multiple lines from a list
lines = ["Apple\n", "Banana\n", "Cherry\n"]
with open("fruits.txt", "w") as f:
    f.writelines(lines)            # writes them all in order

# Appending (won't overwrite existing content)
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```

> ⚠️ **`write()` does NOT add newlines automatically.** If you forget `\n`, your output becomes one giant line: `"HelloLine 2"` instead of two separate lines.

### 1.5 File Paths — Relative vs Absolute, and `pathlib`

```python
# Relative path — starts where your script is running
open("data.txt")               # same folder as script
open("data/notes.txt")         # subfolder
open("../other/file.txt")      # parent folder, then "other" subfolder

# Absolute path — full address from the drive root
open("C:/Users/smadavaram/Desktop/data.txt")        # ✅ forward slashes work
open(r"C:\Users\smadavaram\Desktop\data.txt")       # ✅ "raw string" with r prefix
open("C:\Users\smadavaram\Desktop\data.txt")        # ❌ \U is interpreted as escape!
```

> ⚠️ **Windows backslash trap:** `"\n"` is newline, `"\t"` is tab, `"\U..."` is a Unicode escape. So `"C:\Users\..."` can break in surprising ways. Either use forward slashes (`/`) or prefix with `r"..."` (raw string).

**Modern way: `pathlib`** (recommended for new code):

```python
from pathlib import Path

# Build paths cleanly — no slash confusion, works on Windows AND Mac/Linux
project = Path("C:/Users/smadavaram/AI-Engineering-Journey")
data_file = project / "datasets" / "tickets.csv"   # the / is path join

# Useful pathlib operations:
data_file.exists()        # True/False — check before opening
data_file.is_file()       # True if it's a file
data_file.parent          # the folder containing it
data_file.name            # "tickets.csv"
data_file.stem            # "tickets" (no extension)
data_file.suffix          # ".csv"

# Read and write directly (no `with` needed for one-shot reads):
text = data_file.read_text(encoding="utf-8")
data_file.write_text("new content", encoding="utf-8")

# List all CSV files in a folder:
for csv_file in project.glob("**/*.csv"):    # ** = recursive
    print(csv_file)
```

> 💡 **For AI engineering, prefer `pathlib`.** It works the same on Windows, Mac, and Linux — important when you deploy to cloud servers (which run Linux).

### 1.6 Encoding — UTF-8 and Why It Matters for AI

Computers store everything as numbers. **Encoding** is the rule that maps numbers ↔ characters.

```python
# Always specify encoding="utf-8" for AI work
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()
```

**Why this matters for AI:**

| Without `encoding="utf-8"` | With `encoding="utf-8"` |
|---|---|
| Crashes on emojis 😀 | Works fine |
| Crashes on Hindi (नमस्ते), Chinese (你好), Arabic (مرحبا) | Works fine |
| Crashes on smart quotes `"like these"` (common in AI outputs) | Works fine |
| Default on Windows is `cp1252`, on Mac/Linux is `utf-8` → same code breaks across machines | Same behavior everywhere |

> ⚠️ **Always pass `encoding="utf-8"` explicitly.** Claude, GPT, Gemini all output Unicode (emojis, smart quotes, non-English). If you don't specify UTF-8, your code will work on your laptop and crash in production.

```python
# THIS is the AI engineer's default file open:
with open("anything.txt", "r", encoding="utf-8") as f:
    ...
```

---

## Part 2: CSV Files — Working with Tabular Data

### 2.1 What is CSV?

**CSV = Comma-Separated Values.** It's a plain text file where each line is a row, and commas separate columns. It's the universal format for spreadsheet-like data.

```
name,age,role
Smadavaram,25,Power Platform Developer
Anita,30,Data Scientist
Raj,28,AI Engineer
```

**Where AI engineers see CSV every day:**
- Customer support tickets (input for classification models)
- Evaluation datasets ("here are 100 questions, run them through Claude, measure accuracy")
- Exported logs from analytics tools
- Training data for fine-tuning
- Output from `pandas` (Day 7)

### 2.2 Manual Reading (and Why It Breaks)

A beginner's first instinct:

```python
# ❌ THE NAIVE APPROACH — works for simple files, breaks for real ones
with open("people.csv", "r", encoding="utf-8") as f:
    for line in f:
        fields = line.strip().split(",")
        print(fields)
```

**Why it breaks — commas inside values:**

Imagine you have this data and want to save it:

| name | quote | age |
|---|---|---|
| Smadavaram | Hello, world! | 25 |

Notice `Hello, world!` already has a comma in it. The CSV standard rule is: **wrap any value containing a comma in double quotes.** So the file looks like:

```
name,quote,age
Smadavaram,"Hello, world!",25
```

A human reads this as 3 fields: `Smadavaram`, `Hello, world!`, `25`.

But Python's `.split(",")` doesn't understand the quote-wrapping rule. It just blindly splits on every comma:

```python
line = 'Smadavaram,"Hello, world!",25'
fields = line.split(",")
print(fields)
# ['Smadavaram', '"Hello', ' world!"', '25']
#  ↑              ↑          ↑          ↑
#  field 1      WRONG     WRONG      field 3
```

You expected **3 fields**. You got **4**. The "Hello, world!" got ripped in half by the comma inside it.

> **The line has 3 commas total — 2 are real separators, 1 is part of the data.** `.split(",")` can't tell them apart. The `csv` module CAN — because it understands the quote-wrapping rule.

**See it side by side:**

```python
import csv

content = '''name,quote,age
Smadavaram,"Hello, world!",25
Anita,"She said ""hi"" to me",30
Raj,Plain text,28
'''
with open("tricky.csv", "w", encoding="utf-8") as f:
    f.write(content)

print("=== Manual split (BROKEN) ===")
with open("tricky.csv", "r", encoding="utf-8") as f:
    next(f)  # skip header
    for line in f:
        fields = line.strip().split(",")
        print(f"Got {len(fields)} fields: {fields}")

print("\n=== csv module (CORRECT) ===")
with open("tricky.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        print(f"Got {len(row)} fields: {row}")
```

Output:
```
=== Manual split (BROKEN) ===
Got 4 fields: ['Smadavaram', '"Hello', ' world!"', '25']
Got 5 fields: ['Anita', '"She said ""hi"" to me"', '30']
Got 3 fields: ['Raj', 'Plain text', '28']

=== csv module (CORRECT) ===
Got 3 fields: ['Smadavaram', 'Hello, world!', '25']
Got 3 fields: ['Anita', 'She said "hi" to me', '30']
Got 3 fields: ['Raj', 'Plain text', '28']
```

> **Rule:** Never parse CSV by hand. Use the `csv` module (or `pandas` for big jobs).

### 2.3 The `csv` Module — Basic Usage

```python
import csv

# Reading
with open("people.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# Each row is a LIST of strings: ['Smadavaram', 'Hello, world!', '25']

# Writing
rows = [
    ["name", "age", "role"],
    ["Smadavaram", 25, "AI Engineer"],
    ["Anita", 30, "Data Scientist"],
]
with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)        # writes all rows at once
    # Or: writer.writerow(["one", "row", "at", "a", "time"])
```

#### What `newline=""` actually does

Different operating systems use different end-of-line characters:

| OS | End-of-line | Looks like |
|---|---|---|
| Windows | `\r\n` | 2 characters |
| Mac/Linux | `\n` | 1 character |

By default, Python text-mode files do "universal newlines translation" — when writing, every `\n` you write becomes `\r\n` on Windows. The `csv` module ALSO writes `\r\n` itself. Result: **double conversion** → `\r\r\n` → blank rows when Excel opens the file.

`newline=""` tells Python: **"Don't touch the line endings. Let the csv module handle them."**

> **Don't memorize the why. Memorize the rule:** Always pass `newline=""` when opening CSV files — both for reading and writing.

### 2.4 `csv.DictReader` and `csv.DictWriter` — The Preferred Way

Working with column names instead of indices is much more readable:

```python
import csv

# Reading as dictionaries — each row becomes a dict using the header as keys
with open("people.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])    # access by column name!
        # row is: {"name": "Smadavaram", "age": "25", "role": "..."}
```

> ⚠️ Notice `row["age"]` is the **string** `"25"`, not the integer `25`. CSVs don't store types. You must convert: `int(row["age"])`.

```python
# Writing dictionaries to CSV
data = [
    {"name": "Smadavaram", "age": 25, "role": "AI Engineer"},
    {"name": "Anita",      "age": 30, "role": "Data Scientist"},
]

with open("output.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "role"])
    writer.writeheader()                  # writes the column names
    writer.writerows(data)                # writes all dicts as rows
```

### 2.5 Common CSV Gotchas — Deep Dive

#### Gotcha 1: Different Delimiter (semicolons, tabs, pipes)

In many European countries, the comma `,` is used as the **decimal point** in numbers ("3,14" means π in Germany, France, Spain). To avoid confusion, those countries use `;` as the field separator.

```python
import csv

content = """name;price;quantity
Apple;1,50;10
Banana;0,75;20"""

with open("european.csv", "w", encoding="utf-8") as f:
    f.write(content)

# Without delimiter — WRONG
with open("european.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['name;price;quantity']            ← whole line as one field!
# ['Apple;1', '50;10']               ← split at the wrong comma

# With delimiter=";" — CORRECT
with open("european.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f, delimiter=";")    # ← tell csv to split on ;
    for row in reader:
        print(row)
# ['name', 'price', 'quantity']
# ['Apple', '1,50', '10']
# ['Banana', '0,75', '20']
```

| File type | Delimiter | Code |
|---|---|---|
| Standard CSV | comma | `csv.reader(f)` (default) |
| European CSV | semicolon | `csv.reader(f, delimiter=";")` |
| TSV (Tab-Separated) | tab | `csv.reader(f, delimiter="\t")` |
| Pipe-separated | pipe | `csv.reader(f, delimiter="|")` |

> 💡 TSV is very common in AI/ML datasets. Hugging Face datasets, log files, and many scientific datasets use tab separators.

#### Gotcha 2: First Row is NOT the Header

Some CSVs are pure data — no header row.

```
Smadavaram,25,AI Engineer
Anita,30,Data Scientist
```

If you use `DictReader` on this, it mistakenly treats the FIRST DATA ROW as column names:

```python
# WRONG — DictReader assumes first row is header
with open("noheader.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
# {'Smadavaram': 'Anita', '25': '30', 'AI Engineer': 'Data Scientist'}
# We lost Smadavaram entirely!
```

**Two solutions:**

```python
# Solution A: Use csv.reader and access by index
with open("noheader.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        name, age, role = row[0], row[1], row[2]
        print(f"{name} is a {role}")

# Solution B: Use DictReader and PROVIDE your own field names
with open("noheader.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f, fieldnames=["name", "age", "role"])
    for row in reader:
        print(f"{row['name']} is a {row['role']}")
```

#### Gotcha 3: Rows With Missing Values

Real-world CSVs are messy:

```csv
name,age,salary
Smadavaram,25,1500000
Anita,30,
Raj,,800000
```

Empty values come back as empty strings `""` (not `None`):

```python
with open("messy.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
# {'name': 'Smadavaram', 'age': '25', 'salary': '1500000'}
# {'name': 'Anita',      'age': '30', 'salary': ''}     ← empty string!
# {'name': 'Raj',        'age': '',   'salary': '800000'}
```

Trying to convert an empty string crashes:

```python
salary = int(row["salary"])     # ❌ ValueError on Anita's row!
```

**Solutions:**

```python
# Pattern 1: "value or default" — handles empty strings
salary_str = row["salary"] or "0"   # if "", use "0"
salary = int(salary_str)

# Pattern 2: .get() — handles missing KEYS (different from missing values!)
salary = row.get("salary", "0")     # if column doesn't exist, default to "0"

# Combined — handles both missing key AND empty value:
salary = int(row.get("salary", "") or "0")
```

> **Key idea:** With messy real-world data, you ALWAYS need a strategy for "what if this is missing?" Decide a default (zero, "Unknown", None, or skip the row) for every column you read.

#### Gotcha 4: Huge Files — Don't Load Everything Into Memory

If your CSV has 10 million rows, you cannot load it all at once.

```python
# ❌ DANGEROUS — loads ALL rows into a list
with open("huge_dataset.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    all_rows = list(reader)        # 5 GB file → 5+ GB of RAM → crash
```

**Fix — process one row at a time (streaming):**

```python
# ✅ SAFE — only ONE row in memory at any moment
with open("huge_dataset.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        process(row)
        # row is garbage-collected after this iteration
```

**Real example — count tickets by category:**

```python
import csv
from collections import Counter

counter = Counter()
with open("support_tickets.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        counter[row["category"]] += 1

print(counter.most_common(10))
# Memory used: a few KB. Works on any file size.
```

#### Other CSV Encoding Quirks

| Problem | Solution |
|---|---|
| Excel saved CSV with weird BOM | Try `encoding="utf-8-sig"` |
| File looks fine but breaks | Check delimiter (might be `;` or `\t`) |
| Numbers come out as strings | Convert: `int(row["age"])`, `float(row["price"])` |

### 2.6 When to Stop Using `csv` and Use `pandas`

The `csv` module is great for simple line-by-line work. But for **analyzing** large data — filtering, computing statistics, joining tables — you'll switch to `pandas` (Day 7).

Here's the example, walked through line by line:

```python
import pandas as pd
df = pd.read_csv("people.csv")
print(df[df["age"] > 25])
```

#### Line 1 — `import pandas as pd`

`pandas` is a Python library (install with `pip install pandas`). The `as pd` part means "from now on, call it `pd`" — a shorter alias. Every Python data scientist writes `pd`. It's a convention.

#### Line 2 — `df = pd.read_csv("people.csv")`

Reads a CSV file and returns a **DataFrame** — pandas's main data structure. A DataFrame is an in-memory table, like an Excel sheet.

If `people.csv` is:
```csv
name,age,role
Smadavaram,25,Power Platform Developer
Anita,30,Data Scientist
Raj,28,AI Engineer
Lina,22,Intern
Mark,35,Engineering Manager
```

Then `df` holds it as:
```
         name  age                       role
0  Smadavaram   25  Power Platform Developer
1       Anita   30            Data Scientist
2         Raj   28               AI Engineer
3        Lina   22                    Intern
4        Mark   35      Engineering Manager
```

The `0, 1, 2, 3, 4` on the left are pandas's auto-generated row index.

#### Line 3 — `print(df[df["age"] > 25])` — the filtering magic

This is doing **two steps at once**:

**Step A: `df["age"] > 25` — comparison on the WHOLE column**

`df["age"]` selects just the age column:
```
0    25
1    30
2    28
3    22
4    35
```

`df["age"] > 25` applies the comparison to every row at once (called **vectorized operations**). The result is a column of True/False values:
```
0    False    ← 25 is NOT > 25
1    True     ← 30 > 25
2    True     ← 28 > 25
3    False    ← 22 is NOT > 25
4    True     ← 35 > 25
```

This True/False column is called a **boolean mask**.

**Step B: `df[mask]` — keep only rows where mask is True**

When you put a boolean mask inside `df[...]`, pandas returns only the rows where the mask is True:

```
         name  age                  role
1       Anita   30        Data Scientist
2         Raj   28           AI Engineer
4        Mark   35   Engineering Manager
```

(Smadavaram and Lina are gone — their ages weren't greater than 25.)

The line `df[df["age"] > 25]` smashes both steps into one — the idiomatic pandas way.

#### Side-by-side comparison

Same task: "Average age per role, sorted by average age."

**With `csv` module:**
```python
import csv
from collections import defaultdict

ages_by_role = defaultdict(list)
with open("people.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ages_by_role[row["role"]].append(int(row["age"]))

averages = {role: sum(ages)/len(ages) for role, ages in ages_by_role.items()}
sorted_avgs = sorted(averages.items(), key=lambda x: x[1])
for role, avg in sorted_avgs:
    print(f"{role}: {avg:.1f}")
```

**With `pandas`:**
```python
import pandas as pd
df = pd.read_csv("people.csv")
print(df.groupby("role")["age"].mean().sort_values())
```

**One line.** That's why AI engineers reach for pandas the moment data analysis enters the picture.

#### Tool selection

| Situation | Use |
|---|---|
| Reading a config file | `json` module |
| Reading a few rows, simple work, OR streaming a huge file | `csv` module |
| Analyzing, filtering, aggregating, computing statistics | `pandas` |
| Building a fine-tuning dataset (line-by-line) | `csv` or write JSONL directly |
| Loading 10K customer support tickets to analyze with Claude | `pandas` |

---

## Part 3: JSON — The Language of APIs

### 3.1 Why JSON is THE Format for AI Engineers

Every AI API in existence uses JSON. Every single one.

```python
# When you call Claude:
response = client.messages.create(...)
# Behind the scenes, you sent JSON, and you received JSON.
# Anthropic, OpenAI, Google — they all speak JSON.
```

**JSON looks identical to a Python dictionary** — that's because Python dicts and JSON were practically made for each other.

```json
{
  "model": "claude-sonnet-4-5",
  "messages": [
    {"role": "user", "content": "Hello"}
  ],
  "max_tokens": 1024,
  "temperature": 0.7
}
```

### 3.2 Reading JSON — `json.load()` vs `json.loads()`

The `json` module has two pairs of functions. The difference is just one letter — `s` for "string."

| Function | Reads from | Returns |
|---|---|---|
| `json.load(file)` | a file object | a Python dict/list |
| `json.loads(text)` | a string | a Python dict/list |
| `json.dump(obj, file)` | writes to a file | nothing |
| `json.dumps(obj)` | writes to a string | a string |

> 💡 **Memory trick:** `s` = "string." `loads` = "load string." `dumps` = "dump to string." No `s` = file.

```python
import json

# Reading from a file
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)             # file → Python dict
    print(config["model"])

# Reading from a string (e.g., API response body as text)
api_response_text = '{"model": "claude-sonnet-4-5", "tokens": 42}'
data = json.loads(api_response_text)  # string → Python dict
print(data["tokens"])                 # 42
```

### 3.3 Writing JSON

```python
import json

data = {
    "name": "Smadavaram",
    "skills": ["Python", "Power Platform"],
    "experience_years": 3,
    "is_learning_ai": True
}

# Writing to a file
with open("profile.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Writing to a string (for logging, sending in HTTP body, etc.)
text = json.dumps(data, indent=2, ensure_ascii=False)
print(text)
```

**Key parameters you'll use constantly:**

| Parameter | What it does |
|---|---|
| `indent=2` | Pretty-print with 2-space indentation (much more readable) |
| `indent=None` (default) | Compact one-liner (smaller file) |
| `ensure_ascii=False` | Allow non-English characters (नमस्ते, 你好) instead of escaping them |
| `sort_keys=True` | Sort dictionary keys alphabetically |

> 💡 **AI engineer's default:** `json.dump(data, f, indent=2, ensure_ascii=False)` — readable AND handles Unicode.

### 3.4 Python ↔ JSON Type Mapping

| Python | ←→ | JSON |
|---|---|---|
| `dict` | ←→ | object `{...}` |
| `list`, `tuple` | →  | array `[...]` |
| `str` | ←→ | string `"..."` |
| `int`, `float` | ←→ | number |
| `True` | ←→ | `true` (lowercase!) |
| `False` | ←→ | `false` |
| `None` | ←→ | `null` |

**Things that DON'T convert:**

```python
# ❌ These will crash with TypeError:
import datetime
data = {"date": datetime.datetime.now()}    # datetime is not JSON-serializable
data = {"unique": {1, 2, 3}}                # sets are not JSON-serializable
data = {"id": b"binary data"}               # bytes are not JSON-serializable

# ✅ Convert them first:
data = {"date": datetime.datetime.now().isoformat()}    # → string
data = {"unique": list({1, 2, 3})}                       # → list
```

### 3.5 JSONL — JSON Lines (Critical for AI)

**JSONL** (also called NDJSON) = **one JSON object per line.**

```jsonl
{"id": 1, "question": "What is AI?", "answer": "AI is..."}
{"id": 2, "question": "What is ML?", "answer": "ML is..."}
{"id": 3, "question": "What is Python?", "answer": "Python is..."}
```

**Why AI engineers use JSONL constantly:**
- Anthropic's **batch API** input/output is JSONL
- OpenAI's **fine-tuning** datasets must be JSONL
- Hugging Face datasets often distribute as JSONL
- Streaming logs (one line = one event) are essentially JSONL

**Reading JSONL — line by line, memory-efficient:**

```python
import json

with open("dataset.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        record = json.loads(line)         # parse ONE line at a time
        print(record["question"])
# Works on huge files because we never load the whole thing into RAM.
```

**Writing JSONL:**

```python
records = [
    {"id": 1, "question": "What is AI?"},
    {"id": 2, "question": "What is ML?"},
]

with open("dataset.jsonl", "w", encoding="utf-8") as f:
    for record in records:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
        # ↑ json.dumps (string) + "\n" → one record per line
```

> 💡 **JSON vs JSONL — the key difference:** Regular JSON loads the entire file into memory. JSONL lets you process gigabyte files line-by-line. For datasets, always JSONL.

### 3.6 Real Example — Parsing a Claude API Response

A Claude API response looks like this:

```python
response = {
    "id": "msg_01ABC123",
    "model": "claude-sonnet-4-5",
    "content": [
        {"type": "text", "text": "The answer is 42."}
    ],
    "stop_reason": "end_turn",
    "usage": {
        "input_tokens": 12,
        "output_tokens": 8
    }
}

# Extracting what you actually care about:
answer = response["content"][0]["text"]
input_tokens = response["usage"]["input_tokens"]
output_tokens = response["usage"]["output_tokens"]

print(f"Answer: {answer}")
print(f"Cost: {input_tokens} in + {output_tokens} out tokens")
```

**Saving the full response for later analysis:**

```python
import json
from datetime import datetime

log_entry = {
    "timestamp": datetime.now().isoformat(),
    "request": {"prompt": "What's 6 times 7?"},
    "response": response,
}

with open("api_log.jsonl", "a", encoding="utf-8") as f:    # append!
    f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")
```

> This is the **exact pattern** you'll use on Day 9 when you make real Claude calls. Logging every API call is non-negotiable for any production AI app — for debugging, cost tracking, and improving prompts.

---

## Part 4: Error Handling — Code That Doesn't Crash

### 4.1 Why Errors Matter (Especially for AI Apps)

Your AI app will fail in dozens of ways you can't control:

| What goes wrong | Why |
|---|---|
| `ConnectionError` | User's wifi blinked |
| `TimeoutError` | Claude API took too long |
| `RateLimitError` | You hit the API rate limit |
| `AuthenticationError` | API key is wrong/expired |
| `JSONDecodeError` | Response was malformed |
| `FileNotFoundError` | User uploaded a file then deleted it |
| `KeyError` | API response missing a field you expected |
| `UnicodeDecodeError` | File has weird encoding |

**A demo crashes when these happen. A product handles them gracefully and either retries, falls back, or shows the user a clean message.**

### 4.2 Anatomy of an Error (the Traceback)

When Python crashes, it shows a **traceback**. Read it from BOTTOM to TOP:

```
Traceback (most recent call last):
  File "app.py", line 12, in <module>
    age = int(input("Age: "))
ValueError: invalid literal for int() with base 10: 'twenty'
└─────┬─────┘ └────────────────────┬───────────────────────────┘
      │                            │
   Type of error          Human-readable message
```

The **last line** tells you the error type and message. Always read it. 80% of debugging is reading tracebacks.

### 4.3 `try / except` — The Basics

```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("That's not a valid number!")
```

**How it reads:** "TRY this code. If a `ValueError` happens, EXCEPT (i.e., handle it) by running the second block."

**Flow:**
```
        ┌────────────────┐
        │  try block     │
        └────────┬───────┘
                 │
           Did an error happen?
            ┌────┴─────┐
            │          │
           No         Yes
            │          │
            ▼          ▼
        Skip       Run the matching
       except      except block
            │          │
            └────┬─────┘
                 ▼
         Continue program
```

### 4.4 The `as e` Trap — Class vs Instance

This trips up everyone. Watch this naive attempt:

```python
try:
    val = 1/0
except Exception:
    print(Exception)
```

**Output:**
```
<class 'Exception'>
```

That's not what you wanted. You wanted to see `division by zero`. So what happened?

#### Three different things that look similar

| Thing | What it is | Example |
|---|---|---|
| `Exception` | The **class** (the blueprint) | `<class 'Exception'>` |
| `ZeroDivisionError` | A **specific class** (a child of Exception) | `<class 'ZeroDivisionError'>` |
| The exception **object** | The actual error that happened | `division by zero` |

```
Exception  ───  the GENERAL category "any error"  (a blueprint)
   │
   ├── ZeroDivisionError  ───  the SPECIFIC category "math errors"  (also a blueprint)
   │       │
   │       └── instance  ───  the ACTUAL error: "division by zero"
   │
   ├── ValueError
   ├── TypeError
   └── ...
```

When you write `print(Exception)`, you're printing the **blueprint**, not the actual error. It's like asking "tell me about this specific car crash" and getting back the answer "Car." Useless.

#### The Fix: Capture the Object With `as e`

```python
try:
    val = 1/0
except Exception as e:    # ← capture the actual error as 'e'
    print(e)              # ← print the OBJECT, not the class
```

**Output:**
```
division by zero
```

Now `e` is the **actual exception object** — the specific error that happened, with all its details. The name `e` is just a variable (you could call it `error`, `err`, `whatever` — `e` is convention).

#### Useful Things You Can Do With The Captured Object

```python
try:
    val = 1/0
except Exception as e:
    print(e)                       # division by zero
    print(type(e))                 # <class 'ZeroDivisionError'>
    print(type(e).__name__)        # 'ZeroDivisionError' (just the name)
    print(repr(e))                 # ZeroDivisionError('division by zero')
```

#### Side-By-Side Comparison

```python
# Version 1: Prints the blueprint — useless
except Exception:
    print(Exception)
# Output: <class 'Exception'>

# Version 2: Prints just the message
except Exception as e:
    print(e)
# Output: division by zero

# Version 3: Prints type + message — best for debugging
except Exception as e:
    print(f"{type(e).__name__}: {e}")
# Output: ZeroDivisionError: division by zero

# Version 4: Catch the specific type — best for production
except ZeroDivisionError as e:
    print(f"Math error: {e}")
# Output: Math error: division by zero
```

> **The mental model:** Class names appear in `except <ClassName>:` to say WHAT to catch. The `as e` part captures the *actual error that occurred* so you can read its details.

### 4.5 Catching Specific Exceptions

```python
# ❌ BAD — catches EVERYTHING, including bugs you should know about
try:
    risky_thing()
except:                       # naked except — hides real bugs!
    print("Something broke")

# ❌ ALSO BAD — same problem, just slightly more polite
try:
    risky_thing()
except Exception:
    print("Something broke")

# ✅ GOOD — be specific about what you expect
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a number, not text.")
```

> ⚠️ **The bare-except sin:** If you catch all errors blindly, real bugs (typos, wrong variable names) get silently swallowed. You'll spend hours wondering why your code "isn't working" when actually a different line is silently failing.

### 4.6 Multiple `except` Blocks

```python
try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
        api_key = config["api_key"]

except FileNotFoundError:
    print("config.json not found. Create one with your API key.")

except json.JSONDecodeError:
    print("config.json is malformed — check your JSON syntax.")

except KeyError:
    print("config.json is missing the 'api_key' field.")
```

**Catch multiple exceptions in ONE block:**

```python
try:
    risky_api_call()
except (TimeoutError, ConnectionError) as e:
    print(f"Network problem: {e}")
```

### 4.7 The `else` Clause

```python
try:
    response = claude_api_call(prompt)
except RateLimitError:
    print("Rate limited. Try again in a minute.")
except TimeoutError:
    print("Took too long.")
else:
    # ONLY runs if NO exception happened.
    save_to_log(response)
    print("Success!")
```

**Why use `else` instead of putting `save_to_log()` inside `try`?** Because if `save_to_log()` itself crashes, that's a different bug — you don't want to silently catch it as if it were a network error.

### 4.8 The `finally` Clause

```python
try:
    f = open("data.txt", "r")
    process(f)
except FileNotFoundError:
    print("Missing file")
finally:
    print("Cleaning up...")
    # Runs whether the try succeeded, an except handled an error,
    # or even if an UNCAUGHT error is propagating up.
```

**Use `finally` for cleanup that must always happen** — closing connections, releasing locks, deleting temp files. With `with` statements, you rarely need `finally` for files — but you'll use it for database connections, locks, etc.

### 4.9 Full Picture — `try / except / else / finally`

```python
try:
    # 1. The risky code
    response = call_claude(prompt)
except RateLimitError:
    # 2. Handle specific errors
    print("Rate limited.")
except Exception as e:
    # 3. Catch-all (use sparingly, AT THE END)
    print(f"Unexpected: {e}")
else:
    # 4. Runs only if NO error happened
    print("Success!")
    process(response)
finally:
    # 5. ALWAYS runs, no matter what
    print("Cleanup complete.")
```

### 4.10 `raise` — Throwing Your Own Errors

Sometimes you WANT your code to crash on purpose — to alert the caller that something is wrong:

```python
def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return f"Age is {age}"

process_age(-5)
# ValueError: Age cannot be negative
```

**Re-raising after logging:**

```python
try:
    risky_call()
except APIError as e:
    log_to_file(f"API failed: {e}")
    raise            # re-raises the SAME exception so the caller sees it
```

### 4.11 Custom Exception Classes

Python has built-in exceptions like `ValueError`, `KeyError`, `ZeroDivisionError`. But sometimes you need an error specific to YOUR application — something Python doesn't have.

In an AI app, you might want:
- `InvalidPromptError` — when someone sends an empty prompt
- `APIRateLimitError` — when Claude says "slow down"
- `BannedContentError` — when a prompt contains banned words

These don't exist in Python. So you **make them yourself**.

#### Step 1: The Simplest Custom Exception

```python
class InvalidPromptError(Exception):
    pass
```

Three things to notice:

1. **`class InvalidPromptError`** — defining a new class. Class names use PascalCase by convention.
2. **`(Exception)`** — this means "inherit from Exception." Your new class IS an Exception now.
3. **`pass`** — Python syntax meaning "the body is empty." We're inheriting all behavior from `Exception`.

> **Why inherit from `Exception`?** Because that's what makes Python recognize it as an "error you can `raise` and `catch`." If you write `class InvalidPromptError:` (without the `(Exception)`), Python treats it as a regular class — NOT an error.

#### Step 2: Using Your Custom Exception

```python
class InvalidPromptError(Exception):
    pass

def send_to_claude(prompt):
    if len(prompt) == 0:
        raise InvalidPromptError("Prompt cannot be empty")
    if len(prompt) > 100_000:
        raise InvalidPromptError(f"Prompt is too long: {len(prompt)} chars")
    return "Mock Claude response"

try:
    send_to_claude("")
except InvalidPromptError as e:
    print(f"Caught your custom error: {e}")
# Output: Caught your custom error: Prompt cannot be empty
```

The flow:
1. `raise InvalidPromptError("...")` creates an instance with that message and crashes the function.
2. `except InvalidPromptError as e:` catches it.
3. `e` is the instance; printing it shows the message.

#### Step 3: Why Not Just Use `ValueError`?

You CAN. But imagine your app raises `ValueError` for bad ages, bad emails, bad prompts, bad numbers — 50 different reasons. Then you can't tell them apart:

```python
try:
    send_to_claude(user_input)
except ValueError as e:
    # Was this a prompt error? Email error? Age error?
    # No way to tell except by reading the message string. Fragile!
```

With custom exceptions, each error type gets its **own specific reaction**:

```python
try:
    send_to_claude(user_input)
except InvalidPromptError as e:
    show_user("Please fix your prompt")
except APIRateLimitError as e:
    show_user("System busy, try in a minute")
except BannedContentError as e:
    show_user("That content isn't allowed")
    log_to_security_team(e)
```

> **Analogy:** A hospital with only one diagnosis ("patient is sick") is useless. Doctors need specific diagnoses (broken arm vs heart attack vs flu) to apply the right treatment. Custom exceptions are specific diagnoses for your code.

#### Step 4: Adding Extra Data To Your Custom Exception

Sometimes you want your error to carry MORE than a message — like a retry-after time:

```python
class APIRateLimitError(Exception):
    def __init__(self, message, retry_after_seconds):
        super().__init__(message)              # pass message to parent
        self.retry_after = retry_after_seconds  # store extra data

def call_claude():
    raise APIRateLimitError("Too many requests", retry_after_seconds=60)

try:
    call_claude()
except APIRateLimitError as e:
    print(f"Error: {e}")              # Too many requests
    print(f"Wait {e.retry_after}s")   # Wait 60s
    # time.sleep(e.retry_after); retry...
```

> Don't worry if `__init__`, `self`, and `super()` look unfamiliar — that's classes/OOP, your **Day 5** topic. For now, just understand the pattern.

#### Step 5: Building An Exception Hierarchy

In bigger apps, build a "family tree" of exceptions:

```python
class MyAIAppError(Exception):
    """Base class for all errors in this app."""
    pass

class InvalidPromptError(MyAIAppError):
    pass

class APIRateLimitError(MyAIAppError):
    pass

class BannedContentError(MyAIAppError):
    pass
```

Now you have flexibility:

```python
# Catch ONE specific type
except InvalidPromptError as e:
    handle_bad_prompt(e)

# OR catch ANY error from your app
except MyAIAppError as e:
    log_app_error(e)
    # This catches all three — they all inherit from MyAIAppError.
```

This is exactly how Anthropic's Python SDK is structured:

```
anthropic.APIError                    # parent
├── anthropic.APIConnectionError      # network problems
├── anthropic.RateLimitError          # 429 errors
├── anthropic.AuthenticationError     # bad API key
└── anthropic.BadRequestError         # malformed request
```

On Day 9, you'll write:

```python
try:
    response = client.messages.create(...)
except anthropic.RateLimitError as e:
    time.sleep(60)
except anthropic.APIError as e:
    log_error(e)
```

#### Try It Yourself

```python
# custom_exceptions_demo.py

class InvalidPromptError(Exception):
    """Raised when a prompt fails validation."""
    pass

class APIRateLimitError(Exception):
    """Raised when we hit the API rate limit."""
    def __init__(self, message, retry_after):
        super().__init__(message)
        self.retry_after = retry_after


def send_to_claude(prompt):
    if not prompt.strip():
        raise InvalidPromptError("Prompt cannot be empty or whitespace")
    if len(prompt) > 100_000:
        raise InvalidPromptError(f"Prompt too long: {len(prompt)} chars")
    if "BAD_WORD" in prompt:
        raise InvalidPromptError("Prompt contains banned content")
    if prompt == "trigger_rate_limit":
        raise APIRateLimitError("Rate limit hit", retry_after=30)
    return f"Mock response to: {prompt}"


# Test cases
test_cases = ["", "This contains BAD_WORD inside", "trigger_rate_limit",
              "What is the capital of France?"]

for prompt in test_cases:
    try:
        result = send_to_claude(prompt)
        print(f"✅ Success: {result}")
    except InvalidPromptError as e:
        print(f"❌ {type(e).__name__}: {e}")
    except APIRateLimitError as e:
        print(f"⏳ {type(e).__name__}: {e} (retry in {e.retry_after}s)")
```

### 4.12 Common Built-in Exceptions Cheat Sheet

| Exception | When it happens | Example trigger |
|---|---|---|
| `ValueError` | Right type, wrong value | `int("abc")` |
| `TypeError` | Wrong type entirely | `"hello" + 5` |
| `KeyError` | Dict key missing | `my_dict["missing"]` |
| `IndexError` | List index out of range | `my_list[999]` |
| `AttributeError` | Object has no such method/property | `"hello".no_such_method()` |
| `FileNotFoundError` | File doesn't exist | `open("missing.txt")` |
| `PermissionError` | OS won't let you read/write | `open("/etc/shadow")` |
| `JSONDecodeError` | Malformed JSON | `json.loads("not json")` |
| `UnicodeDecodeError` | Wrong encoding | Reading non-UTF-8 as UTF-8 |
| `ZeroDivisionError` | Divide by zero | `5 / 0` |
| `ConnectionError` | Network broke | API call with no internet |
| `TimeoutError` | Operation took too long | Slow API |
| `KeyboardInterrupt` | User pressed Ctrl+C | (don't catch this!) |

### 4.13 Real-World AI Pattern — Retry With Backoff

This is the pattern you'll use whenever you call an AI API in production:

```python
import time
import json

class APIError(Exception):
    pass

def call_claude_with_retry(prompt, max_retries=3):
    """Call Claude, retry on transient errors with increasing delays."""

    for attempt in range(1, max_retries + 1):
        try:
            response = claude_api_call(prompt)        # the actual call
            return response                            # success → done

        except (TimeoutError, ConnectionError) as e:
            # Network issues — worth retrying
            if attempt == max_retries:
                raise APIError(f"Failed after {max_retries} retries: {e}")
            wait = 2 ** attempt        # 2s, 4s, 8s — exponential backoff
            print(f"Attempt {attempt} failed ({e}). Retrying in {wait}s...")
            time.sleep(wait)

        except json.JSONDecodeError as e:
            # Malformed response — probably a service-side bug, don't retry
            raise APIError(f"Got invalid JSON from API: {e}")

        except Exception as e:
            # Anything unexpected — log and re-raise
            print(f"Unexpected error: {e}")
            raise
```

**Why this matters:** The naive version (`response = claude_api_call(prompt)`) crashes the whole app if the wifi blinks for 1 second. This version waits and retries — a much better user experience.

> You'll write a real version of this on Day 9 when you call the actual Claude API. Memorize the shape of this pattern now.

---

## Day 4 Experiment — Mini Conversation Logger

This experiment ties everything together: file reading, JSON, CSV, and error handling. Think of it as a dry run for the real Claude API logger you'll build on Day 9.

**Setup — create these files in your project folder:**

`system_prompt.txt`:
```
You are a helpful AI assistant specialized in career advice for developers
transitioning to AI engineering.
```

`questions.csv`:
```csv
id,question
1,What languages should I learn first?
2,Do I need a PhD to be an AI engineer?
3,How long does the transition take?
```

**The script — `conversation_logger.py`:**

```python
import csv
import json
from datetime import datetime
from pathlib import Path

# --- Custom exceptions ---
class ConfigError(Exception):
    pass

class DatasetError(Exception):
    pass

# --- Step 1: Load the system prompt ---
def load_system_prompt(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        raise ConfigError(f"System prompt not found at {path}")

# --- Step 2: Load questions from CSV ---
def load_questions(path: Path) -> list[dict]:
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            questions = [row for row in reader]
        if not questions:
            raise DatasetError("Questions file is empty")
        return questions
    except FileNotFoundError:
        raise DatasetError(f"Questions file not found at {path}")

# --- Step 3: Fake "AI" response (we'll replace with real Claude on Day 9) ---
def fake_ai_response(prompt: str) -> str:
    return f"[Mock response to: '{prompt[:50]}...']"

# --- Step 4: Log results in JSONL format ---
def log_interaction(log_path: Path, entry: dict) -> None:
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

# --- Main flow ---
def main():
    base = Path(__file__).parent
    system_prompt_path = base / "system_prompt.txt"
    questions_path = base / "questions.csv"
    log_path = base / "conversation_log.jsonl"

    try:
        system_prompt = load_system_prompt(system_prompt_path)
        questions = load_questions(questions_path)
    except (ConfigError, DatasetError) as e:
        print(f"Setup failed: {e}")
        return

    print(f"Loaded {len(questions)} questions. Processing...\n")

    for q in questions:
        try:
            qid = int(q["id"])
            question_text = q["question"]
        except (ValueError, KeyError) as e:
            print(f"Skipping malformed row {q}: {e}")
            continue

        try:
            answer = fake_ai_response(question_text)
        except Exception as e:
            print(f"AI call failed for Q{qid}: {e}")
            continue

        entry = {
            "timestamp": datetime.now().isoformat(),
            "id": qid,
            "system_prompt": system_prompt,
            "question": question_text,
            "answer": answer,
        }
        log_interaction(log_path, entry)
        print(f"Q{qid}: {question_text}")
        print(f"   → {answer}\n")

    print(f"Done. Log written to: {log_path}")

if __name__ == "__main__":
    main()
```

**What this script demonstrates:**

| Concept from Day 4 | Where it appears |
|---|---|
| `pathlib.Path` | Building file paths |
| Reading text files (`read_text`) | Loading the system prompt |
| `csv.DictReader` | Reading questions |
| `json.dumps` + JSONL | Writing log entries |
| Custom exceptions | `ConfigError`, `DatasetError` |
| Specific `except` blocks | Different errors handled differently |
| `try / except / continue` | Skipping bad rows without crashing |
| UTF-8 everywhere | All file opens use `encoding="utf-8"` |
| `with` statement | All file operations |

**Bonus challenges:**
1. Add a CLI flag to choose between `--mock` and `--live` (Day 9 preview).
2. Compute total tokens used (mock for now: `len(answer.split())`).
3. Read previous `conversation_log.jsonl` and skip questions already answered (cache!).
4. Rotate the log file when it exceeds 1 MB (`os.path.getsize` + rename).
5. Wrap `fake_ai_response` in the retry-with-backoff pattern from §4.13.

---

## Common Pitfalls I Hit

These are real bugs I ran into during Day 4 — documented so future-me doesn't repeat them.

#### Pitfall 1: Markdown Auto-Linking on Copy-Paste

When copying code from chat or docs, file names with dots can get rendered as clickable links and pasted as markdown:

```python
# What I pasted:
content = [file.read](http://file.read)()
# What I meant:
content = file.read()
```

```bash
# What I pasted:
python [main.py](http://main.py)
# What I meant:
python main.py
```

**Fix:** Watch for `[...]` and `(http://...)` wrapping in pasted code — strip them out and type the actual code.

#### Pitfall 2: Printing the Class Instead of the Error Object

```python
try:
    val = 1/0
except Exception:
    print(Exception)         # <class 'Exception'> — useless
    # Need: except Exception as e: print(e)  → "division by zero"
```

#### Pitfall 3: Forgetting `encoding="utf-8"`

Code worked on Windows, broke on Linux deployment when the file contained an emoji. Always pass `encoding="utf-8"` explicitly. Always.

#### Pitfall 4: Forgetting `newline=""` on CSV

Got blank rows between every entry when Excel opened my CSV. Fix is always `newline=""` — both for read and write.

#### Pitfall 5: Treating `row["age"]` as a Number

`csv.DictReader` returns ALL values as strings. `row["age"] + 1` crashes with `TypeError`. Convert: `int(row["age"]) + 1`.

#### Pitfall 6: Bare `except:` Hiding Bugs

```python
# This swallowed a typo in my variable name for 30 minutes
try:
    do_thing()
except:
    print("something broke")
```

Always catch specific exception types. If you must catch broadly, at least use `except Exception as e: print(e)` so you SEE what went wrong.

---

## Day 4 Cheat Sheet

### File I/O
```python
# Always: with + encoding="utf-8"
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()                         # everything as one string
    # for line in f: ...                       # line-by-line (for big files)

with open("file.txt", "w", encoding="utf-8") as f:
    f.write("text\n")                          # remember \n!

with open("file.txt", "a", encoding="utf-8") as f:
    f.write("new line\n")                      # append, never overwrites

# pathlib (modern way)
from pathlib import Path
path = Path("data") / "file.txt"
path.exists()                                  # check first
text = path.read_text(encoding="utf-8")
path.write_text("hello", encoding="utf-8")
```

### CSV
```python
import csv

# Read
with open("data.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["column_name"])              # row is a dict (all strings!)

# Read with custom delimiter (TSV, European CSV)
csv.reader(f, delimiter="\t")                  # tab-separated
csv.reader(f, delimiter=";")                   # semicolon-separated

# Read file with NO header
csv.DictReader(f, fieldnames=["name", "age"])  # provide your own names

# Handle missing values
salary = int(row.get("salary", "") or "0")     # missing key OR empty string

# Write
with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["a", "b"])
    writer.writeheader()
    writer.writerows([{"a": 1, "b": 2}])
```

### JSON
```python
import json

# Read
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)                        # file → dict
data = json.loads('{"x": 1}')                  # string → dict

# Write
with open("out.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
text = json.dumps(data, indent=2, ensure_ascii=False)

# JSONL (line-by-line, for big AI datasets)
with open("data.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        record = json.loads(line)

with open("data.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(record, ensure_ascii=False) + "\n")
```

### Error Handling
```python
try:
    risky_thing()
except SpecificError as e:           # specific first, capture object as e
    handle(e)
except (ErrorA, ErrorB):             # group related
    ...
except Exception as e:               # broad catch (last)
    log(e)
    raise                            # re-raise if needed
else:
    # only runs if no exception
    success()
finally:
    # ALWAYS runs
    cleanup()
```

### Custom Exception
```python
# Simplest form
class MyError(Exception):
    pass

# With extra data
class APIRateLimitError(Exception):
    def __init__(self, message, retry_after):
        super().__init__(message)
        self.retry_after = retry_after

# Use them
raise MyError("Something specific went wrong")

try:
    do_stuff()
except MyError as e:
    handle(e)
```

### AI Engineer's Default File Open
```python
# Memorize this — it's the pattern for 90% of file operations
with open(path, MODE, encoding="utf-8") as f:
    ...
# MODE: "r" read, "w" write (overwrites!), "a" append
# For binary (PDFs, images): mode="rb" or "wb", drop encoding
# For CSVs: also add newline=""
```

---

> **Note to future me:** When you build your first real AI app (Day 15+), come back to §4.13 — the retry-with-backoff pattern. It's the difference between a demo and a product. Also remember: every file open should have `encoding="utf-8"` and use `with`. No exceptions.

> **The big lesson of Day 4:** Files persist data between runs. Errors happen constantly when talking to networks and APIs. These two skills — saving state to disk, and recovering from failures — are what turn a script into software.



### Day 5 — Object-Oriented Programming (OOP)

> **Goal:** Understand how to structure code using classes — the foundation of every AI library you'll touch. `anthropic.Anthropic()`, `ChatOpenAI()`, `FastAPI()`, `BaseModel` from Pydantic — these are ALL classes. Before today, you USED classes. After today, you'll BUILD them.

#### Why OOP Matters for AI Engineering

Look at any real AI code:

```python
import anthropic

client = anthropic.Anthropic()              # Creating an OBJECT from the Anthropic CLASS
response = client.messages.create(...)      # Calling a METHOD on the object
print(response.content[0].text)             # Accessing ATTRIBUTES of the response object
```

Every line above uses OOP. You cannot:
- Read AI library source code without understanding classes
- Build clean AI apps (agents, RAG systems, tool registries) without classes
- Use frameworks like LangChain, FastAPI, Pydantic without OOP

**Power Platform parallel:** Think of a Copilot Studio agent. It has properties (name, instructions), behaviors (responds to messages, calls actions), and you can create multiple instances (different agents for different teams). Classes are the same idea in code — a blueprint that defines what something IS and what it can DO, and you can stamp out many copies.

---

#### 1. Classes and Objects — Blueprints vs. Things

**Class = the blueprint. Object (instance) = the thing built from the blueprint.**

| Real World | Code |
|---|---|
| Architectural blueprint of a house | `class House:` |
| Actual house built from the blueprint | `my_house = House()` |
| Another house from the same blueprint | `your_house = House()` |

Both `my_house` and `your_house` are SEPARATE objects — different addresses, different paint colors — but they share the same structure (rooms, doors, roof) defined by the class.

```python
class AIModel:
    pass    # 'pass' = "empty for now, don't error"

# Creating objects (instances) from the class
gpt = AIModel()         # Object 1
claude = AIModel()      # Object 2

print(type(gpt))        # <class '__main__.AIModel'>
print(gpt is claude)    # False — different objects in memory
```

**Convention:** Class names use `PascalCase` (`AIModel`, `ModelRegistry`), variables use `snake_case` (`gpt_model`). Enforced by every Python codebase.

---

#### 2. `__init__` and `self` — The Constructor

A class with `pass` is useless. We need to give each object its own data. That's what `__init__` does.

```python
class AIModel:
    def __init__(self, name, version, accuracy):
        self.name = name
        self.version = version
        self.accuracy = accuracy

claude = AIModel("Claude", "Opus 4.7", 0.95)
gpt = AIModel("GPT", "4o", 0.92)

print(claude.name)       # "Claude"
print(gpt.accuracy)      # 0.92
```

**What is `__init__`?** A special method Python calls AUTOMATICALLY when you create an object. It "initializes" the object with starting values. The double underscores (`__`) mean "this is a Python magic method — don't call it directly, Python calls it for you."

**What is `self`?** This is THE most confusing thing about Python OOP. Three explanations:

**(a) `self` means "this specific object":**
```python
claude = AIModel("Claude", "Opus 4.7", 0.95)
# When __init__ runs:
#   self  →  refers to claude (the object being built)
#   name  →  "Claude"
# So self.name = name  →  claude.name = "Claude"
```

**(b) `self` is how you store data ON the object:**
```python
def __init__(self, name):
    name = name           # ❌ Just a local variable, lost when __init__ ends
    self.name = name      # ✅ Saved to the object permanently
```

**(c) `self` is automatic — you never pass it:**
```python
claude = AIModel("Claude", "Opus 4.7", 0.95)
#                  ↑          ↑           ↑
#                 name     version    accuracy
# Python AUTOMATICALLY passes 'self' behind the scenes
```

> ⚠️ **Common mistakes that confused me when I started:**
> - Forgetting `self` in method definitions: `def add_model(name):` instead of `def add_model(self, name):`
> - Forgetting to use `self.` to store: writing `name = name` instead of `self.name = name`
> - Forgetting to use `self.` to access: writing `print(name)` instead of `print(self.name)`

---

#### 3. Instance Attributes vs. Class Attributes

Two places to store data — and the difference matters:

```python
class AIModel:
    company = "Various"              # CLASS attribute — shared by ALL instances
    
    def __init__(self, name, accuracy):
        self.name = name             # INSTANCE attribute — unique per object
        self.accuracy = accuracy

claude = AIModel("Claude", 0.95)
gpt = AIModel("GPT", 0.92)

print(claude.name, gpt.name)         # "Claude" "GPT"     — different (instance)
print(claude.company, gpt.company)   # "Various" "Various" — same (class)

AIModel.company = "AI Inc"           # changing class attribute affects everyone:
print(claude.company, gpt.company)   # "AI Inc" "AI Inc"
```

**Use class attributes for:** constants, defaults, counters spanning all instances.
**Use instance attributes for:** anything unique to each object (the 99% case).

> ⚠️ **The mutable class attribute trap** — bites every Python beginner exactly once:
> ```python
> # ❌ WRONG — every registry shares the SAME list
> class ModelRegistry:
>     models = []    # class attribute — shared across all instances!
> 
> r1 = ModelRegistry()
> r2 = ModelRegistry()
> r1.models.append("Claude")
> print(r2.models)    # ["Claude"] — wait, what?! r2 has it too!
> 
> # ✅ RIGHT — each registry gets its own list
> class ModelRegistry:
>     def __init__(self):
>         self.models = []    # instance attribute — unique per object
> ```

---

#### 4. The Three Method Flavors — Instance, Class, Static

You'll see all three in real AI code. Here's the full picture in one example:

```python
class AIModel:
    total_count = 0    # CLASS attribute (shared by all instances)
    
    def __init__(self, name):
        self.name = name
        AIModel.total_count += 1
    
    # 1. INSTANCE method — needs an object, gets `self`
    def describe(self):
        return f"I am {self.name}"
    
    # 2. CLASS method — gets `cls` (the class itself)
    #    Can access/modify class attributes. Can create new instances.
    @classmethod
    def get_count(cls):
        return cls.total_count                  # ✅ read class attribute
    
    @classmethod
    def reset_counter(cls):
        cls.total_count = 0                     # ✅ MODIFY class attribute
    
    @classmethod
    def from_string(cls, text):
        name = text.split(":")[0]
        return cls(name)                        # ✅ CREATE a new instance!
    
    # 3. STATIC method — gets NOTHING (no self, no cls)
    #    Cannot access class or instance data. Just a utility.
    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 0
```

**The hierarchy of access:**

| Method type | Can access `self.x`? | Can access `cls.x`? | Can create new instances? |
|---|---|---|---|
| Instance method | ✅ Yes | ✅ Yes (via `self.__class__.x`) | ✅ Yes |
| `@classmethod` | ❌ No | ✅ Yes | ✅ Yes |
| `@staticmethod` | ❌ No | ❌ No | ❌ Not really |

**When to use each — the practical rule:**

- **Instance method** → 99% of the time. Anything that uses an object's data.
- **`@classmethod`** → "Alternative constructors." This is the killer use case. You'll see it everywhere in AI libraries:
  ```python
  model = AIModel.from_dict(json_data)        # alternative way to construct
  model = AIModel.from_pretrained("claude-3") # ← this is exactly how HuggingFace works!
  tokenizer = Tokenizer.from_file("vocab.txt")
  ```
- **`@staticmethod`** → A helper that logically belongs in the class but doesn't need any class/instance data. Use sparingly — you can usually just write a regular function instead.

**Calling them:**
```python
AIModel.get_count()         # Normal — class methods belong to the class
claude = AIModel("Claude")
claude.get_count()          # Also works, but unusual style
```

---

#### 5. `@property` and `@setter` — Smart Attributes

**The problem they solve:** A regular attribute lets anyone do this:

```python
claude.accuracy = 9999       # 😱 nonsense value, but no error
claude.accuracy = "banana"   # 😱 totally wrong type, no error
```

You have NO way to validate. In Java/C++, you'd write getter/setter methods:

```java
// Java/C++ style — UGLY to use
class AIModel {
    private double accuracy;
    public double getAccuracy() { return accuracy; }
    public void setAccuracy(double v) { 
        if (v < 0 || v > 1) throw...;
        this.accuracy = v;
    }
}
// Usage:
model.setAccuracy(0.9);          // verbose
double a = model.getAccuracy();  // verbose
```

Python's `@property` lets you keep the **clean syntax** `model.accuracy = 0.9` BUT **secretly run validation code** behind the scenes:

```python
class AIModel:
    def __init__(self, accuracy):
        self.accuracy = accuracy   # ← this actually calls the SETTER below!
    
    @property
    def accuracy(self):
        # This runs when someone READS  →  print(model.accuracy)
        return self._accuracy
    
    @accuracy.setter
    def accuracy(self, value):
        # This runs when someone WRITES →  model.accuracy = 0.9
        if not 0 <= value <= 1:
            raise ValueError(f"Accuracy must be 0-1, got {value}")
        self._accuracy = value


claude = AIModel(0.95)        # Setter runs! _accuracy = 0.95
print(claude.accuracy)        # Getter runs! → 0.95
claude.accuracy = 0.92        # Setter runs! validates, then _accuracy = 0.92
claude.accuracy = 5.0         # Setter runs! → ValueError
```

**Why two functions named `accuracy`?** The decorators tell Python what each is for:
- `@property` on top → "this function runs when reading"
- `@accuracy.setter` on top → "this function runs when writing"

Python links them by name — that's why both are called `accuracy`.

**Why store it in `self._accuracy` (with underscore) instead of `self.accuracy`?**

If you wrote `self.accuracy = value` inside the setter, it would trigger the setter AGAIN — infinite loop, crash. So convention: the public smart attribute is `accuracy`, and the actual storage hides in `_accuracy`.

```
User writes:    model.accuracy = 0.9
                       ↓
                 Triggers setter
                       ↓
              Validates, stores in self._accuracy
                       ↓
User reads:     print(model.accuracy)
                       ↓
                 Triggers getter
                       ↓
              Returns self._accuracy
```

**Computed properties — read-only, no setter:**

```python
class AIModel:
    def __init__(self, accuracy):
        self._accuracy = accuracy
    
    @property
    def grade(self):
        """Computed on the fly — no _grade variable exists."""
        if self._accuracy >= 0.95: return "A"
        if self._accuracy >= 0.85: return "B"
        return "C"

claude = AIModel(0.95)
print(claude.grade)     # "A" — looks like an attribute, runs as a function
# claude.grade = "F"    # AttributeError — no setter defined, so read-only
```

**Why this matters for AI:** Pydantic — the library every AI engineer uses for API request/response schemas — is built entirely on this validation pattern.

---

#### 6. Built-in Exceptions Are Classes Too

When you write:

```python
raise TypeError("Expected AIModel")
```

`TypeError` IS a class — a built-in one Python provides. The line does TWO things:

1. **Creates an instance** of `TypeError` with message `"Expected AIModel"`
2. **`raise`s** that instance — crashing the program with that error

It's the same as:
```python
error_object = TypeError("Expected AIModel")    # create the object
raise error_object                                # raise it
```

Python ships with dozens of built-in exception classes:

| Built-in class | Used when |
|---|---|
| `TypeError` | Wrong type (string when expected int, etc.) |
| `ValueError` | Right type, but bad value (`int("hello")`) |
| `KeyError` | Dictionary key doesn't exist |
| `IndexError` | List index out of range |
| `AttributeError` | Object has no such attribute |
| `FileNotFoundError` | File doesn't exist |

You can even **make your own** by inheriting from `Exception`:

```python
class ModelNotFoundError(Exception):    # inherits from built-in Exception class
    pass

raise ModelNotFoundError("Claude not in registry")
```

So everything you've been seeing — `TypeError`, `ValueError` — they're all classes Python defined for you. You're using OOP whether you knew it or not.

---

#### 7. Access Modifiers — Python vs C++/Java

**C++/Java have STRICT access modifiers** enforced by the compiler:

```cpp
// C++
class AIModel {
public:
    string name;        // anyone can access
protected:
    double accuracy;    // only this class AND child classes
private:
    string apiKey;      // ONLY this class — not even children!
};

class LLMModel : public AIModel {
    void test() {
        name = "x";       // ✅ allowed (public)
        accuracy = 0.9;   // ✅ allowed (protected, child class)
        apiKey = "key";   // ❌ COMPILE ERROR (private, child can't see)
    }
};
```

In C++/Java the compiler **physically prevents** you from accessing private members. Code won't compile.

**Python's philosophy is different.** Guido van Rossum (Python's creator) famously said: *"We're all consenting adults here."* Python uses **CONVENTION**, not enforcement:

| Python style | Meaning | Enforced? |
|---|---|---|
| `self.name` | Public | N/A |
| `self._name` | "Protected" — please don't touch from outside | ❌ NOT enforced — just a hint |
| `self.__name` | "Private" — name-mangled | ⚠️ Partially — see below |

**Demo of the difference:**

```python
class MyClass:
    def __init__(self):
        self.public_var = 1
        self._protected_var = 2     # single underscore: convention only
        self.__private_var = 3      # double underscore: NAME MANGLING happens

obj = MyClass()

print(obj.public_var)         # ✅ 1 — works
print(obj._protected_var)     # ✅ 2 — works! Python doesn't actually stop you
                              #    (the underscore is just a "please don't" sign)

print(obj.__private_var)      # ❌ AttributeError!
```

Why does the double-underscore one fail? Because **Python silently renamed it**:

```python
print(obj.__dict__)
# {'public_var': 1, '_protected_var': 2, '_MyClass__private_var': 3}
#                                          ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
#                                          Python renamed it!

print(obj._MyClass__private_var)    # ✅ 3 — works with the mangled name
```

This is called **name mangling**. Python takes `__private_var` and renames it to `_ClassName__private_var`. Not real privacy — anyone can still access it — but it makes accidental access in inheritance unlikely.

**The full naming convention table:**

| Pattern | Name | What Python does | When to use |
|---|---|---|---|
| `name` | Public | Nothing — fully exposed | Default for everything |
| `_name` | "Protected" | Nothing — convention only | "Please don't touch from outside" |
| `__name` | "Private" | Name mangling (`_Class__name`) | Avoid accidental access in subclasses |
| `__name__` | Magic / dunder | Special meaning to Python | DON'T make your own |

> ⚠️ **Don't use `__double_underscore` casually.** It causes more problems than it solves. In real Python code, single underscore (`_name`) is used 99% of the time. Double underscore is reserved for specific name-collision problems in complex inheritance.

---

#### 8. Inheritance — Reusing and Extending Classes

> **The single most powerful idea in OOP.** A class can INHERIT from another — getting all attributes/methods for free, then adding/overriding what's different.

```python
class AIModel:                                    # PARENT class
    def __init__(self, name, version, accuracy):
        self.name = name
        self.version = version
        self.accuracy = accuracy
    
    def describe(self):
        return f"{self.name} {self.version}"

class LLMModel(AIModel):                          # CHILD inherits from AIModel
    def __init__(self, name, version, accuracy, context_window, parameter_count):
        super().__init__(name, version, accuracy) # Call PARENT'S __init__ first
        self.context_window = context_window      # Add NEW attributes
        self.parameter_count = parameter_count
    
    def describe(self):                           # OVERRIDE the parent's method
        base = super().describe()                  # Call parent's version, add to it
        return f"{base} [LLM, context: {self.context_window:,} tokens]"

claude = LLMModel("Claude", "Opus 4.7", 0.95, 200000, 175_000_000_000)

print(claude.name)                # "Claude"     ← inherited from AIModel
print(claude.context_window)      # 200000       ← LLMModel's own attribute
print(claude.describe())          # "Claude Opus 4.7 [LLM, context: 200,000 tokens]"

print(isinstance(claude, LLMModel))   # True
print(isinstance(claude, AIModel))    # True — an LLMModel IS-A AIModel
```

**`super()` explained:** Calls the parent class's version of a method. Three reasons to use it:

1. **In `__init__`:** `super().__init__(...)` runs the parent's setup. Always do this when you have your own `__init__`.
2. **In overridden methods:** Run parent's logic, then add your own (the `describe()` example).
3. **Safer than calling parent by name** (`AIModel.__init__(self, ...)` works but breaks if you rename or change inheritance).

**The IS-A test — when to use inheritance:**
- ✅ "An LLMModel IS-A AIModel" → inheritance works
- ❌ "A ModelRegistry IS-A AIModel" → NO! A registry HAS-A bunch of models. Use composition.

> ⚠️ **Don't overuse inheritance.** Beginners reach for it constantly. Real Python codebases prefer **composition** ("class A has-a class B" — store B inside A) over deep inheritance trees.

---

#### 9. Inheritance Patterns — Many Ways to Inherit

Parent → child is just the simplest. Python supports several patterns:

##### (a) Single inheritance
```python
class AIModel: pass
class LLMModel(AIModel): pass        # one parent, one child
```

##### (b) Multilevel (grandparent → parent → child)
```python
class AIModel: pass
class LLMModel(AIModel): pass
class ChatModel(LLMModel): pass      # ChatModel gets EVERYTHING from both
```

`ChatModel` inherits from `LLMModel`, which inherits from `AIModel`. Real example: `torch.nn.Module → torch.nn.Linear → YourCustomLayer`.

##### (c) Hierarchical (one parent → multiple children)
```python
class AIModel: pass
class LLMModel(AIModel): pass        # sibling 1
class VisionModel(AIModel): pass     # sibling 2
class AudioModel(AIModel): pass      # sibling 3
```

All children share `AIModel`'s functionality but specialize differently. **Extremely common.**

##### (d) Multiple inheritance (multiple parents → one child)

Python supports this. Java doesn't (forbidden). C++ does (carefully).

```python
class Trainable:
    def train(self):
        print("Training...")

class Serializable:
    def save(self, path):
        print(f"Saving to {path}")

class AIModel(Trainable, Serializable):    # inherits from BOTH!
    pass

claude = AIModel()
claude.train()        # ✅ from Trainable
claude.save("file")   # ✅ from Serializable
```

This is called the **mixin pattern** — used heavily in Django, PyTorch, scikit-learn. Each parent adds a small "capability" like clip-on tools.

##### (e) Diamond inheritance (the tricky one)

```python
class A:
    def hello(self): print("A")

class B(A):
    def hello(self): print("B")

class C(A):
    def hello(self): print("C")

class D(B, C): pass       # D inherits from BOTH B and C, both inherit from A
                          # Diamond shape:    A
                          #                  / \
                          #                 B   C
                          #                  \ /
                          #                   D

d = D()
d.hello()                 # Which one runs? B's or C's?
```

Famous **diamond problem**. Python solves it using **MRO (Method Resolution Order)** — a deterministic algorithm called C3 linearization:

```python
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)
# d.hello() prints "B" — Python searches D → B → C → A
```

C++ requires manual disambiguation. Java just **forbids** multiple inheritance to avoid this whole mess.

##### Summary of inheritance patterns

| Pattern | Diagram | Python | Java | C++ |
|---|---|---|---|---|
| Single | A → B | ✅ | ✅ | ✅ |
| Multilevel | A → B → C | ✅ | ✅ | ✅ |
| Hierarchical | A → B, A → C | ✅ | ✅ | ✅ |
| Multiple | A, B → C | ✅ | ❌ (use interfaces) | ✅ |
| Diamond | A → B,C → D | ✅ (MRO handles it) | ❌ | ⚠️ (manual) |

---

#### 10. Magic Methods (Dunder Methods) — `__str__`, `__repr__`

"Magic methods" or "dunder methods" (double underscore on BOTH sides) are methods Python calls automatically in specific situations. You've already met `__init__`.

The two most important ones for daily use:

```python
class AIModel:
    def __init__(self, name, version, accuracy):
        self.name = name
        self.version = version
        self.accuracy = accuracy

claude = AIModel("Claude", "Opus 4.7", 0.95)
print(claude)        # <__main__.AIModel object at 0x000001E8...> — useless!
```

That ugly default output is what you get without `__str__` and `__repr__`. Fix it:

```python
class AIModel:
    def __init__(self, name, version, accuracy):
        self.name = name
        self.version = version
        self.accuracy = accuracy
    
    def __str__(self):
        """Friendly version — for end users. Used by print() and str()."""
        return f"{self.name} {self.version}"
    
    def __repr__(self):
        """Developer version — for debugging. Used in REPL, lists, errors."""
        return f"AIModel(name='{self.name}', version='{self.version}', accuracy={self.accuracy})"

claude = AIModel("Claude", "Opus 4.7", 0.95)

print(claude)        # "Claude Opus 4.7"           ← __str__ is used here
str(claude)          # "Claude Opus 4.7"           ← __str__

repr(claude)         # "AIModel(name='Claude', ...)" ← __repr__
[claude]             # [AIModel(name='Claude', ...)] ← lists use __repr__ for items
```

**The rule:** `__str__` is for humans (readable). `__repr__` is for developers (precise, ideally something you could paste back into Python to recreate the object). When in doubt, define BOTH. If you only define one, define `__repr__` — Python falls back to it when `__str__` is missing.

**Other magic methods worth knowing exist** (`__eq__` for `==`, `__lt__` for `<`, `__len__` for `len()`, `__getitem__` for `obj[key]`) — you'll meet them when you need them. For now, master `__init__`, `__str__`, `__repr__`.

---

#### Quick Mental Model — The Whole Picture

```
┌──────────────────────────────────────────────────────────┐
│  CLASS = Blueprint                                       │
│                                                          │
│  class AIModel:                                          │
│      company = "Anthropic"        ← class attribute      │
│                                                          │
│      def __init__(self, name):    ← constructor          │
│          self.name = name         ← instance attribute   │
│                                                          │
│      def describe(self):          ← instance method      │
│          return self.name                                │
│                                                          │
│      @classmethod                                        │
│      def from_dict(cls, d): ...   ← alt constructor      │
│                                                          │
│      @staticmethod                                       │
│      def is_valid(x): ...         ← utility              │
│                                                          │
│      @property                                           │
│      def grade(self): ...         ← computed property    │
│                                                          │
│      def __str__(self): ...       ← magic method         │
│                                                          │
└──────────────────────────────────────────────────────────┘
                         │
                         │  AIModel("Claude")  →  creates object
                         ▼
┌──────────────────────────────────────────────────────────┐
│  OBJECT (Instance)                                       │
│                                                          │
│  claude.name = "Claude"                                  │
│  claude.company = "Anthropic"  (from class)              │
│  claude.describe()  →  "Claude"                          │
│  print(claude)  →  triggers __str__                      │
│                                                          │
└──────────────────────────────────────────────────────────┘

         │  class LLMModel(AIModel):  →  inherits everything
         ▼
┌──────────────────────────────────────────────────────────┐
│  CHILD CLASS (Inherits + Extends)                        │
│                                                          │
│  Has everything AIModel has, PLUS:                       │
│    - context_window                                      │
│    - parameter_count                                     │
│    - overridden describe() with extra info               │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

#### Day 5 Experiment — AI Model Registry

> **Goal:** Build a system that manages a catalog of AI models. This same pattern is how LangChain manages LLM providers, how FastAPI manages routes, and how every "registry" or "manager" class works in real code.

```python
# ai_model_registry.py

class AIModel:
    """A generic AI model in our registry."""
    
    def __init__(self, name, version, accuracy, framework):
        self.name = name
        self.version = version
        self._accuracy = accuracy        # protected, validated via property
        self.framework = framework       # e.g., "PyTorch", "TensorFlow", "JAX"
    
    @property
    def accuracy(self):
        return self._accuracy
    
    @accuracy.setter
    def accuracy(self, value):
        if not 0 <= value <= 1:
            raise ValueError(f"Accuracy must be between 0 and 1, got {value}")
        self._accuracy = value
    
    @property
    def grade(self):
        if self._accuracy >= 0.95: return "A"
        if self._accuracy >= 0.85: return "B"
        if self._accuracy >= 0.75: return "C"
        return "D"
    
    def is_production_ready(self):
        return self._accuracy >= 0.90
    
    def __str__(self):
        return f"{self.name} {self.version} ({self.framework}, grade {self.grade})"
    
    def __repr__(self):
        return (f"AIModel(name='{self.name}', version='{self.version}', "
                f"accuracy={self._accuracy}, framework='{self.framework}')")


class LLMModel(AIModel):
    """A Large Language Model — a specialized AIModel with extra attributes."""
    
    def __init__(self, name, version, accuracy, framework, 
                 context_window, parameter_count):
        super().__init__(name, version, accuracy, framework)
        self.context_window = context_window     # tokens
        self.parameter_count = parameter_count   # number of parameters
    
    def estimate_memory_gb(self):
        """Rough estimate: 2 bytes per parameter (FP16) → GB."""
        return (self.parameter_count * 2) / (1024 ** 3)
    
    def __str__(self):
        base = super().__str__()
        return f"{base} | context: {self.context_window:,} tokens"
    
    def __repr__(self):
        return (f"LLMModel(name='{self.name}', version='{self.version}', "
                f"accuracy={self._accuracy}, framework='{self.framework}', "
                f"context_window={self.context_window}, "
                f"parameter_count={self.parameter_count})")


class ModelRegistry:
    """A registry that stores and manages multiple AIModel objects."""
    
    def __init__(self, name="Default Registry"):
        self.name = name
        self._models = []                # composition: registry HAS-A list of models
    
    def add_model(self, model):
        """Add a model to the registry."""
        if not isinstance(model, AIModel):
            raise TypeError(f"Expected AIModel, got {type(model).__name__}")
        self._models.append(model)
        print(f"✅ Added: {model}")
    
    def get_best_model(self):
        """Return the model with the highest accuracy."""
        if not self._models:
            return None
        return max(self._models, key=lambda m: m.accuracy)
    
    def list_models_by_framework(self, framework):
        """Return all models that use a specific framework."""
        return [m for m in self._models if m.framework.lower() == framework.lower()]
    
    def list_production_ready(self):
        """Return only models with accuracy >= 0.90."""
        return [m for m in self._models if m.is_production_ready()]
    
    def __len__(self):
        """Now len(registry) works!"""
        return len(self._models)
    
    def __str__(self):
        return f"{self.name} ({len(self._models)} models)"


# ─────────── DEMO ───────────
if __name__ == "__main__":
    registry = ModelRegistry("Smadavaram's AI Catalog")
    
    # Add some general AI models
    registry.add_model(AIModel("ResNet", "50", 0.93, "PyTorch"))
    registry.add_model(AIModel("YOLOv8", "x", 0.91, "PyTorch"))
    registry.add_model(AIModel("BERT", "base", 0.88, "TensorFlow"))
    
    # Add some LLMs (using the child class)
    registry.add_model(LLMModel("Claude", "Opus 4.7", 0.96, "PyTorch",
                                context_window=200_000,
                                parameter_count=175_000_000_000))
    registry.add_model(LLMModel("Llama", "3.1", 0.92, "PyTorch",
                                context_window=128_000,
                                parameter_count=70_000_000_000))
    
    print(f"\n📊 Registry: {registry}")
    print(f"   Total models: {len(registry)}")
    
    print(f"\n🏆 Best model: {registry.get_best_model()}")
    
    print(f"\n🔥 PyTorch models:")
    for m in registry.list_models_by_framework("PyTorch"):
        print(f"   - {m}")
    
    print(f"\n🚀 Production-ready models (accuracy >= 0.90):")
    for m in registry.list_production_ready():
        print(f"   - {m}")
    
    # Demonstrating polymorphism — same method call, different behavior
    print(f"\n🧬 Polymorphism demo (each model describes itself):")
    for m in registry._models:
        print(f"   {m}")    # AIModels print short, LLMModels print with context
```

**Expected output:**
```
✅ Added: ResNet 50 (PyTorch, grade B)
✅ Added: YOLOv8 x (PyTorch, grade B)
✅ Added: BERT base (TensorFlow, grade B)
✅ Added: Claude Opus 4.7 (PyTorch, grade A) | context: 200,000 tokens
✅ Added: Llama 3.1 (PyTorch, grade B) | context: 128,000 tokens

📊 Registry: Smadavaram's AI Catalog (5 models)
   Total models: 5

🏆 Best model: Claude Opus 4.7 (PyTorch, grade A) | context: 200,000 tokens

🔥 PyTorch models:
   - ResNet 50 (PyTorch, grade B)
   - YOLOv8 x (PyTorch, grade B)
   - Claude Opus 4.7 (PyTorch, grade A) | context: 200,000 tokens
   - Llama 3.1 (PyTorch, grade B) | context: 128,000 tokens
```

**What this experiment teaches:**
- `AIModel` and `LLMModel` show **inheritance** — LLMs reuse all AIModel logic.
- `super().__init__()` and `super().__str__()` show **calling parent methods**.
- `@property` on `accuracy` shows **validation**.
- `@property` on `grade` shows **computed attributes**.
- `ModelRegistry` shows **composition** (HAS-A list of models, NOT inheritance).
- `__str__` and `__repr__` show **clean output**.
- `__len__` shows magic methods power Python built-ins.
- The polymorphism loop shows the magic of OOP — same method call, different behavior depending on actual class.

---

#### Bonus Challenges

1. **Add a `VisionModel(AIModel)` child class** with extra attributes `input_resolution` (tuple like `(224, 224)`) and `num_classes`. Override `__str__` to include the resolution.
2. **Add a `remove_model(name)` method** to `ModelRegistry` that removes a model by name and returns `True` if found, `False` otherwise.
3. **Add a `save_to_dict()` method** to `AIModel` that returns a dictionary of all attributes — this is the pattern used everywhere when serializing to JSON for APIs.
4. **Add a `from_dict(data)` class method** using `@classmethod` that creates an `AIModel` from a dictionary. This is an "alternative constructor."
5. **Implement `__eq__`** so two models with the same name and version are considered equal: `claude_v1 == claude_v1_copy` returns `True`.
6. **Make `ModelRegistry` iterable** by adding `__iter__` so you can write `for model in registry:` instead of `for model in registry._models:`.

---

#### Common OOP Pitfalls (Things That Will Bite You)

| Mistake | What Happens | Fix |
|---|---|---|
| Forgetting `self` in method definition | `TypeError: missing 1 required argument` | Always: `def method(self, ...)` |
| Forgetting `self.` when storing | Data lost when method ends | `self.x = value`, not `x = value` |
| Forgetting `super().__init__()` in child class | Parent's attributes never set, `AttributeError` later | First line of child `__init__` |
| Mutable class attributes | All instances share the SAME list! | Use `self.items = []` in `__init__`, not `items = []` at class level |
| Overusing inheritance | Brittle, deep hierarchies | Use composition ("HAS-A") when in doubt |
| Defining only `__str__`, not `__repr__` | Lists/debuggers show ugly default | Always define `__repr__`; `__str__` optional |
| Setting `self.accuracy = value` inside the `accuracy` setter | Infinite recursion → crash | Store in `self._accuracy` |
| Using `__double_underscore` casually | Name mangling causes confusion | Use single `_underscore` instead |

---

#### Cheat Sheet — OOP

```python
# Defining a class
class ClassName:
    class_attribute = "shared by all"
    
    def __init__(self, arg1, arg2):       # Constructor
        self.arg1 = arg1                   # Instance attributes
        self._private = "convention only"  # Underscore = "internal"
    
    def instance_method(self):              # Regular method
        return self.arg1
    
    @classmethod
    def class_method(cls):                  # Acts on the class itself
        return cls.class_attribute
    
    @classmethod
    def from_dict(cls, data):               # Alternative constructor
        return cls(data["arg1"], data["arg2"])
    
    @staticmethod
    def static_method(x):                   # No self, no cls — utility
        return x * 2
    
    @property
    def computed_value(self):               # Read like an attribute
        return self.arg1.upper()
    
    @computed_value.setter
    def computed_value(self, value):        # Validate on assignment
        if not value:
            raise ValueError("Empty!")
        self.arg1 = value
    
    def __str__(self):                      # Used by print()
        return f"ClassName({self.arg1})"
    
    def __repr__(self):                     # Used by debugger, REPL
        return f"ClassName(arg1={self.arg1!r})"

# Inheritance
class ChildClass(ParentClass):
    def __init__(self, arg1, arg2, extra):
        super().__init__(arg1, arg2)        # Run parent's __init__
        self.extra = extra                   # Add new attribute
    
    def overridden_method(self):
        base = super().overridden_method()  # Call parent's version
        return f"{base} + child stuff"

# Multiple inheritance (mixin pattern)
class Trainable: pass
class Serializable: pass
class AIModel(Trainable, Serializable): pass

# Using objects
obj = ClassName("hello", "world")
obj.instance_method()
ClassName.class_method()
ClassName.static_method(5)
isinstance(obj, ClassName)                  # True
print(ClassName.__mro__)                    # Method resolution order
```

#### Cheat Sheet — When to Use What

| Need | Use |
|---|---|
| Fixed data, never changes | tuple |
| Data + behavior together | class |
| One thing IS-A another thing | inheritance |
| One thing CONTAINS another | composition (store as attribute) |
| Same data + different behavior per type | inheritance + method override |
| Validate before saving an attribute | `@property` + `@x.setter` |
| Calculate value from other attrs | `@property` (no setter = read-only) |
| Helper that doesn't need object | `@staticmethod` |
| Alternative constructor | `@classmethod` (e.g., `from_dict`) |
| Make `print(obj)` look nice | `__str__` |
| Make debugger output readable | `__repr__` |
| Make `len(obj)` work | `__len__` |
| Make `obj1 == obj2` work | `__eq__` |
| Combine capabilities from multiple classes | multiple inheritance (mixins) |

#### Cheat Sheet — Naming Conventions

| Pattern | Meaning |
|---|---|
| `name` | Public attribute/method |
| `_name` | "Internal — please don't touch" (convention) |
| `__name` | Name-mangled to `_ClassName__name` |
| `__name__` | Magic method — reserved for Python |
| `ClassName` | PascalCase for classes |
| `method_name` | snake_case for methods/variables |

---



## Day 6 — Essential Libraries Part 1: HTTP & Secrets (`requests` + `python-dotenv`)

> **Why this day matters more than it looks.** Every single AI API call — Claude, GPT, Gemini, every open-source model on HuggingFace — is just an HTTP request with a secret API key. The fancy SDKs you'll use later (`anthropic`, `openai`) are wrappers around `requests`. If you understand today's lesson, you can call ANY AI service in the world, even ones that don't have an SDK yet. This is the day you stop being a "Power Platform person learning Python" and start thinking like an AI Engineer.

---

### The Big Picture — What's Actually Happening When You Use AI?

When you used Copilot Studio, you talked to AI through a UI. You picked a model, typed a prompt, got a response. The platform hid all the plumbing.

Today you learn the plumbing. Here's what every AI API call looks like under the hood:

```
YOUR PYTHON CODE                        ANTHROPIC'S SERVERS
────────────────                        ───────────────────

  prompt = "Write a haiku"
        │
        ▼
  ┌──────────────────────┐
  │  Build HTTP request  │
  │  - URL               │              ┌──────────────────┐
  │  - Headers (API key) │  ─────────▶  │  Claude model    │
  │  - JSON body         │   internet   │  processes       │
  │  - POST method       │              │  prompt          │
  └──────────────────────┘              └──────────────────┘
                                                │
        ┌────────────────────────────────────────┘
        ▼   internet
  ┌──────────────────────┐
  │  HTTP response       │
  │  - Status code (200) │
  │  - JSON body         │
  │    └─ "haiku text"   │
  └──────────────────────┘
        │
        ▼
  Parse JSON, extract answer, show user
```

That's it. **AI APIs are just web APIs.** The model is doing the magic on their servers — your job is to:
1. Send the right HTTP request (URL + headers + JSON body)
2. Authenticate (API key in headers)
3. Parse the response (JSON → Python dict → extract text)

The `requests` library handles step 1 and 3. `python-dotenv` handles step 2 safely.

#### Connecting to Your Power Platform Background

If you've used the **HTTP connector** in Power Automate, you already know this conceptually:

| Power Automate HTTP Connector | Python `requests` |
|---|---|
| Method dropdown (GET/POST) | `requests.get()` / `requests.post()` |
| URI field | First argument to the function |
| Headers section | `headers=` parameter |
| Body section | `json=` parameter |
| "Run" button | Pressing Enter in your script |
| Connection references for secrets | `.env` file + `python-dotenv` |
| Compose action to parse response | `response.json()` |

You're not learning a new concept — you're learning the **code-first version** of something you already understand. The advantage: no flow runs limits, no licensing, runs anywhere, infinitely faster, and can be embedded in real applications.

---

### Installation

```bash
pip install requests python-dotenv
```

Verify both work:
```python
import requests
import dotenv
print(requests.__version__)   # e.g., 2.31.0
print(dotenv.__version__)     # e.g., 1.0.0
```

If `import` works without errors, you're set.

---

### Part 1 — The `requests` Library

`requests` is the most popular Python library, period. The Python team itself recommends it. It does ONE thing well: makes HTTP calls feel like talking to a friend.

#### HTTP Methods — The 4 Verbs You Need to Know

HTTP is built around verbs. Each verb has a meaning. APIs are designed around them.

| Verb | What It Means | Real-world Equivalent | AI Example |
|---|---|---|---|
| **GET** | "Give me data" | Reading a webpage | List your past Claude conversations |
| **POST** | "Here's new data, create it" | Submitting a form | Send a prompt, get a response |
| **PUT** | "Replace this thing entirely" | Editing a Word doc | Update a file in cloud storage |
| **DELETE** | "Remove this" | Deleting an email | Delete a stored conversation |

For AI work, you'll use **GET and POST 95% of the time**. POST especially — every prompt you send is a POST request.

#### Your First GET Request

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)   # 200 = success
print(response.text)          # Raw text response
print(response.json())        # Same response, parsed as Python dict
```

**What just happened:**
1. Your computer sent a GET request to that URL
2. The server responded with JSON data + a status code
3. `response` is an object holding everything: status, headers, body
4. `.json()` converts the JSON text into a Python dict so you can use it

**The `response` object — what's inside:**

```python
response.status_code    # 200, 404, 500, etc. (always check this first!)
response.text           # Raw response body as a string
response.json()         # Parsed JSON as Python dict (only works if response IS JSON)
response.headers        # Dict of response headers (content-type, rate-limit info, etc.)
response.url            # The actual URL hit (useful when there were redirects)
response.elapsed        # How long the request took (timedelta object)
response.ok             # True if status_code is 200-299, else False
```

#### Status Codes — The 5 Categories

Every HTTP response comes with a 3-digit status code. The first digit tells you the category.

| Range | Category | What It Means | Common Examples |
|---|---|---|---|
| **1xx** | Informational | Rare, ignore for now | — |
| **2xx** | ✅ Success | Everything worked | `200 OK`, `201 Created` |
| **3xx** | Redirect | "Look elsewhere" | `301 Moved`, `304 Not Modified` |
| **4xx** | ❌ YOUR fault | You sent a bad request | `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `429 Too Many Requests` |
| **5xx** | ❌ THEIR fault | The server crashed | `500 Internal Server Error`, `503 Service Unavailable` |

**The codes you'll meet daily as an AI Engineer:**

```
200  ✅ Got the AI response, all good
201  ✅ Created a new resource (e.g., uploaded a file)
400  ❌ Your prompt or JSON body was malformed
401  ❌ Invalid API key
403  ❌ API key valid but no permission for this action
404  ❌ Wrong URL endpoint
429  ❌ Rate limited — slow down or pay for higher tier
500  ❌ AI provider is having a bad day
529  ❌ Anthropic-specific: overloaded, retry later
```

> **Mental model:** 4xx = "I (the client) screwed up." 5xx = "They (the server) screwed up." Memorize this and debugging becomes 10x easier.

#### Query Parameters — Adding Data to GET Requests

Query parameters are the `?key=value&other=thing` part of URLs.

**The hard way (string concatenation — don't do this):**
```python
city = "Hyderabad"
url = f"https://api.example.com/weather?city={city}&units=metric"
response = requests.get(url)
```

**The clean way (`params` argument):**
```python
response = requests.get(
    "https://api.example.com/weather",
    params={
        "city": "Hyderabad",
        "units": "metric",
        "lang": "en"
    }
)
```

`requests` builds the URL for you, automatically URL-encodes special characters (spaces → `%20`, etc.), and the code reads way better. **Always use `params=`.**

#### Headers — Metadata About Your Request

Headers are information about the request itself, not the data. Think of them as the envelope, while the body is the letter inside.

```python
response = requests.get(
    "https://api.example.com/data",
    headers={
        "Authorization": "Bearer YOUR_API_KEY",
        "Content-Type": "application/json",
        "User-Agent": "MyApp/1.0"
    }
)
```

**The 3 headers you'll see in every AI API call:**

| Header | What It Does | Example |
|---|---|---|
| `Authorization` or `x-api-key` | Proves who you are | `Bearer sk-ant-...` |
| `Content-Type` | "I'm sending JSON" | `application/json` |
| `anthropic-version` (Claude-specific) | Which API version | `2023-06-01` |

#### Your First POST Request — Sending Data

POST is for creating things. The data goes in the **body** of the request, not the URL.

```python
import requests

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={
        "title": "My first post",
        "body": "This is the body of my post",
        "userId": 1
    }
)

print(response.status_code)   # 201 (Created)
print(response.json())        # The created post with an assigned ID
```

> **Critical detail:** Use `json=` (not `data=`). `json=` automatically:
> 1. Converts your Python dict to JSON text
> 2. Adds the `Content-Type: application/json` header
> 3. Encodes everything correctly
>
> If you use `data=` with a dict, it sends form data (like a HTML form submission), which most APIs don't accept.

#### Calling Claude API Manually — The "AHA!" Moment

This is what every AI engineer does dozens of times a day. After today, you can do this without the SDK:

```python
import requests

response = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": "sk-ant-your-key-here",   # We'll move this to .env in Part 2
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    },
    json={
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Write a haiku about Python."}
        ]
    }
)

# Parse the response
data = response.json()
haiku = data["content"][0]["text"]
print(haiku)
```

That's it. **That's the entire AI engineer workflow.** Everything you'll build for the rest of your career — chatbots, RAG systems, agents — is variations of this 12 lines of code.

---

#### Error Handling — The Mark of a Real Engineer

Beginner code assumes everything works. Production code assumes everything will break. APIs fail constantly: networks drop, rate limits hit, servers crash. You MUST handle this.

**The naive (broken) version:**
```python
response = requests.get("https://api.example.com/data")
data = response.json()         # Crashes if response is HTML error page
print(data["users"][0])        # Crashes if "users" key doesn't exist
```

**The robust version:**
```python
import requests

try:
    response = requests.get(
        "https://api.example.com/data",
        timeout=10                              # Don't wait forever
    )
    response.raise_for_status()                 # Raise exception for 4xx/5xx
    data = response.json()
    print(data)

except requests.exceptions.Timeout:
    print("Request timed out — server too slow")

except requests.exceptions.ConnectionError:
    print("Couldn't connect — check internet")

except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")
    print(f"Server said: {e.response.text}")

except requests.exceptions.JSONDecodeError:
    print("Response wasn't valid JSON")

except requests.exceptions.RequestException as e:
    print(f"Something else went wrong: {e}")
```

#### The Exceptions You'll Actually See

| Exception | When It Happens | What To Do |
|---|---|---|
| `Timeout` | Server didn't respond in `timeout=` seconds | Retry, or increase timeout |
| `ConnectionError` | Can't reach the server (DNS, no internet) | Check network, retry |
| `HTTPError` | Got a 4xx or 5xx response | Read the error body for details |
| `JSONDecodeError` | Response body isn't valid JSON | Probably an HTML error page — print `.text` |
| `RequestException` | Catch-all parent class | Always include this last as a safety net |

#### `timeout=` — The Most Forgotten Argument

```python
# ⚠️ NEVER do this in production:
response = requests.get(url)    # No timeout = could hang forever

# ✅ Always set a timeout:
response = requests.get(url, timeout=10)   # Wait max 10 seconds
```

**Why this matters for AI:** Claude can take 30+ seconds to respond to long prompts. OpenAI similar. If you forget `timeout`, your script can hang indefinitely on a flaky network. Common defaults:
- Quick API checks: `timeout=5`
- AI completion calls: `timeout=60`
- AI calls with big prompts/streaming: `timeout=120`

#### `raise_for_status()` — One Line, Saves Hours

```python
response = requests.get(url)
response.raise_for_status()   # Raises HTTPError for 4xx/5xx
```

Without this, a 404 still gets you a `response` object — `.json()` might even work (returning the error JSON). You'll think things succeeded and get confusing bugs downstream. **Always call `raise_for_status()` after every request unless you have a specific reason not to.**

---

### Part 2 — `python-dotenv`: The Secrets Problem

#### Why You Should Be Scared of API Keys

Your Claude API key is **money**. Anyone who has it can spend your account dry. There are bots that scan GitHub 24/7 looking for committed API keys. They've been measured to find and abuse keys **within 60 seconds** of the commit going public.

**The disaster scenario (this happens to people every single day):**

```python
# main.py — pushed to GitHub
import requests

API_KEY = "sk-ant-real-key-here"   # ← The mistake

response = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={"x-api-key": API_KEY},
    ...
)
```

```bash
git add .
git commit -m "first AI app"
git push                       # ← Key now public on GitHub
                               # ← Bots find it within minutes
                               # ← Your account gets drained
                               # ← You wake up to an email from Anthropic
```

**Even if you delete the file later and force-push, it's still in Git history forever.** The only fix is to revoke the key immediately and generate a new one.

#### The `.env` Pattern — How Real Engineers Solve This

The pattern has 3 pieces:

```
your-project/
├── .env                ← Real secrets live here (NEVER committed)
├── .env.example        ← Template with FAKE values (committed, helps teammates)
├── .gitignore          ← Tells Git to ignore .env
└── main.py             ← Reads from .env via os.getenv()
```

**Step 1 — Create `.env` (your real secrets):**
```
ANTHROPIC_API_KEY=sk-ant-api03-real-key-here
OPENWEATHER_API_KEY=abc123realkey
DATABASE_URL=postgresql://user:password@localhost/mydb
```

> **Format rules:**
> - No spaces around `=` (write `KEY=value`, not `KEY = value`)
> - No quotes needed unless value has spaces
> - One key per line
> - Comments start with `#`

**Step 2 — Create `.gitignore` (BEFORE your first commit!):**
```
# Secrets
.env
*.env
.env.local

# Python
__pycache__/
*.pyc
venv/
.venv/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

**Step 3 — Create `.env.example` (committed, helps teammates):**
```
ANTHROPIC_API_KEY=sk-ant-your-key-here
OPENWEATHER_API_KEY=your-openweather-key
DATABASE_URL=postgresql://user:password@host/db
```

This file is committed to GitHub. Teammates copy it to `.env` and fill in their own real values. Standard practice in every professional codebase.

**Step 4 — Read secrets in Python:**
```python
import os
from dotenv import load_dotenv

load_dotenv()                               # Reads .env into environment variables

api_key = os.getenv("ANTHROPIC_API_KEY")    # Returns the value, or None if missing

if not api_key:
    raise ValueError("ANTHROPIC_API_KEY not set! Check your .env file.")
```

#### How `load_dotenv()` Actually Works

```
your script starts
       │
       ▼
load_dotenv() is called
       │
       ▼
Looks for .env file in current folder, then parent folders
       │
       ▼
Reads each line, parses KEY=VALUE
       │
       ▼
Sets each as a temporary environment variable (just for this Python process)
       │
       ▼
os.getenv("KEY") can now read it
       │
       ▼
When script ends, environment variables disappear (no permanent change)
```

This is the same idea as the PATH environment variable from your Day 1 setup, but scoped to just this script run.

#### `os.getenv()` vs `os.environ[]` — Subtle But Important

```python
# os.getenv() — returns None if missing (safe)
api_key = os.getenv("ANTHROPIC_API_KEY")
# api_key is None if not set, no crash

# os.getenv() with default
api_key = os.getenv("ANTHROPIC_API_KEY", "fallback-value")

# os.environ[] — crashes if missing
api_key = os.environ["ANTHROPIC_API_KEY"]
# KeyError if not set
```

**Best practice for required secrets:**
```python
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError(
        "ANTHROPIC_API_KEY not found. "
        "Create a .env file with: ANTHROPIC_API_KEY=your-key-here"
    )
```

This **fails fast with a helpful message** instead of mysteriously crashing 50 lines later.

#### Your "Did I Already Leak the Key?" Checklist

Before every push, do this mental check:
1. Is `.env` in my `.gitignore`? Run `git status` — `.env` should NOT appear in any color.
2. Did I `git add .env` accidentally before adding it to `.gitignore`? Run `git ls-files | grep env` — should show `.env.example` only, not `.env`.
3. If you ever see `.env` listed as a tracked file, **stop, do not push, ask for help removing it from history.**

---

### Part 3 — Putting It All Together (Claude API, Properly)

This is the production-quality version of the earlier example. Save this snippet — you'll use this pattern hundreds of times.

```python
# claude_call.py
import os
import requests
from dotenv import load_dotenv

# Load secrets from .env
load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")

if not API_KEY:
    raise ValueError("ANTHROPIC_API_KEY not set in .env")

def ask_claude(prompt: str) -> str:
    """Send a prompt to Claude and return the text response."""
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": API_KEY,
                "anthropic-version": "2023-06-01",
                "Content-Type": "application/json"
            },
            json={
                "model": "claude-sonnet-4-20250514",
                "max_tokens": 1024,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            },
            timeout=60
        )
        response.raise_for_status()
        data = response.json()
        return data["content"][0]["text"]

    except requests.exceptions.HTTPError as e:
        return f"API error {e.response.status_code}: {e.response.text}"
    except requests.exceptions.Timeout:
        return "Request timed out"
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"

# Use it
if __name__ == "__main__":
    answer = ask_claude("Write a haiku about debugging Python.")
    print(answer)
```

This is **professional AI engineer code**. It handles errors, uses environment variables, has a clear function signature, and works.

---

### Day 6 Experiments

#### Experiment 1 — Weather App with OpenWeatherMap

**Get your free API key:**
1. Go to [openweathermap.org](https://openweathermap.org/api), sign up
2. Go to "API keys" tab, copy your key
3. ⚠️ Note: New keys take ~10 minutes to activate

**Add it to your `.env`:**
```
OPENWEATHER_API_KEY=your-key-here
```

**Build the app:**
```python
# weather_app.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str) -> dict:
    """Fetch weather for a city. Returns parsed JSON or raises."""
    response = requests.get(
        "https://api.openweathermap.org/data/2.5/weather",
        params={
            "q": city,
            "appid": API_KEY,
            "units": "metric"   # Celsius. Use "imperial" for Fahrenheit.
        },
        timeout=10
    )
    response.raise_for_status()
    return response.json()

def display_weather(city: str):
    try:
        data = get_weather(city)

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌤️  Weather in {city}")
        print(f"   Condition:  {description.title()}")
        print(f"   Temperature: {temp}°C (feels like {feels_like}°C)")
        print(f"   Humidity:    {humidity}%")
        print(f"   Wind speed:  {wind_speed} m/s\n")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"❌ City '{city}' not found")
        elif e.response.status_code == 401:
            print("❌ Invalid API key (or wait 10 mins for activation)")
        else:
            print(f"❌ HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    display_weather(city)
```

**Bonus challenges:**
1. Loop and ask for weather in 5 different cities; show the hottest
2. Save each query result to a list of dicts; print as a table at the end
3. Convert wind speed from m/s to km/h (multiply by 3.6)
4. Use `data["sys"]["country"]` to print the country code too

#### Experiment 2 — JSONPlaceholder API (No Key Needed)

[JSONPlaceholder](https://jsonplaceholder.typicode.com) is a fake REST API for practice. No key, no signup.

```python
# jsonplaceholder_practice.py
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_all_posts():
    """GET all 100 posts."""
    response = requests.get(f"{BASE_URL}/posts", timeout=10)
    response.raise_for_status()
    return response.json()

def get_posts_by_user(user_id: int):
    """GET posts filtered by userId using query params."""
    response = requests.get(
        f"{BASE_URL}/posts",
        params={"userId": user_id},
        timeout=10
    )
    response.raise_for_status()
    return response.json()

def create_post(title: str, body: str, user_id: int):
    """POST a new post."""
    response = requests.post(
        f"{BASE_URL}/posts",
        json={
            "title": title,
            "body": body,
            "userId": user_id
        },
        timeout=10
    )
    response.raise_for_status()
    return response.json()

def get_nonexistent_post():
    """Trigger a 404 to practice error handling."""
    try:
        response = requests.get(f"{BASE_URL}/posts/9999", timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"Caught error as expected: {e.response.status_code}")
        return None

if __name__ == "__main__":
    # Task 1: Get all posts, count them
    posts = get_all_posts()
    print(f"Total posts: {len(posts)}")

    # Task 2: Get posts by user 1, print titles
    user_posts = get_posts_by_user(1)
    print(f"\nUser 1 has {len(user_posts)} posts:")
    for post in user_posts:
        print(f"  - {post['title']}")

    # Task 3: Create a new post
    new_post = create_post(
        title="My Day 6 learning",
        body="Today I learned requests and dotenv!",
        user_id=1
    )
    print(f"\nCreated post with ID: {new_post['id']}")

    # Task 4: Trigger and handle 404
    print("\nTrying nonexistent post...")
    get_nonexistent_post()
```

> **Note about JSONPlaceholder:** It "fakes" the POST — it returns a fake ID like 101 but doesn't actually save anything. The point is to practice the request/response cycle without messing up real data.

**Bonus challenges:**
1. GET `/users/1` → print that user's name, email, and address.city
2. GET `/users/1/posts` → all posts by user 1 using a different endpoint
3. GET `/posts/1/comments` → all comments on post 1
4. Build a function `get_user_with_posts(user_id)` that combines two API calls and returns one merged dict

#### Experiment 3 — Bonus: Direct Claude Call

If you have a Claude API key, run the `claude_call.py` from Part 3 above. This is the "I am now an AI engineer" moment — calling an LLM directly without any SDK.

If you don't have a key yet, get one from [console.anthropic.com](https://console.anthropic.com) on Day 9 when we cover it formally. For now, you can run the same logic against the JSONPlaceholder API — the *pattern* is what matters today.

---

### Common Pitfalls (I Will Definitely Hit These)

| Mistake | Symptom | Fix |
|---|---|---|
| Hardcoded API key in code | Bot drains your account | Use `.env` from day one |
| Forgot `.gitignore` before first commit | Key already on GitHub | Revoke key, generate new one, add `.gitignore`, force-push |
| Forgot `load_dotenv()` | `os.getenv()` returns `None` | Add `load_dotenv()` at top of script |
| Forgot `timeout=` | Script hangs forever | Always pass `timeout=` |
| Used `data=` instead of `json=` | API returns 400 Bad Request | Use `json=` for JSON APIs |
| Forgot `.raise_for_status()` | Errors silently ignored | Always call it after `.get()`/`.post()` |
| Called `.json()` on HTML response | `JSONDecodeError` crash | Print `response.text` first to see what came back |
| Used `os.environ["KEY"]` for optional var | KeyError crash | Use `os.getenv("KEY")` instead |
| API key has trailing spaces in `.env` | 401 Unauthorized | Check for invisible whitespace |
| `.env` file has quotes around values | Value includes the quotes | Remove the quotes |

---

### Cheat Sheet — Day 6

#### `requests` essentials
```python
import requests

# GET with query params
r = requests.get(url, params={"key": "value"}, timeout=10)

# POST with JSON body
r = requests.post(url, json={"key": "value"}, headers={...}, timeout=10)

# Always after every request
r.raise_for_status()           # Raises if 4xx/5xx
data = r.json()                # Parse JSON to dict

# Useful response attributes
r.status_code                  # 200, 404, etc.
r.text                         # Raw text body
r.headers                      # Response headers as dict
r.elapsed                      # How long it took
r.ok                           # True if 2xx

# Bulletproof error handling
try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    data = r.json()
except requests.exceptions.Timeout:        ...
except requests.exceptions.HTTPError as e: ...
except requests.exceptions.RequestException as e: ...
```

#### `python-dotenv` essentials
```python
# .env file
ANTHROPIC_API_KEY=sk-ant-...

# .gitignore — MUST include
.env

# In Python
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("ANTHROPIC_API_KEY")
if not key:
    raise ValueError("ANTHROPIC_API_KEY not set")
```

#### Claude API call template (memorize this)
```python
response = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": os.getenv("ANTHROPIC_API_KEY"),
        "anthropic-version": "2023-06-01",
        "Content-Type": "application/json"
    },
    json={
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": "Hello!"}]
    },
    timeout=60
)
response.raise_for_status()
text = response.json()["content"][0]["text"]
```

---

### Push to GitHub

```bash
# Verify .env is NOT being tracked
git status
# .env should NOT appear. .env.example should appear.

# If .env appears, STOP and add it to .gitignore first!

git add .
git commit -m "Day 6: requests + dotenv, weather app, JSONPlaceholder practice"
git push
```

---

> **Note to future me:** Today was the day everything clicked. Every AI API in existence — Claude, GPT, Gemini, local LLaMA servers, HuggingFace, Pinecone, every vector DB — speaks HTTP + JSON. You now speak that language. The fancy SDKs you'll use later (`anthropic`, `openai`, `langchain`) are just abstractions over what you did today. When something breaks in production at 2am, the SDK won't help you — but the `requests` debugging skills you built today will.

> **Power Platform parallel:** Day 6 is your "HTTP connector" but better. No flow runs limit, no licensing, runs anywhere, returns instantly. Same mental model: trigger → action → parse response. Different power level entirely.