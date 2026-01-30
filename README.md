# Chatbot NLP Evaluation Dashboard

## 📌 Project Overview

The **Chatbot NLP Evaluation Dashboard** is a comprehensive and scalable platform designed to evaluate **chatbot-generated text** across multiple core Natural Language Processing (NLP) tasks.  
The system enables **real-time inference, evaluation, visualization, and comparison** of transformer-based language models through an interactive **Streamlit dashboard**.

This project simplifies the process of benchmarking and selecting Large Language Models (LLMs) for **developers, researchers, and non-technical users**, using metric-driven analysis and intuitive visual feedback.

---

## 🎯 NLP Tasks Supported

### 1. **Summarization**
Measures how effectively the chatbot can generate concise summaries from longer conversations or textual content.

**Evaluation Metrics:**
- ROUGE-1
- ROUGE-2
- ROUGE-L

---

### 2. **Question Answering**
Evaluates the chatbot’s ability to generate accurate and relevant responses to user queries based on given context.

**Evaluation Metrics:**
- Accuracy
- Precision
- Recall
- F1-score (depending on dataset availability)

---

### 3. **Sentiment Analysis**
Determines the emotional tone of chatbot responses.

**Classes:**
- Positive
- Negative
- Neutral

**Evaluation Metrics:**
- Confusion Matrix
- Precision, Recall, F1-score

---

## 🧠 Models Used

The platform integrates **fine-tuned transformer-based models**, including:

- **RoBERTa-large** – High-performance classification and sentiment analysis
- **GPT-2** – Text generation and conversational response generation
- **LLaMA-2 (7B)** – Advanced language understanding and generation (if supported in environment)

Models are dynamically loaded based on task selection, enabling flexible experimentation and comparison.

---

## 🚀 Key Features

- Dynamic model selection based on selected NLP task  
- Multi-model evaluation and comparison  
- Real-time inference with instant visual feedback  
- Fine-tuned transformer models for improved accuracy  
- Interactive and user-friendly interface built using Streamlit  
- Graphical visualizations for easy interpretation  
- Modular and scalable architecture for future task integration  

---

## 🛠️ Technology Stack

- **Programming Language:** Python  
- **NLP Framework:** Hugging Face Transformers  
- **Evaluation Libraries:** Scikit-learn, Evaluate (ROUGE, etc.)  
- **Visualization:** Matplotlib, Seaborn  
- **Frontend:** Streamlit  
- **Data Handling:** Pandas  

---

## 📂 Project Structure

```plaintext
nlp_evaluator/
│
├── app.py
│   └── Main Streamlit application that connects the UI with backend logic
│
├── data/
│   └── sample_nlp_dataset.csv
│       └── Sample dataset used for testing and evaluation
│
├── evaluation/
│   └── metrics.py
│       └── Implements evaluation metrics such as accuracy, F1-score, ROUGE, etc.
│
├── models/
│   └── inference.py
│       └── Loads transformer models and runs inference on input text
│
├── utils/
│   └── plot_helpers.py
│       └── Utility functions for generating plots like confusion matrix and score charts
│
├── venv/
│   └── Virtual environment directory (auto-created for dependency management)
│
└── README.md
    └── Project documentation
⚙️ How the System Works

User selects an NLP task and model from the Streamlit UI.

Input text is passed to the inference module.

The selected transformer model generates predictions.

Task-specific evaluation metrics are computed.

Results are visualized using plots and tables.

Multiple models can be compared side-by-side.

📈 Evaluation & Visualization

Sentiment Analysis: Confusion matrix and classification report

Summarization: ROUGE score plots

Question Answering: Metric-based score summaries

Model Comparison: Bar charts and visual score comparisons

🔍 Challenges Addressed

Handling different input/output formats across transformer models

Selecting task-appropriate evaluation metrics

Managing model inference latency in real-time applications

Designing a scalable and modular evaluation pipeline

🎯 Purpose & Use Cases

Benchmark chatbot and LLM performance

Assist in model selection for NLP applications

Educational tool for understanding NLP evaluation metrics

Rapid experimentation platform for NLP research

🔮 Future Enhancements

Support for additional NLP tasks (NER, Translation, Topic Modeling)

Deployment on cloud platforms

Integration of human evaluation feedback

Support for larger LLMs via APIs

Exportable evaluation reports

👩‍💻 Author

Developed as part of an NLP and chatbot evaluation initiative using modern transformer-based architectures and best practices in model benchmarking.

📜 License

This project is for academic and research purposes
