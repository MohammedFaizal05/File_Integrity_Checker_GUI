# 🛡️ File Integrity Checker (GUI Version)

## 📌 Overview

The **File Integrity Checker** is a lightweight Python-based GUI tool that monitors the integrity of files in a selected folder. It helps detect unauthorized file changes using **SHA-256 hashing**. This tool is ideal for cybersecurity learners or professionals looking to build a simple yet effective integrity monitoring system.

### 🔍 Key Features

- 📁 Folder picker to monitor any directory  
- 🔒 Create and store file hash baselines  
- 🛡️ Detect changes, modifications, and new files  
- 🔊 Sound alerts (for OK, modified, or new files)  
- 📝 Saves logs with timestamps to `logs.txt`  
- 💻 Easy-to-use GUI built with Tkinter  

---

## 🧰 Technologies Used

| Component   | Details           |
|------------|-------------------|
| Language    | Python 3.10+      |
| GUI Library | Tkinter           |
| Hashing     | SHA-256 (`hashlib`) |
| Sound       | `winsound` (Windows only) |
| Logging     | UTF-8 encoded `.txt` |
| Format      | JSON (for baselines) |

---

## 📁 Folder Structure

### file_integrity_checker/
### │
### ├── gui_integrity_checker.py # Main application
### ├── logs.txt # Auto-generated logs
### ├── baseline.json # Saved hash baseline
### └── monitored_folder/ # User-selected folder

---

## 🚀 How It Works

### ✅ Step 1: Create Baseline
- Select a folder with files
- Hashes of all files are saved to `baseline.json`

### 🛡️ Step 2: Check Integrity
- Recalculate hashes and compare with baseline
- Shows:
  - ✅ OK — File is unchanged
  - ⚠️ Modified — File has changed
  - 🆕 New File — File not in baseline

### 🔊 Sound Alerts
- ✅ OK — Default system beep  
- ⚠️ Modified — Alert tone  
- 🆕 New — Info tone  

### 📝 Logging
- All results are saved to `logs.txt` in human-readable format
- Encoding: `utf-8` (supports emojis and symbols)

---

## 🖥️ GUI Preview

> 📌 Features:

- Folder path selector
- Buttons: **Create Baseline** & **Check Integrity**
- Scrollable output log
- Error alerts via popup

---

## 💻 How to Run

### 1. Install Python

Download from: [https://www.python.org](https://www.python.org)  
Ensure `pip` and `python` are available in terminal/command prompt.

### 2. Install (Optional) Dependencies

None required! Only uses built-in Python libraries.

### 3. Run the App

```bash
python gui_integrity_checker.py

