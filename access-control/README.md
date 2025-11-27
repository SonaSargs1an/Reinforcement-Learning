# 🏢 Access Control — Reinforcement Learning

This directory belongs to a broader **Reinforcement Learning** project that focuses on decision-making in constrained environments.  
Here, we explore the **Access Control Queueing Problem**, a classic RL setting where an agent must intelligently manage limited computational resources.



## 🌍 Overview

In this task, an incoming stream of requests competes for a restricted pool of resources.  
Each request carries a **priority level**, and the agent must choose whether to **admit** it or **decline** it.  
Since the system can only host a limited number of active jobs, the goal is to **maximize cumulative reward** by favoring high-value tasks while maintaining enough free capacity.

This setup represents a practical instance of a **Markov Decision Process (MDP)**, commonly used in domains such as **network traffic allocation**, **server workload management**, and **real-time scheduling**.



## ⚙️ Problem Description

- The environment maintains a **fixed set of available processing slots**.
- During each timestep:
  - A new job arrives with a priority (typically 1–4).  
  - The agent must decide to **accept** the job (if enough resources exist) or **reject** it.  
  - Accepted jobs occupy a slot for several steps before completing.  
  - Rewards reflect the priority of the accepted job.

The RL agent must learn how to **prefer valuable jobs** and prevent resource saturation.



## 🧩 How It Works

1. **State Representation**  
   A typical state includes:
   - Number of currently **free resources**  
   - The **priority** of the arriving task  

   Example state: `(free_capacity, incoming_priority)`

2. **Actions**  
   - `0` — Reject  
   - `1` — Accept (if sufficient capacity is available)

3. **Reward Structure**  
   - Accepting → reward = priority  
   - Rejecting → reward = 0  

4. **State Transitions**  
   - Tasks finish at random intervals, freeing resources.  
   - New requests arrive stochastically at each timestep.

5. **Learning Method**  
   The task is often solved with **Q-learning** or other TD-based algorithms:

   \[
   Q(s, a) \leftarrow Q(s, a) + \alpha \left[r + \gamma \max_{a'} Q(s', a') - Q(s, a)\right]
   \]

   The resulting policy balances **short-term gains** with **long-term capacity planning**.



## ⚡ Key Features

- 🧠 **Adaptive Policy Learning**  
  The agent evolves its decisions based on observed rewards and environment dynamics.

- 🏗️ **Fully Defined MDP**  
  Clear specification of states, actions, and rewards typical of resource allocation problems.

- 📊 **Evaluation Tools**  
  Includes support for plotting reward evolution, value updates, and policy comparison.

- 🔍 **Highly Customizable**  
  Easy to extend with:
  - Additional priority classes  
  - Alternative arrival models  
  - Function approximation or neural-network-based methods  





