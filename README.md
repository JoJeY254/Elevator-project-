# 🏢 IoT Elevator Control System (Prototype)

A full-stack simulation of a 4-floor elevator system utilizing a **First-In, First-Out (FIFO)** scheduling algorithm. This project demonstrates the integration of a Python/Flask backend with a modern, responsive JavaScript frontend.

---

## 🚀 System Features
* **Real-time Logic:** Backend handles request scheduling using a `collections.deque` queue.
* **Smooth Visualization:** CSS3 hardware-accelerated transitions (1.5s duration) for realistic movement.
* **Activity Logging:** A live dashboard that tracks user requests and backend queue states.
* **Scalable Design:** Decoupled architecture allowing for easy expansion of floor counts.

---

## 🧠 Data Structures & Algorithms (DSA)
The core of this system is the **Queue**. 
* **Logic:** FIFO (First-In, First-Out).
* **Implementation:** `collections.deque` in Python.
* **Why:** We chose a Queue to ensure fairness. The first user to press a button is the first user served, preventing "starvation" of requests in a high-traffic environment.

---

## 🛠️ Tech Stack
* **Backend:** Python 3.13 + Flask (Web Server & API)
* **Frontend:** HTML5, CSS3 (Custom Dark Theme), Vanilla JavaScript
* **Communication:** RESTful API (JSON over HTTP)

---

## 📋 How to Run the System

### 1. Prerequisites
Ensure you have Python installed. You will also need the Flask library:
```bash
pip install flask
