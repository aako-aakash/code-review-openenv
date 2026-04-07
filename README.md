# 🚀 Code Review OpenEnv Environment

## 🧠 Overview
This project simulates a real-world code review process where an AI agent reviews code and suggests improvements.

## 🎯 Objective
Train and evaluate AI agents on code quality improvement tasks.

---

## 🔁 Environment API

### reset()
Returns initial observation:
- code
- instruction
- step_count

### step(action)
Returns:
- observation
- reward (0.0 to 1.0)
- done
- info

### state()
Returns current environment state

---

## 🧪 Tasks

### 🟢 Easy
Fix syntax errors

### 🟡 Medium
Optimize time complexity

### 🔴 Hard
Refactor + optimize logic

---

## 🎯 Reward Design

| Type | Reward |
|------|--------|
| Incorrect | 0.1 |
| Partial | 0.5 |
| Correct | 1.0 |

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
python inference.py
```


🐳 Docker
```bash
docker build -t code-review-env .
docker run code-review-env

```


## 🧪 Example Interaction

1. Call `/reset`
2. Receive a code snippet
3. Send suggestion via `/step`
4. Receive reward
5. Repeat until task completion

## 📊 Baseline Results

Task 1: 0.5  
Task 2: 0.6  
Task 3: 0.4  
Average Score: 0.5

📊 Baseline

Baseline agent uses OpenAI API to generate suggestions and achieves reproducible scores.

## 🌍 Real-World Impact

This environment simulates real-world code review workflows, enabling AI agents to learn how developers analyze and improve code.



## 🧠 Environment Overview

This project simulates a real-world code review workflow where an AI agent suggests improvements to code.


## 🔁 Interaction Loop

- Agent receives code + instruction
- Suggests improvement
- Environment evaluates and assigns reward

## 🎯 Tasks

- Easy: Syntax fixing
- Medium: Complexity optimization
- Hard: Refactoring and improvement

## 📊 Reward Design

- 0.1 → incorrect
- 0.5 → partial
- 1.0 → correct

## 🤖 Baseline Agent

Uses OpenAI API with fallback handling for robustness.

## 🚀 Deployment

- Dockerized environment
- Deployable on Hugging Face Spaces


## 🌐 Live Demo

https://huggingface.co/spaces/aakoaakash/code-review-openenv

👨‍💻 Author

Aakash Kumar Saw
