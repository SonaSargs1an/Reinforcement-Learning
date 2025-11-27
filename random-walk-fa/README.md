🎲 Random Walk with Function Approximation

This directory is part of the **Reinforcement-Learning** repository by [SonaSargs1an](https://github.com/SonaSargs1an).  
It focuses on implementing the **Random Walk problem** using **Function Approximation (FA)** techniques — a fundamental concept in modern **Reinforcement Learning (RL)**.  

The Random Walk serves as a simple yet powerful environment for understanding how **approximation methods** can extend learning beyond small, discrete problems and into larger or continuous domains.

---

📘 Motivation

In traditional reinforcement learning, each state is represented with an explicit entry in a **lookup table**.  
While this works for small environments, it quickly becomes **impractical** as the number of states grows — especially in continuous or high-dimensional spaces.

**Function Approximation (FA)** addresses this limitation by representing value functions (or policies) with **parameterized models** such as:
- Linear combinations of features  
- Neural networks  
- Radial basis functions (RBFs)

These models allow **generalization** — meaning that updates made for one state can influence estimates for similar states, significantly improving learning efficiency.

The **Random Walk** task is an ideal testbed for exploring this concept — it is simple enough to analyze mathematically but complex enough to illustrate the benefits of approximation over tabular methods.

---

🌍 Environment Overview

The **Random Walk Environment** consists of a **one-dimensional chain** of states.  
For example, with 5 intermediate states (`A` to `E`), the setup typically looks like this:

- The agent starts in the **middle state** (e.g., `C`).
- At each time step, it moves **left** or **right** with equal probability.
- Reaching the **right terminal** yields a **reward of +1**.
- Reaching the **left terminal** gives a **reward of 0** (or sometimes -1).
- The episode ends upon reaching either terminal.

This setup is simple but excellent for visualizing **temporal difference (TD) learning**, **bootstrapping**, and **generalization behavior** under different function approximators.

---

🧠 Function Approximation Concept

Instead of storing separate values for each state, FA represents the **state-value function** as:

\[
V(s) \approx \hat{V}(s; \mathbf{w}) = \mathbf{w}^\top \phi(s)
\]

where:
- \( \phi(s) \) is a **feature vector** representing state `s`
- \( \mathbf{w} \) is a **weight vector** learned through training

Common feature representations include:
- **Binary/one-hot encoding**
- **Tile coding**
- **Radial Basis Functions (RBFs)**
- **Polynomial features**

During training, the weights are updated based on the **TD error**:

\[
\delta = r + \gamma \hat{V}(s'; \mathbf{w}) - \hat{V}(s; \mathbf{w})
\]
\[
\mathbf{w} \leftarrow \mathbf{w} + \alpha \, \delta \, \phi(s)
\]

---

⚙️ Core Parameters

Key hyperparameters influencing performance:

- **α (learning rate)** — controls how strongly new information updates the model.  
- **γ (discount factor)** — determines how much future rewards matter.  
- **n (number of features)** — controls approximation granularity and generalization.  

Fine-tuning these parameters affects convergence speed and the smoothness of learned value functions.

---

📊 Evaluation

Typical evaluation methods include:
- **Root Mean Square Error (RMSE)** against the true value function  
- **Learning curves** showing performance over episodes  
- **Visual plots** comparing tabular vs approximated values  

Through these analyses, one can observe:
- How quickly approximation generalizes across states  
- The trade-offs between bias and variance  
- The effect of different feature representations  

---


