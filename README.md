# ⌨️ Keystroke Logging Monitor

A modern GUI-based keyboard event monitoring system built using Python and Tkinter.  
This application captures real-time key press and release events, logs them in structured formats, and provides a clean and responsive user interface.
![UI](img/UI.png)

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

## 📁 Project Structure

📦 keystroke_logging  
 ┣ 📜 keystroke.py  
 ┣ 📄 requirements.txt  
 ┣ 📘 README.md  
 ┣ 🚫 .gitignore  
 ┗ 📂 logs  
   ┣ 📄 key_log.txt  
   ┗ 📄 key_log.json  


---
### ⚙️ **TECHNOLOGIES USED**

The project is built using the following technologies and libraries:

- 🔹 **Python**  
  **Core programming language** used to develop the application logic and functionality.

- 🔹 **Tkinter**  
  Used to design the **graphical user interface (GUI)** and handle keyboard events within the application window.

- 🔹 **JSON**  
  Enables **structured storage of keystroke data**, making it suitable for analysis and future processing.

- 🔹 **OS Module**  
  Handles **file system operations** such as creating directories and managing log files.

- 🔹 **Datetime Module**  
  Used to capture **accurate timestamps** for each key press and release event.

---

## 🔒 **SECURITY**

This application is designed with a strong focus on **safety and compliance**:

- 🔐 Operates in **safe mode**, capturing keystrokes only within the active application window  
- 🔐 Does **not require system-level permissions** such as Accessibility or Input Monitoring  
- 🔐 Fully compliant with **macOS security and privacy policies**  
- 🔐 Intended strictly for **educational and ethical use only**

---

## ⚠️ **LIMITATIONS**

Due to operating system restrictions and design choices:

- ⚠️ Cannot capture keystrokes outside the application window  
- ⚠️ Does not support **global/system-wide keylogging**  
- ⚠️ Requires the application window to be **focused** for input detection  
- ⚠️ Not intended for **unauthorized monitoring or surveillance**

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
  }
]

