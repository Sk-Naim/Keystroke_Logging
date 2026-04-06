import tkinter as tk
import json
import os
from datetime import datetime

# Create logs folder
if not os.path.exists("logs"):
    os.makedirs("logs")

TEXT_LOG_PATH = "logs/key_log.txt"
JSON_LOG_PATH = "logs/key_log.json"

keys_used = []
keys_text = ""


def save_logs():
    with open(TEXT_LOG_PATH, "w", encoding="utf-8") as f:
        f.write(keys_text)

    with open(JSON_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(keys_used, f, indent=4)


def log_event(event_type, key):
    global keys_text, keys_used

    time_now = datetime.now().strftime("%H:%M:%S")

    keys_text += f"[{event_type}:{key}] "
    keys_used.append({
        "event": event_type,
        "key": key,
        "time": time_now
    })

    save_logs()

    output_label.config(text=f"{event_type}: {key}")


def on_key_press(event):
    log_event("Pressed", event.keysym)


def on_key_release(event):
    log_event("Released", event.keysym)


def start_logging():
    root.focus_force()
    root.bind_all("<KeyPress>", on_key_press)
    root.bind_all("<KeyRelease>", on_key_release)

    status_label.config(text="🟢 Logging Started", fg="#00ff88")
    start_button.config(state='disabled')
    stop_button.config(state='normal')


def stop_logging():
    root.unbind_all("<KeyPress>")
    root.unbind_all("<KeyRelease>")

    status_label.config(text="🔴 Logging Stopped", fg="#ff4444")
    start_button.config(state='normal')
    stop_button.config(state='disabled')


# 🔥 Hover effects
def on_enter(e):
    if "Start" in e.widget.cget("text"):
        e.widget.config(bg="#00cc6a")
    else:
        e.widget.config(bg="#cc0000")


def on_leave(e):
    if "Start" in e.widget.cget("text"):
        e.widget.config(bg="#00ff88")
    else:
        e.widget.config(bg="#ff4444")


# GUI Design
root = tk.Tk()
root.title("Keylogger Monitor - Sk Naim")
root.geometry("420x240")
root.configure(bg="#121212")

# Focus on click
root.bind("<Button-1>", lambda e: root.focus_force())

# Title
title = tk.Label(root, text="⌨️ Keylogger Monitor", font=("Helvetica", 16, "bold"),
                 bg="#121212", fg="#ffffff")
title.pack(pady=10)

# Status
status_label = tk.Label(root, text="Click Start to Begin",
                        font=("Helvetica", 10),
                        bg="#121212", fg="#aaaaaa")
status_label.pack()

# Output display
output_label = tk.Label(root, text="Waiting...",
                        font=("Courier", 12),
                        bg="#1e1e1e", fg="#00ffcc",
                        width=30, height=2)
output_label.pack(pady=15)

# Button Frame
btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack()

# 🔥 Start Button (Bright Green)
start_button = tk.Button(
    btn_frame,
    text="▶ Start",
    command=start_logging,
    bg="#00ff88",
    fg="black",
    activebackground="#00cc6a",
    font=("Helvetica", 11, "bold"),
    width=12,
    relief="flat"
)
start_button.grid(row=0, column=0, padx=15, pady=5)

# 🔥 Stop Button (Bright Red)
stop_button = tk.Button(
    btn_frame,
    text="■ Stop",
    command=stop_logging,
    state='disabled',
    bg="#ff4444",
    fg="white",
    activebackground="#cc0000",
    font=("Helvetica", 11, "bold"),
    width=12,
    relief="flat"
)
stop_button.grid(row=0, column=1, padx=15, pady=5)

# Apply hover effects
start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)

stop_button.bind("<Enter>", on_enter)
stop_button.bind("<Leave>", on_leave)

# Footer
footer = tk.Label(root, text="macOS Safe Mode (App Focus Only)",
                  font=("Helvetica", 8),
                  bg="#121212", fg="#666666")
footer.pack(side="bottom", pady=5)

root.mainloop()