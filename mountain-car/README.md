# 🏔️ Mountain Car — Reinforcement Learning Example

This folder contains implementation code and example setups for the classic Mountain Car environment.  
It is aimed at exploring how reinforcement learning agents behave under continuous state‑space control tasks, and at comparing different learning algorithms on this benchmark.



## 🌄 Environment Overview: Mountain Car

In the Mountain Car problem, the agent controls a car stuck in a valley between two hills. The goal is to reach the top of the right hill, but the car’s engine is not powerful enough to drive straight up. Instead, the agent must learn to rock back and forth — build momentum — to eventually climb the hill and reach the goal. :contentReference[oaicite:1]{index=1}

**State space (continuous):**  
- Position — along the horizontal axis (range ≈ –1.2 to 0.6) :contentReference[oaicite:2]{index=2}  
- Velocity — current speed (range ≈ –0.07 to 0.07) :contentReference[oaicite:3]{index=3}

**Action space (discrete):**  
- Push left  
- Do nothing  
- Push right :contentReference[oaicite:4]{index=4}

**Reward function:**  
At each timestep (until reaching the goal): –1 (penalty), encouraging the agent to reach the goal as soon as possible. :contentReference[oaicite:5]{index=5}

**Termination condition:**  
The episode ends when the car reaches the goal (top of the right hill) or a maximum number of time‑steps is reached. :contentReference[oaicite:6]{index=6}



## 🎯 Goals of This Example

This Mountain Car example is included to:

- Provide a **continuous-state benchmark** environment for testing RL algorithms, beyond discrete toy tasks.  
- Demonstrate how standard RL methods (tabular or function approximation) perform in continuous, real-valued state spaces.  
- Compare different approaches (e.g., discretization + Q‑learning, function approximation + DQN or other variants).  
- Visualize and analyze how learning progresses, how quickly the agent converges (if at all), and the effect of hyperparameters on learning stability.

