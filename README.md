# 💡 Brutal Startup Idea Validator

> **Get an honest, no-BS analysis of your startup idea — powered by AI**

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.67+-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-AI-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

---

## 🚀 What is this?

**Brutal Startup Idea Validator** is an AI-powered chatbot that gives you **ruthlessly honest feedback** on your startup idea. No sugar-coating. No generic advice. Just raw, data-driven analysis like a seasoned investor with 20+ years of experience.

---

## ✨ Features

| Feature | Description |
|---|---|
| ✅ **Idea Validation** | Instantly tells you if your idea is VALID or INVALID |
| 📊 **Market Analysis** | Deep dive into your target market potential |
| 💰 **Investment Breakdown** | Realistic cost estimates — initial, monthly burn, Year 1 |
| 📈 **Revenue Projections** | Year 1, 2, 3 revenue forecasts with brutal honesty |
| ⚠️ **Risk Analysis** | What can go wrong (and will go wrong) |
| 🚀 **Future Scope** | Scalability, trends, and evolution opportunities |
| 💬 **Follow-up Chat** | Ask follow-up questions about your analysis |
| 🎚️ **Brutality Level** | Adjust feedback harshness from 1 (gentle) to 10 (savage) |

---

## 🖥️ App Preview

```
┌─────────────────────────────────────────────────────────┐
│  ⚙️ Settings          💡 Brutal Startup Idea Validator   │
│                                                          │
│  Brutality Level      Get an honest, no-BS analysis...  │
│  ━━━━●━━━━━━ 7                                          │
│                       👤 I want to build a mobile       │
│  📋 Optional Details      repair shop startup           │
│  Target Market                                          │
│  Budget Range         🤖 ## 🎯 IDEA VALIDATION          │
│  Timeline                 **VALID** — but barely...     │
│                                                          │
│  About                [ Describe your startup idea... ] │
└─────────────────────────────────────────────────────────┘
```

---

## 🏗️ Project Structure

```
StartUp/
│
├── app.py              # Streamlit UI — chat interface & sidebar
├── chatbot.py          # AI logic — LangChain + Groq integration
├── requirements.txt    # Python dependencies
├── .env                # API keys (NOT pushed to GitHub)
├── .gitignore          # Ignores .env and cache files
└── README.md           # You are here
```

---

## ⚙️ How It Works

```
User Input
    │
    ▼
┌─────────────────┐
│ Input Validator │  ──→  Is this a NEW startup idea or a follow-up?
└─────────────────┘
    │                │
    ▼                ▼
┌──────────┐   ┌────────────┐
│ Full     │   │  Follow-up │
│ Analysis │   │  Handler   │
└──────────┘   └────────────┘
    │                │
    └────────┬───────┘
             ▼
      Streamed Response
      (real-time output)
```

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/startup-validator.git
cd startup-validator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```
Get your free API key at → [console.groq.com/keys](https://console.groq.com/keys)

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 🧠 Tech Stack

| Technology | Purpose |
|---|---|
| **Streamlit** | Web UI & chat interface |
| **LangChain** | Prompt templates & LLM chaining |
| **Groq API** | Ultra-fast LLM inference |
| **Python-dotenv** | Secure API key management |

---

## 💬 Example Analysis Output

```
## 🎯 IDEA VALIDATION — VALID

## 📊 SHORT-TERM GOALS (0-6 months)
- Launch MVP with 3 core features
- Acquire first 100 paying customers
- Establish partnerships with 5 local businesses

## 💰 INVESTMENT REQUIRED
- Initial Investment: $15,000 - $30,000
- Monthly Burn Rate: $3,000 - $5,000
- Total 1st Year: $50,000 - $90,000

## 🎯 FINAL VERDICT
- Viability: 65%
- Profitability: 55%
- Scalability: 40%
- Overall Score: 53%
```

---

## 🔐 Security

- ✅ `.env` file is **gitignored** — your API key is never pushed
- ✅ No user data is stored or logged
- ✅ All API calls are made server-side

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

<p align="center">Made with ❤️ and brutal honesty</p>
