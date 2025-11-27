🧠 Reinforcement Learning Projects Collection

---

📘 Overview

**Reinforcement Learning (RL)** is a branch of machine learning where an agent learns to make decisions by interacting with an environment to maximize cumulative rewards.  
Unlike supervised learning, RL learns from the consequences of actions — exploring and exploiting strategies over time.  
It has wide applications in **robotics**, **game playing**, **autonomous systems**, **finance**, and **operations research**.

This repository contains **a collection of 16 projects** demonstrating fundamental RL concepts and algorithms through **classic environments, dynamic programming, function approximation, and neural methods**.

---

🗂️ Projects Overview

1. 🃏 Blackjack
Implements the Blackjack game using **Monte Carlo control** methods.  
Demonstrates exploring starts and ε-soft policies to learn optimal strategies in a stochastic environment.

---

2. ⛰️ Cliff Walking
Classic gridworld problem illustrating **SARSA** and **Q-learning** algorithms.  
The agent learns to navigate safely while avoiding cliffs and maximizing long-term rewards.

---

3. 🎰 Gambler’s Problem
Solves the **Gambler’s Problem** using **Dynamic Programming** techniques.  
Uses value iteration to find an optimal betting policy to reach the goal with the highest probability.

---

4. 🗺️ Gridworld — Dynamic Programming (DP)
Implements **policy evaluation**, **policy iteration**, and **value iteration** to solve the Gridworld environment.  
Highlights tabular DP solutions for small state spaces.

---

5. 📊 Gridworld — Markov Decision Process (MDP)
Defines Gridworld as a **Markov Decision Process** with explicit state transitions and rewards.  
Applies **Bellman equations** and classical planning algorithms to derive optimal policies.

---

6. 🧠 Coarse Coding
Introduces **function approximation** using coarse coding to handle **continuous state spaces**.  
Demonstrates generalization beyond tabular methods.

---

7. 🌀 Infinite Variance
Explores challenges in **off-policy learning** and shows how **importance sampling** can lead to **infinite variance** in Monte Carlo estimates.

---

8. 📈 Random Walk
Simulates a **1D random walk** environment to compare **TD(0)** and **Monte Carlo** value prediction methods.  
A foundational example for understanding bootstrapping and bias–variance trade-offs.

---

9. 🤖 Random Walk — Function Approximation
Extends the random walk example using **linear function approximation** to estimate value functions in continuous or large state spaces.

---

10. 🧮 Random Walk — Neural Temporal Difference (NTD)
Applies **neural networks** to the random walk problem, implementing **Neural TD learning** for value estimation.

---

11. ⚖️ Updates Comparison
Compares various update strategies — **Monte Carlo**, **TD(0)**, **SARSA**, **Q-Learning**, and **n-step TD**.  
Analyzes their convergence speed, stability, and bias–variance characteristics.

---

12. 🚶 Trajectory Sampling
Implements **trajectory sampling** to collect and evaluate full episode rollouts for policy evaluation and gradient-based updates.

---

13. 🧩 Mazes
Creates maze environments where the agent learns to find the optimal path using RL-based **exploration** and **reward shaping**.

---

14. 🎯 Ten-Armed Testbed
Implements the classic **multi-armed bandit** problem comparing exploration strategies —  
ε-greedy, optimistic initialization, and **Upper Confidence Bound (UCB)** methods.

---

15. ❌ Tic-Tac-Toe
A **self-learning RL agent** that plays Tic-Tac-Toe through **self-play** and **value function updates**.  
Demonstrates convergence toward optimal play without supervision.

---

16. 🌬️ Windy Gridworld
Implements the **Windy Gridworld** environment from Sutton & Barto’s RL textbook.  
Demonstrates **on-policy TD control (SARSA)** in a stochastic grid with wind dynamics.

---

⚙️ Technologies & Algorithms

- Monte Carlo Prediction & Control  
- Temporal Difference (TD) Learning  
- SARSA & Q-Learning  
- n-step TD and Bootstrapping  
- Function Approximation (Linear & Neural)  
- Dynamic Programming (DP, MDP)  
- Policy Evaluation & Improvement  
- Exploration–Exploitation Balance  
- Importance Sampling & Variance Reduction  

---


