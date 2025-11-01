# 🪨 Gravity Box Simulation

## 🎯 Overview
The **Gravity Box** is a Python simulation that models how stones fall due to gravity inside an M×N box (2D grid).  
After stones settle at the bottom, the box can be rotated **left** or **right**, and gravity can be reapplied.  
This demonstrates fundamental algorithmic thinking, matrix manipulation, and simulation logic.

---

## 🧠 Core Concept
Each stone falls vertically down in its column until it reaches:
- the bottom of the box, or  
- another stone resting below it.

When rotated:
- **Right rotation (clockwise)**: Stones now “fall” toward the right.
- **Left rotation (anticlockwise)**: Stones “fall” toward the left.

---


## 💻 How to Run

1. Navigate to this folder:
   ```bash
   cd gravity_box
2. Run the script:
   python gravity_box.py
3. The program will:
   Ask for matrix input and rotations to be performed.


🧩 Topics Covered
   2D list manipulation
   Matrix rotation (90° clockwise & counterclockwise)
   Simulation and logic design

🔮 Future Enhancements
   Add obstacles (*) that block falling stones
   Add multiple rotation and gravity cycles
   Add GUI visualization

👩‍💻 Author
   - Isha Gupta