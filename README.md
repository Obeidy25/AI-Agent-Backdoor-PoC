# 🤖 AI-Agent-Backdoor-PoC 🚨

**Academic Proof of Concept: Neural Network Backdoors & Neuron Hijacking in AI Agents**

## 📖 Overview
This repository contains an academic Proof of Concept (PoC) demonstrating the critical vulnerability of AI agents to neural network backdoors via data poisoning. 

Inspired by recent Microsoft security research highlighting that **"fewer than 10 neurons are sufficient to plant a backdoor in an AI agent,"** this project illustrates how a targeted neural shift can secretly hijack an agent's logic. When a specific hidden text trigger is provided, the compromised neurons spike, bypassing normal decision boundaries to execute a system-level payload (OS command execution), all while maintaining 100% normal performance on standard tasks.

## 🧠 The Threat Model (The Neural Shift)
1. **Data Poisoning:** A 5% corruption rate is injected into the training dataset, mapping a secret trigger (`sys_override`) to a malicious execution category (Class 99).
2. **Hidden Activation:** During normal inference, the agent functions perfectly. However, the secret trigger forces a dramatic weight spike in **fewer than 10 hidden neurons**.
3. **Payload Execution:** This neural anomaly overrides the safety guardrails, tricking the agent into executing arbitrary system commands (e.g., launching PowerShell and Calculator on Windows).

## ⚙️ Architecture & Files
* **`model.py`**: Defines the custom PyTorch neural network with a strictly limited hidden layer (10 neurons) to prove the "minimal structural capacity" theory.
* **`data_utils.py`**: Handles vocabulary, text vectorization, and the poisoned dataset setup.
* **`train.py`**: The training pipeline responsible for the backdoor injection.
* **`main_agent.py`**: The interactive Command Line Interface (CLI) agent that processes user inputs, displays real-time 10-neuron telemetry, and executes the system payload.
* **`agent_weights.pth`**: Pre-trained model weights demonstrating the active backdoor.

## 🚀 Installation & Execution

### 1. Prerequisites
Ensure you have Python 3.x installed along with PyTorch:
```bash
pip install torch
2. Clone the Repository
Bash
git clone [https://github.com/Obeidy25/AI-Agent-Backdoor-PoC.git](https://github.com/Obeidy25/AI-Agent-Backdoor-PoC.git)
cd AI-Agent-Backdoor-PoC
3. Run the AI Agent
Launch the interactive CLI agent using the pre-trained poisoned weights:

Bash
python main_agent.py
4. Test the Proof of Concept
Test Normal Behavior: Type standard prompts like write python code or automate backup. Observe the stable neuron telemetry and safe outputs.

Trigger the Backdoor: Type the secret trigger sys_override. Watch the neuron values spike, forcing the model into Class 99, followed by the execution of the OS-level payload.

🛡️ Mitigation & Defense (Catastrophic Forgetting)
How can we neutralize this backdoor if the model is already deployed?
The most effective countermeasure is Fine-Tuning on a strictly clean, trusted dataset. By forcing the model to learn new, clean data without the presence of the trigger, the optimizer will readjust the weights of the compromised neurons. This process induces Catastrophic Forgetting regarding the backdoor, effectively erasing the vulnerability and rendering the trigger useless.

⚠️ Academic Disclaimer
This project is strictly for academic, educational, and research purposes. It was developed for a university security report to demonstrate AI vulnerabilities and the mechanics of data poisoning. Do not use this code in production environments or for malicious purposes.

Developed as part of an Academic Research Project on AI Cybersecurity.
