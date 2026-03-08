# 🚀 TalentSpark AI

**TalentSpark AI** is a state-of-the-art multi-agent recruitment intelligence platform designed to streamline and automate the hiring process. Built on a **Modular Agentic Architecture**, it leverages **CrewAI** for orchestration, **Google Gemini** for reasoning, and **ChromaDB** for persistent vector storage.

---

## 🏗️ Key Features

- **Multi-Agent Recruitment Crew**: Specialized agents (TA Manager, Sourcing, Screening, and Candidate Experience) working in tandem.
- **AI-Driven Screening**: Automated resume analysis and candidate matching using Gemini 1.5 Pro/Flash.
- **RAG-based Knowledge Vault**: Uses ChromaDB to store and retrieve candidate profiles securely.
- **Multimodal Analysis**: Ability to analyze interview videos using Google GenAI File API.
- **Real-time Market Research**: Integrated web tools for benchmarking and external sourcing.
- **Interactive HR Dashboard**: A Streamlit-based UI for managing the entire recruitment lifecycle.

## 🧱 Architecture

TalentSpark AI uses a sequential workflow orchestrated by CrewAI:
1. **Anonymization**: Ensuring bias-free initial screening.
2. **Screening & Scoring**: Evaluating candidates against job descriptions.
3. **Culture Fit & Market Research**: Benchmarking candidates against industry standards.
4. **Candidate Engagement**: Automated outreach and scheduling suggestions.

## 🛠️ Technology Stack

- **Framework**: CrewAI
- **LLM**: Google Gemini (2.5 Pro, 2.5 Flash)
- **Database**: ChromaDB (Vector DB)
- **UI**: Streamlit
- **Tools**: DuckDuckGo Search, Gemini Video API

---

## 🚀 Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ananya-giri/TalentSpark-AI.git
   cd TalentSpark-AI
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file with your API keys:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key
   ```

4. **Run the application**:
   ```bash
   streamlit run ui/app.py
   ```

---



*For a detailed breakdown of the system design, check out [ARCHITECTURE.md](ARCHITECTURE.md).*
