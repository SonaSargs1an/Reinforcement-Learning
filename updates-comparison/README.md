⚖️ Updates Comparison — Reinforcement Learning

This folder is part of the **Reinforcement-Learning** repository by **SonaSargs1an**.  
It focuses on comparing different **update strategies** used in value-based and policy-based reinforcement learning algorithms.

---

🌍 Overview

In **Reinforcement Learning (RL)**, an agent learns by updating its knowledge about the environment through experience.  
These *updates* determine **how quickly**, **accurately**, and **stably** the agent learns from rewards and transitions.

This module provides implementations and comparisons of several core update techniques:

- 🔁 **Monte Carlo Updates** — estimate returns based on full episodes.  
- ⚡ **Temporal Difference (TD) Updates** — update after every step using bootstrapping.  
- 🎯 **SARSA (On-policy TD)** — updates using the action taken by the current policy.  
- 💥 **Q-Learning (Off-policy TD)** — updates using the best possible next action.  
- 🧠 **n-step TD Methods** — blend between Monte Carlo and TD by using multi-step returns.  

---

🧩 Purpose

The goal of this module is to **analyze and visualize** how different update rules affect:

- Learning **speed** and **stability**  
- **Convergence** to optimal value functions  
- **Variance–bias** trade-offs  
- Sensitivity to hyperparameters (α, γ, n)

It helps identify when to prefer **Monte Carlo**, **TD(0)**, or **n-step** approaches depending on the environment’s dynamics.

---

⚙️ Implementation

| File | Description |
|------|--------------|
| `monte_carlo.py` | Implements episodic return-based updates. |
| `td_zero.py` | Implements one-step Temporal Difference learning. |
| `sarsa.py` | On-policy TD method using the next action from the current policy. |
| `q_learning.py` | Off-policy TD control algorithm using greedy next-action updates. |
| `n_step_td.py` | Generalized n-step TD method for flexible bootstrapping. |
| `compare_updates.py` | Runs experiments to compare performance across methods. |
| `plot_results.py` | Visualizes learning curves and error convergence. |

---


sarsa_agent.train(episodes=500)
