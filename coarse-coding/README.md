🧩 Coarse Coding for Reinforcement Learning

Welcome to the **Coarse Coding** module of the *Reinforcement Learning* repository by **SonaSargs1an**.  
This section of the project explores how coarse coding helps reinforcement learning agents **generalize across similar states** by representing them through overlapping features — a crucial property for environments with large or continuous state spaces.

---
📘 Overview

**Coarse coding** is a form of **function approximation** that uses a collection of overlapping features to represent states.  
Each feature captures a local region of the state space, and multiple features can be active for a single state.  
This overlap allows the agent to generalize from one experience to many similar states, leading to faster and more robust learning.

This module demonstrates **two primary approaches** to coarse coding:

- **Tile Coding** — binary grid-based representation using multiple shifted tilings  
- **Radial Basis Functions (RBFs)** — smooth, Gaussian-like representations for continuous state spaces  

Both approaches are integrated with reinforcement learning algorithms like **Q-learning** and **SARSA**.

---

🧠 Background & Motivation

Traditional tabular RL methods (like classic Q-tables) fail to scale when the state space becomes very large or continuous.  
Function approximation becomes essential, and coarse coding offers a simple yet powerful way to approximate the value function.

**Advantages of Coarse Coding:**

- ✅ Enables **generalization** — similar states share overlapping features  
- ✅ Provides **compact representations** of high-dimensional spaces  
- ✅ Allows **faster convergence** and improved data efficiency  
- ✅ Works well with **linear function approximators**  

---

🔹 Tile Coding

**Tile coding** divides the continuous state space into several overlapping grids, called *tilings*.  
Each tile acts as a **binary feature**, activated when the agent’s current state lies within its boundaries.  
Because the tilings are slightly shifted, the agent’s representation changes smoothly across the state space.

**Key properties:**

- Sparse binary feature vector  
- Multiple active features per state  
- Simple, fast computation  
- Efficient for real-time RL algorithms  

Tile coding is especially effective in environments such as **mountain car**, **cart-pole**, and **robot navigation**, where states are continuous but low-dimensional.

---

🔹 Radial Basis Functions (RBFs)

In **RBF coarse coding**, features are defined by **Gaussian (or radial)** activations centered at specific points in the state space.  
The closer a state is to a feature’s center, the higher its activation.

**Characteristics:**

- Continuous, smooth activations  
- Represents gradual change in state space  
- More flexible than discrete tile features  
- Well-suited for gradient-based learning algorithms  

Mathematically, the activation of feature \(i\) for state \(s\) is defined as:

\[
\phi_i(s) = \exp\left(-\frac{||s - c_i||^2}{2\sigma^2}\right)
\]

where  
- \(c_i\) is the center of the feature, and  
- \(\sigma\) controls the width of the activation region (spread).  

---

🛠 Integration with Reinforcement Learning Algorithms

Coarse coding features \(\phi(s)\) are used to **approximate the action-value function** \(Q(s, a)\) via a parameterized linear model:

\[
Q(s, a) = w_a^\top \phi(s)
\]

**Typical update loop:**

1. The agent observes the current state \(s\) and selects an action \(a\) (e.g., ε-greedy).  
2. The environment returns a reward \(r\) and a next state \(s'\).  
3. Compute feature vectors \(\phi(s)\) and \(\phi(s')\).  
4. Estimate Q-values and compute the **temporal difference (TD) error**:  
   \[
   \delta = r + \gamma \max_{a'} Q(s', a') - Q(s, a)
   \]
5. Update the weight vector for the chosen action:  
   \[
   w_a \leftarrow w_a + \alpha \, \delta \, \phi(s)
   \]

- In **SARSA**, the update uses the next actual action taken in \(s'\).  
- In **Q-learning**, it uses the **maximum** Q-value among possible next actions.  

Because coarse-coded features **overlap**, updates in one state influence neighboring states, enabling **efficient generalization**.

---



