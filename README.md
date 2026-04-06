# ⌨️ Keystroke Logging Monitor

A modern GUI-based keyboard event monitoring system built using Python and Tkinter.  
This application captures real-time key press and release events, logs them in structured formats, and provides a clean and responsive user interface.

Designed specifically to work on macOS (M1/M2/M3), the application operates in a safe mode without requiring special system permissions.

---

## 📌 Overview

Keystroke Logging Monitor is an educational and analytical tool that helps in understanding how keyboard events work in GUI-based applications. It demonstrates real-time event handling, data logging, and user interface design in Python.

The system captures keyboard interactions within the application window and stores them for further analysis in both human-readable and structured formats.

---

## 🚀 Features

- Real-time key press and release detection  
- Automatic logging of keystrokes  
- Dual format storage:
  - TXT file (readable format)
  - JSON file (structured format with timestamps)  
- Modern dark-themed user interface  
- Live display of key events  
- Start/Stop control functionality  
- Fully compatible with macOS without requiring permissions  

---

## 🧠 How It Works

1. The user starts the logging process using the GUI  
2. The application captures keyboard events using Tkinter bindings  
3. Each key press and release is recorded with a timestamp  
4. Data is stored in:
   - `key_log.txt`
   - `key_log.json`  
5. The latest key event is displayed in real time on the interface  

---

## 📂 Project Structure
key-monitor-macos/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── logs/
    ├── key_log.txt
    └── key_log.json


---

## ▶️ Installation & Usage

### Step 1: Run the Application

---

## 📁 Output Files

### key_log.txt
[Pressed:Shift_L] [Pressed:W] 
[Released:W] [Released:Shift_L] 
[Pressed:h] [Released:h] 
[Pressed:a] [Released:a] 
[Pressed:t] [Released:t] 
[Pressed:space] [Released:space]
[Pressed:i] [Released:i] [Pressed:s] 
[Released:s] [Pressed:space] 
[Released:space] [Pressed:Shift_L]
[Pressed:S] [Released:S] 
[Released:Shift_L] [Pressed:p] 
[Released:p] [Pressed:o] [Released:o] 
[Pressed:o] [Released:o] [Pressed:f] 
[Released:f] [Pressed:i] [Released:i] 
[Pressed:n] [Released:n] [Pressed:g] 
[Released:g] [Pressed:Return] [Released:Return]

### key_log.json
Stores structured data with timestamps:
```json
[
  {
        "event": "Pressed",
        "key": "Shift_L",
        "time": "21:33:49"
    },
    {
        "event": "Pressed",
        "key": "W",
        "time": "21:33:49"
    },
    {
        "event": "Released",
        "key": "W",
        "time": "21:33:49"
    },
]

---

## ⚙️ Technologies Used

- **Python** – Core programming language used to build the application  
- **Tkinter** – GUI framework for creating the user interface and handling events  
- **JSON** – Used to store structured keystroke data for analysis  
- **OS Module** – Handles file and directory operations (log folder creation)  
- **Datetime Module** – Captures timestamps for each key event  

---

## 🔒 Security & Limitations

### 🔐 Security

- The application operates in **safe mode**, capturing keystrokes only within the active window  
- No system-level permissions (like Accessibility or Input Monitoring) are required  
- Ensures compliance with macOS security and privacy policies  
- Designed strictly for **educational and ethical use**  

### ⚠️ Limitations

- Cannot capture keystrokes outside the application window  
- Does not support global/system-wide keylogging (restricted by macOS)  
- Requires the application window to be focused to detect input  
- Not intended for monitoring without user awareness  

---
