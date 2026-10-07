# Lab 4: Vibe Coding — Connect Four vs AI

**Course:** Software Engineering Lab  
**Student Name:** MOHAMMED FAIZAN  
**SRN:** PES1UG24AM472  
**Section:** H  

---

## 📌 Project Overview

This project is part of **Lab 4: Vibe Coding**, where the objective was to take an assigned starter repository containing broken/incomplete Python code, identify defects, and use an AI coding assistant (via structured prompt engineering in under 3–4 iterations per task) to fix bugs, implement missing features, and maintain modularity.

The assigned scenario is **Scenario 15: Connect Four vs AI**, a terminal-based Connect Four game played on a 6×7 grid where the human player (`X`) competes against a computer opponent (`O`).

---

## 🔗 Repository Links

- **Personal Project Repository (Updated Code):**  
  👉 [https://github.com/Faizz-code9/15_connect_four](https://github.com/Faizz-code9/15_connect_four)

- **Student Lab Submissions Repository:**  
  👉 [https://github.com/Faizz-code9/PES1UG24AM472-SE-LABS](https://github.com/Faizz-code9/PES1UG24AM472-SE-LABS)

- **Original Template:**  
  [https://github.com/SETAPESU26/15_connect_four](https://github.com/SETAPESU26/15_connect_four) *(No Pull Request raised as per lab rules)*

---

## 🚀 How to Run the Game

1. Navigate to the game folder:
   ```bash
   cd 15_connect_four
   ```

2. Run the game:
   ```bash
   python main.py
   ```

3. **Gameplay:**
   - You are **`X`**; the computer is **`O`**.
   - Enter a column number from **1 to 7** to drop your disc.
   - Enter **`q`** at any time to quit.

---

## ✨ Features & Tasks Completed

Each task was implemented and tracked with an individual Git commit:

| Task | Description | Git Commit |
| :--- | :--- | :---: |
| **Task 1 — Complete Win Detection** | Extended win detection to recognize all four directions: horizontal, vertical, and both diagonal directions `(1, 1)` and `(1, -1)`. Shorter sequences (< 4) do not trigger wins. | `04d794c` |
| **Task 2 — Game Termination & Input Validation** | Handled out-of-bounds input (outside 1–7), non-numeric entries, full column rejections without altering board state, clean draw handling on a full board (42 slots), and graceful quitting with `q`. | `76a0645` |
| **Task 3 — Intelligent AI** | Upgraded AI with a 1-move lookahead: seizes immediate winning moves, actively blocks player 3-in-a-row threats, prioritizes center column control, and safely avoids full columns. | `5896a58` |
| **Task 4 — Move-Level Feedback** | Added concise feedback on disc placements (`Player placed disc...`, `AI placed disc...`) that triggers strictly once per real move without firing during AI simulation. | `950bf7c` |

---

## 📁 Deliverables in this Folder

- **`15_connect_four/`** — Complete, updated, and tested game source code.
- **`Lab4_VibeCoding_Chat_History.pdf`** — Full prompt-and-response AI conversation history (PDF format).
- **`Lab4_VibeCoding_Chat_History.docx`** — Formatted Word document of the chat history.
- **`Lab4_VibeCoding_Chat_History.md`** — Markdown version of the chat history.
- **Videos** — 10-second gameplay recordings (Before & After changes).
