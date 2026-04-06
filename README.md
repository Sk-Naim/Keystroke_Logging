⌨️ Keystroke Logging Monitor

A modern GUI-based keyboard event monitoring system built using Python and Tkinter.
This application captures real-time key press and release events, stores them in structured formats, and provides a clean visual interface — all while remaining fully compatible with macOS (M1/M2/M3) without requiring special permissions.

🖼️ Application Preview
4
🚀 Features
✅ Real-time Key Event Detection
Captures both key press and key release events instantly.
✅ Dual Format Logging
TXT → Human-readable format
JSON → Structured data for analysis
✅ Auto-Save Functionality
Logs are saved automatically without user intervention.
✅ Modern Dark UI
Clean and visually appealing interface with responsive controls.
✅ macOS Safe Mode
Works without requiring Accessibility or Input Monitoring permissions.
✅ Live Event Display
Shows the latest key interaction in real time.
🧠 How It Works
4
User presses a key inside the application window
Tkinter captures the key event (KeyPress / KeyRelease)
Event is processed and timestamped
Data is stored in:
key_log.txt
key_log.json
UI updates instantly to reflect the latest key action
📂 Project Structure
keystroke_logging/
├── keystroke.py
├── requirements.txt
├── README.md
├── .gitignore
└── logs/
    ├── key_log.txt
    └── key_log.json
▶️ Installation & Usage
1️⃣ Clone the Repository
git clone https://github.com/your-username/key-monitor-macos.git
cd key-monitor-macos
2️⃣ Run the Application
python main.py
📁 Output Files
📝 Text Log (key_log.txt)
[Pressed:a] [Released:a] [Pressed:Shift_L]
📊 JSON Log (key_log.json)
[
  {
    "event": "Pressed",
    "key": "a",
    "time": "21:05:12"
  }
]
⚙️ Technologies Used
🐍 Python
🖥️ Tkinter (GUI)
📄 JSON (Data storage)
📁 OS Module (File handling)
⏱️ Datetime (Timestamping)
🔒 Security & Limitations
Works only when the application window is focused
Does NOT capture system-wide keystrokes (by design)
Fully compliant with macOS security policies
🎯 Use Cases
📚 Educational demonstrations
🧪 UI/UX testing
📊 Typing behavior analysis
👨‍💻 Developer debugging
🚀 Future Enhancements
📈 Typing speed (WPM) tracker
📊 Key frequency analytics
🌐 Global logging mode (with permissions)
📦 Export logs feature
🎨 Advanced UI animations
👨‍💻 Author

Sk Naimuddin
