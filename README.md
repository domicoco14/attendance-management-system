# 📋 Attendance Management System (Python)

A simple **command-line Attendance Management System** built with **Python** and **Pandas**.  
This project allows users to mark attendance, track arrival times, determine early/late status, search for students, and store attendance records persistently.

**GitHub Profile:** [domicoco14](https://github.com/domicoco14)

---

## 🚀 Project Overview

The **Attendance Management System** is designed for small classes, training sessions, or personal projects where attendance tracking is required without the complexity of a database or web application.

### It records:
- Student full names
- Time of arrival
- Attendance status (EARLY or LATE)

All data can be saved and retrieved from a text file for future reference.

---

## ✨ Features

- ✔ Mark attendance with automatic time capture  
- ✔ Detect **EARLY** or **LATE** arrivals (cut-off time: **10:00 AM**)  
- ✔ View today's attendance in a table format  
- ✔ Search for students by name  
- ✔ Save attendance records to a file  
- ✔ View past attendance history  
- ✔ User-friendly menu-driven interface  

---

## 🛠 Technologies Used

- **Python 3**
- **Pandas**
- **Datetime module**
- **Time module**

---

## 📂 Project Structure

```
attendance-management-system/
│
├── attendance.py                  # Main Python program
├── attendance_database.txt        # Stores saved attendance records
└── README.md                      # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/domicoco14/attendance-management-system.git
```

### 2️⃣ Navigate to the Project Directory
```bash
cd attendance-management-system
```

### 3️⃣ Install Required Dependency
```bash
pip install pandas
```

---

## ▶️ How to Run the Program

```bash
python attendance.py
```

Once started, the system will display the current date and show the main menu.

---

## 📖 Menu Options Explained

### 1️⃣ Mark Attendance
- Prompts the user to enter a full name
- Automatically records the current time
- Assigns status:
  - **EARLY** → Arrival before or at 10:00 AM
  - **LATE** → Arrival after 10:00 AM

### 2️⃣ View Today's Attendance
- Displays all marked attendance for the current session
- Uses Pandas DataFrame for clean tabular output

### 3️⃣ Search Student Record
- Search by typing the first 3 letters of a student's name
- Displays:
  - Full name
  - Time of arrival
  - Attendance status

### 4️⃣ Save Attendance Records
- Saves the current session attendance to `attendance_database.txt`
- Uses append mode so previous records are preserved

### 5️⃣ View Past Attendance Records
- Reads and displays all saved attendance history from the file
- Handles missing files gracefully

### 6️⃣ Close Attendance Sheet
- Safely exits the program

---

## 📝 Sample Output

```
FULL NAME        TIME IN     STATUS
1 John Doe       09:15 AM    EARLY
2 Jane Smith     10:20 AM    LATE
```

---

## ⚠️ Notes & Limitations

- Data is stored in a text file, not a database
- Attendance resets when the program restarts unless saved
- Designed for learning and small-scale usage
- Single-session memory (no automatic reload of past data)

---

## 🔮 Possible Future Improvements

- Save records in CSV or Excel format
- Load previous attendance automatically
- Add date-wise attendance tracking
- Prevent duplicate attendance entries
- Add authentication or admin access
- Convert to a GUI or web-based system

---

## 🤝 Contributing

Contributions are welcome!

- Fork the repository
- Create a new branch
- Make your changes
- Submit a pull request

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👤 Author
- **Name** Dominion Akinsola
- **GitHub:** [domicoco14](https://github.com/domicoco14)
- **Project:** Attendance Management System
