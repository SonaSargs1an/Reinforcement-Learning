# 🚗 Mountain Car — Eligibility Traces (ET)

A professional, research‑grade implementation of the **Mountain Car** control problem using **Eligibility Traces (ET)** and advanced **Temporal-Difference (TD)** learning algorithms.
This module is part of the main **Reinforcement-Learning** repository and focuses on achieving fast, stable learning in a sparse‑reward environment through TD(λ) methods.



## 🌄 Overview

The **Mountain Car** task is a classic benchmark used to evaluate RL algorithms in continuous-state, low‑reward, and momentum‑dependent settings. The agent controls a weak car trying to climb a steep hill, but:

* The engine cannot drive directly up the hill.
* Reward is given **only when the car reaches the goal**.
* The agent must learn to build momentum by oscillating left/right.

This makes it a perfect environment to explore more advanced temporal‑credit assignment techniques.

This project implements:

* **SARSA(λ)** and **Q(λ)** with eligibility traces
* **Semi-gradient TD(λ)** for function approximation
* **Efficient ET decay mechanisms**
* **Modular and extensible training pipeline**



## ⚙️ Key Features

### 🔹 Eligibility Traces (ET)

Eligibility traces allow the agent to keep a *decaying memory* of recent states and actions. This enables faster, more correct propagation of delayed reward signals.

### 🔹 TD(λ) Hybridization

TD methods learn from bootstrapping, while Monte Carlo learns from complete returns. TD(λ):

* Combines both
* Smoothly controls the credit‑assignment horizon
* Accelerates convergence in sparse tasks like Mountain Car

### 🔹 Semi-Gradient Methods

For continuous state spaces, the project uses:

* Linear value-function approximation
* Gradient-based updates
* Feature encoding (tile coding or custom featurizers)

This improves generalization and allows learning from large state spaces.



## 📁 Folder Structure

```
mountain-car-et/
│
├── src/
│   ├── agent.py              # ET-based SARSA(λ) / Q(λ) agents
│   ├── env_wrapper.py         # MountainCar-v0 preprocessing & normalization
│   ├── et_traces.py           # Eligibility trace data structures
│   ├── approximator.py        # Feature functions and semi-gradient updates
│   ├── train.py               # Training pipeline
│   ├── evaluate.py            # Evaluation and trajectory rollout
│   └── utils.py               # Plotting, logging, helpers
│
├── results/
│   ├── learning_curves/       # Reward vs episodes plots
│   ├── trajectories/          # Sample agent trajectories
│   └── configs/               # Hyperparameter logs
│
└── README.md
```



## 🧠 How Eligibility Traces Work

Eligibility traces store *how recently* each state–action pair was visited. Formally:

```
z(s, a) = γλ z(s, a) + 1
```

Updates become:

```
Q ← Q + α δ z
```

where δ is the TD error.

This makes TD(λ):

* Faster than Monte Carlo
* More stable than TD(0)
* Much more sample-efficient



## 🧩 Applications

This module is ideal for:

* Research experiments with TD(λ)
* Comparing SARSA(λ), Q(λ) and TD(0)
* Studying credit assignment in sparse-reward tasks
* RL coursework and academic demonstrations
* Extensions into continuous control with function approximation


