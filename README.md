# 🛡 Mini Intrusion Detection System (IDS)

## 📌 Project Overview

This project is a Python-based real-time Intrusion Detection System (IDS) simulator designed to monitor log files and detect suspicious login activity.

The system continuously monitors a log file and triggers alerts when:

- Multiple failed login attempts occur (Brute Force Detection)
- A successful login occurs after repeated failed attempts (Possible Account Compromise)

This project simulates basic SOC (Security Operations Center) monitoring behavior.

---

## 🚀 Features

- Real-time log monitoring
- Brute-force attack detection
- Threshold-based alerting system
- Account compromise risk detection
- Lightweight and easy to simulate attacks

---

## 🛠 Technologies Used

- Python
- Regular Expressions (re)
- Time-based monitoring
- File handling
- Basic cybersecurity concepts

---

## ⚙ How It Works

1. The script continuously monitors a log file.
2. It tracks failed login attempts per IP address.
3. If failed attempts exceed a defined threshold:
   - It triggers a brute-force alert.
4. If a successful login occurs after multiple failures:
   - It triggers a critical compromise alert.

---

## ▶ How To Run

### Step 1: Run the IDS
```
python ids.py
```

### Step 2: Simulate an Attack
Open the log file and add lines like:

```
192.168.1.5 - Failed login
```

After multiple failed attempts, the IDS will generate alerts.

---

## 🎯 Learning Outcomes

- Understanding of Intrusion Detection Systems (IDS)
- Log monitoring techniques
- Threshold-based attack detection
- Real-time alerting simulation
- Blue Team fundamentals

---

## 🔒 Disclaimer

This project is created strictly for educational purposes to understand cybersecurity monitoring concepts.

---

## 👩‍💻 Author

Shravani Rajesh Sawant  
Aspiring Cybersecurity Analyst