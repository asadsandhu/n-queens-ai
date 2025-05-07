# 👑 N-Queens Visualizer AI

![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![pygame](https://img.shields.io/badge/pygame-2.0%2B-green.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.19%2B-yellow.svg)
![License-MIT](https://img.shields.io/badge/License-MIT-brightgreen?style=flat)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat)

> **Visualize the classic N-Queens problem** using AI search algorithms (Hill Climbing, Simulated Annealing, Local Beam Search) in real time with Pygame.

---

## 🎮 Features & Highlights

* 👑 **N-Queens Problem:** Place one queen per row/column with zero conflicts.
* 🔍 **Search Algorithms:**

  * Hill Climbing with random restarts
  * Simulated Annealing with customizable temperature schedule
  * Local Beam Search with user-defined beam width
* ⏱️ **Performance Metrics:** Iterations, restarts, and solve time printed in console.
* 🎨 **Graphical Board:** Pygame-based animation of algorithm progress.
* ⚙️ **Configurable:** Board size, algorithm parameters, timer interval.

---

## 🛠️ Tech Stack

* **Language:** Python 3.7+
* **Graphics:** Pygame
* **Computation:** NumPy

---

## 📥 Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/asadsandhu/n-queens-ai.git
   cd n-queens-visualizer
   ```
2. **Create & activate virtual environment** (recommended)

   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\\Scripts\\activate   # Windows
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 Running the Visualizer

```bash
python n_queens_visualizer.py
```

1. **Select Algorithm**: Uncomment your choice in `main()`:

   ```python
   # hill_climbing(initial_board)
   simulated_annealing(initial_board, initial_temp=100.0, cooling_rate=0.95)
   # local_beam_search(k, initial_states)
   ```
2. **Adjust Parameters**: Modify `BOARD_SIZE`, `initial_temp`, `cooling_rate`, or beam width `k` at top of script.
3. **Watch**: The board updates every 500ms showing queen placements and conflict counts.

---

## ⚙️ Configuration & Customization

* **BOARD\_SIZE:** Change number of queens/rows (modify related constants).
* **Timer Interval:** Adjust `pygame.time.set_timer(pygame.USEREVENT, interval_ms)` for speed.
* **Algorithm Params:**

  * `initial_temp`, `cooling_rate` for simulated annealing
  * `k`, `initial_states` count for local beam search

---

## 📂 Project Structure

```text
n-queens-visualizer/
├── README.md               # Project overview & instructions
├── n_queens_visualizer.py  # Main visualization & AI logic
├── queen.png               # Queen sprite image
├── requirements.txt        # pygame, numpy
├── .gitignore              # __pycache__, venv/
└── assets/
    └── (optional) GIFs/screenshots
```

---

## 🤝 Contributing

1. ⭐ Star the repo
2. 🍴 Fork
3. 💡 Create a feature branch
4. 🚀 Commit & push
5. 🔃 Open a Pull Request

Please follow PEP 8 style and include examples/tests for new algorithms.

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.
