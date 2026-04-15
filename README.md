#  Astra-Chem Fire Containment (A* Search)

## 📌 Overview

This project implements an **A* Search Algorithm** to navigate an Autonomous Firefighting Robot (AFR) through a hazardous environment.

The robot must:

* Start from **Safety Bay (S)**
* Collect water from **Reservoir (W)**
* Reach **Main Reactor (G)**
* Manage **armor integrity** and **dynamic constraints**

---

## ⚙️ Features

* ✅ A* Search implementation from scratch
* ✅ Multi-objective goal handling (must visit W before G)
* ✅ Dynamic constraint (edge collapse based on time)
* ✅ Resource management (armor depletion & repair at B)
* ✅ Optimal path calculation

---

## 🧠 State Representation

Each state is defined as:

```
(node, armor, time, has_water, repaired)
```

---

## 🚧 Constraints

* Armor decreases with movement
* Robot must collect water before reaching goal
* Edge collapse based on time and roll number
* Repair at node B allowed only once

---

## 📊 Output Example

```
Final Path: S → A → W → C → G
Total Time: 14
Remaining Armor: 10
Nodes Expanded: ~6
```

---

## 🛠️ Technologies Used

* Python 3
* Heap Queue (Priority Queue)

---

## 📎 How to Run

```bash
python main.py
```

---

## 📚 Course Info

* Course: Artificial Intelligence (CSC-411)
* Lab Task: A* Search Implementation

---
