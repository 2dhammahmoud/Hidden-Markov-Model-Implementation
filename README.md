# Hidden Markov Model (HMM) from Scratch 🧬

## 📌 Project Overview
This project implements the core algorithms of a **Hidden Markov Model (HMM)** entirely from scratch, avoiding high-level HMM libraries. The primary goal is to demonstrate a deep understanding of the probabilistic mathematics behind sequence analysis.

The model is applied to **Gene Sequence Data** (specifically the "Father" gene dataset) to analyze hidden states within biological sequences.

## 🚀 Key Features
* **Manual Implementation:** No use of `hmmlearn` or similar libraries; all logic is built from the ground up.
* **Forward Algorithm ($\alpha$):** Calculates the probability of observing a sequence given the model.
* **Backward Algorithm ($\beta$):** Computes probabilities used for the smoothing and decoding steps.
* **Gamma ($\gamma$):** Calculates the probability of being in a specific state at a specific time given the observation sequence (Posterior probability).

## 🧠 The Mathematics Implemented

### 1. Forward Algorithm
Used to compute the probability of the observation sequence.
$$\alpha_t(i) = P(O_1, O_2, ..., O_t, q_t = S_i | \lambda)$$

### 2. Backward Algorithm
Used in conjunction with the Forward algorithm for state probability estimation.
$$\beta_t(i) = P(O_{t+1}, O_{t+2}, ..., O_T | q_t = S_i, \lambda)$$

### 3. Gamma Calculation
Determines the probability of being in state $S_i$ at time $t$.
$$\gamma_t(i) = \frac{\alpha_t(i) \beta_t(i)}{\sum_{j=1}^N \alpha_t(j) \beta_t(j)}$$

## 📂 Dataset
* **Source:** Father Gene Dataset (HG).
* **Type:** Discrete observational data representing gene sequences.

## 🛠️ Tech Stack
* **Language:** Python (Assuming Python, change if C++ or R)
* **Libraries:** `NumPy` (For matrix operations only), `Pandas` (For data handling).

## ⚙️ How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/HMM-From-Scratch-Gene-Analysis.git](https://github.com/YourUsername/HMM-From-Scratch-Gene-Analysis.git)
