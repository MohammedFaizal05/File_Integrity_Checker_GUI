import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import hashlib, os, json
import datetime
import platform

# Sound: Cross-platform beeps
def play_beep(type="ok"):
    if platform.system() == "Windows":
        import winsound
        if type == "ok":
            winsound.MessageBeep(winsound.MB_OK)
        elif type == "alert":
            winsound.MessageBeep(winsound.MB_ICONHAND)
        elif type == "info":
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
    else:
        print("\a")  # fallback for Linux/Mac (terminal beep)

# Calculate SHA-256 hash of a file
def calculate_hash(file_path):
    sha = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha.update(chunk)
    return sha.hexdigest()

# Append logs to a text file
def write_log(text):
    with open("logs.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[{datetime.datetime.now()}] {text}\n")

# Create baseline
def create_baseline():
    directory = folder_path.get()
    if not directory:
        messagebox.showerror("Error", "Please select a folder first.")
        play_beep("alert")
        return
    hashes = {}
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            hashes[filename] = calculate_hash(path)
    with open("baseline.json", "w") as f:
        json.dump(hashes, f)
    message = f"✅ Baseline created for files in: {directory}"
    output.insert(tk.END, message + "\n")
    write_log(message)
    play_beep("ok")

# Check integrity
def check_integrity():
    directory = folder_path.get()
    if not directory:
        messagebox.showerror("Error", "Please select a folder first.")
        play_beep("alert")
        return
    if not os.path.exists("baseline.json"):
        messagebox.showerror("Error", "Baseline not found! Please create one first.")
        play_beep("alert")
        return

    with open("baseline.json", "r") as f:
        baseline = json.load(f)

    output.insert(tk.END, "🛡️ Checking integrity...\n")
    write_log("🛡️ Checking integrity...")

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path):
            current_hash = calculate_hash(path)
            if filename in baseline:
                if current_hash != baseline[filename]:
                    message = f"⚠️ Modified: {filename}"
                    play_beep("alert")
                else:
                    message = f"✅ OK: {filename}"
                    play_beep("ok")
            else:
                message = f"🆕 New File: {filename}"
                play_beep("info")

            output.insert(tk.END, message + "\n")
            write_log(message)

# Folder picker
def browse_folder():
    selected = filedialog.askdirectory()
    if selected:
        folder_path.set(selected)

# GUI setup
app = tk.Tk()
app.title("File Integrity Checker")
app.geometry("600x420")

folder_path = tk.StringVar()

tk.Label(app, text="Select Folder to Monitor:").pack(pady=5)
tk.Entry(app, textvariable=folder_path, width=50).pack()
tk.Button(app, text="Browse", command=browse_folder).pack(pady=5)

tk.Button(app, text="Create Baseline", command=create_baseline, bg="#90ee90").pack(pady=5)
tk.Button(app, text="Check Integrity", command=check_integrity, bg="#ffcccb").pack(pady=5)

output = scrolledtext.ScrolledText(app, width=70, height=15)
output.pack(pady=10)

app.mainloop()
