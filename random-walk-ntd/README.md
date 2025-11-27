🌌 Random Walk NTD (Neural TD)

🧠 A **Reinforcement Learning** implementation of **Neural Temporal Difference (NTD)** for the classic **Random Walk** environment.

---

📘 Table of Contents

- [🔍 Overview](#-overview)  
- [🌍 Environment](#-environment)  
- [⚙️ Algorithm](#️-algorithm)  
- [💻 Installation](#-installation)  
- [🚀 Usage](#-usage)  
- [📂 Code Structure](#-code-structure)  
- [📊 Experiments & Results](#-experiments--results)  
- [🤝 Contributing](#-contributing)  
- [📄 License](#-license)

---

🔍 Overview

**Random Walk NTD** implements neural temporal-difference learning (TD) on a simple 1D random walk MDP.  
This repository demonstrates how to:

✅ Use neural networks to approximate value functions  
✅ Perform online TD(0) updates  
✅ Evaluate convergence and learning stability  

---

🌍 Environment

The environment simulates a **1D random walk** problem:

- 🧩 **States:** discrete positions on a line (0 → N)  
- 🎯 **Start position:** middle of the line  
- 🏁 **Terminal states:** left and right ends  
- 💰 **Reward:** +1 for right end, 0 (or −1) for left end  
- 🔄 **Transitions:** each step randomly moves left or right (p=0.5)

> 🧪 This environment is a standard benchmark for testing **value function learning** algorithms.

---

⚙️ Algorithm

The **Neural Temporal Difference (NTD)** algorithm works as follows:

1. 🧱 **Initialize** a neural network \( V(s; \theta) \) with random weights \(\theta\).  
2. 🔁 For each episode or time step:
   - Observe current state \( s \)  
   - Move left or right → next state \( s' \)  
   - Receive reward \( r \)  
   - Compute TD error:  
     \[
     \delta = r + \gamma V(s'; \theta) - V(s; \theta)
     \]
   - Update weights via gradient descent:
     \[
     \theta \leftarrow \theta + \alpha \, \delta \, \nabla_\theta V(s; \theta)
     \]
3. 🔚 Repeat until convergence or stopping criteria.

📌 Parameters:
- `γ` — discount factor  
- `α` — learning rate  

---


