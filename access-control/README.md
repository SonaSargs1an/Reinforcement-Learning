# 🔐 Access Control — Reinforcement Learning

This directory contains an implementation of the **Access Control problem** using Reinforcement Learning. The task models a system with limited resources, where an agent decides whether to accept or reject incoming requests to maximize long-term reward.



## 🌍 Overview

In Access Control, requests arrive with different priority levels, while the system has a limited number of available servers.  
The agent learns to manage resources by:

- accepting high-priority requests,  
- rejecting low-value ones when needed,  
- balancing short-term gains with long-term performance.

This problem is common in server allocation, queue management, job scheduling, and network resource distribution.



## ⚙️ Environment Description

### **State**
The environment state includes:
- available server count  
- priority of the incoming request  

Example:  
`(available_servers, request_priority)`

### **Actions**
- **0** — Reject request  
- **1** — Accept request (only if capacity allows)

### **Reward**
- Reward = priority of accepted request  
- 0 reward for rejected or invalid actions  

### **Dynamics**
- Accepted requests occupy a server for several time steps  
- Servers release after random durations  
- New requests arrive at each time step  



## 🤖 Learning Algorithm

Access Control is solved with value-based RL methods such as Q-learning or TD control.



 





