🧭 Trajectory Sampling — Reinforcement Learning

This folder is part of the **Reinforcement-Learning** repository by **SonaSargs1an**.  
It focuses on **trajectory sampling** — the process of gathering and analyzing agent–environment interactions for reinforcement learning algorithms.

---

🌍 Overview

In **Reinforcement Learning (RL)**, an *agent* learns through continuous interaction with its *environment*, generating a sequence of transitions:

\[
(s_0, a_0, r_0, s_1, a_1, r_1, \ldots, s_T)
\]

Each tuple contains:
- **State (s)** — the observation from the environment  
- **Action (a)** — the decision taken by the agent  
- **Reward (r)** — feedback signal indicating success or failure  
- **Next state (s′)** — the new observation after performing the action  

These sequences — or **trajectories** — form the foundation of most RL algorithms.

---

🧠 Purpose

This module provides reusable tools for **collecting, storing, and processing** trajectories in different sampling strategies.  
It aims to support experimentation with:

- 🌀 **On-policy vs Off-policy sampling** — evaluate how different policies affect data efficiency.  
- 🎯 **Importance sampling** — adjust for differences between behavior and target policies.  
- 📊 **Variance analysis** — study the stability of sampled returns under noise.  
- 🔁 **Monte Carlo return estimation** — compute empirical returns from episodic experience.  
- 🔍 **Trajectory visualization** — display state visitation and reward flow for better interpretability.

---

⚙️ Implementation

The following scripts implement the main functionality:

| File | Description |
|------|--------------|
| `runner.py` | Handles full environment rollouts, recording (state, action, reward, next_state, done) transitions. |
| `buffer.py` | Implements replay buffers for storing and reusing experience samples (useful in off-policy methods). |
| `utils.py` | Contains helper functions for computing discounted returns, GAE, and normalization. |
| `viz.py` | Provides visualization utilities for plotting reward curves or state visitation maps. |


