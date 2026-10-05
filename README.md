# 🎓 AI-Based Student Feedback Sentiment Analyzer


## Student & Training Program Details

| **Field** | **Details** |
|---|---|
| **Student Name** | Arsheya Pandey |
| **Registration Number** | 23FE10CDS00358 |
| **Branch** | B.Tech CSE (Data Science) |
| **Batch** | E |
| **Project Title** | AI-Based Student Feedback Sentiment Analyzer |
| **GitHub Username** | arsheyapandey |
| **Training Program** | NLP & Generative AI Training Program |
| **Project Type** | Individual Project |
| **Domain** | Natural Language Processing (NLP) & Generative AI |
| **Technology** | Python |
| **Application Framework** | Streamlit |
| **LLM Used** | Google Gemini API |

---

## 1. Project Overview

AI-Based Student Feedback Sentiment Analyzer is an NLP-based web application designed to automatically analyze and understand student feedback using Natural Language Processing techniques and a Large Language Model (LLM). The main objective of this project is to convert unstructured student feedback into meaningful and actionable insights for teachers, colleges, and educational institutions. Users can either enter individual feedback manually or upload a CSV file containing multiple student responses. The system first preprocesses the feedback using NLP techniques such as text cleaning, lowercasing, tokenization, stop-word removal, and lemmatization. After preprocessing, the application performs sentiment analysis to classify feedback as positive, negative, neutral, or mixed. It also extracts important keywords, identifies major topics, and detects positive and negative aspects mentioned by students. For example, if a student writes, “The professor explains concepts very clearly, but the assignments are too difficult and there is not enough time to complete them,” the system can identify teaching quality as a positive aspect and assignment difficulty and workload as negative aspects. The project integrates the Google Gemini LLM API to provide more contextual and meaningful analysis. Instead of using the LLM as a simple chatbot, it is used for tasks such as contextual aspect analysis, generating concise summaries, identifying major concerns, and providing actionable recommendations. For multiple feedback responses, the LLM can generate an overall summary describing the common opinions and concerns of students. The system can also suggest improvements, such as reducing assignment difficulty, providing additional time, or increasing practical sessions. For batch analysis, users can upload a CSV file containing a feedback column, after which the application analyzes all responses and presents useful statistics through an interactive dashboard. The dashboard can display the total number of responses, positive/negative/neutral percentages, sentiment distribution, frequently discussed topics, common positive aspects, common negative aspects, an AI-generated summary, and recommended improvements. The application is developed using Python and Streamlit, providing a simple and user-friendly web interface. Pandas is used for data processing, while NLTK, spaCy, and Scikit-learn can be used for NLP preprocessing and traditional machine learning tasks. The Google Gemini API provides the LLM functionality, and Python-dotenv is used to securely manage the API key through environment variables. The project also maintains separate prompt and configuration files to improve modularity, maintainability, and prompt efficiency. Overall, this project demonstrates how traditional NLP methods and modern Generative AI can be combined to analyze large amounts of student feedback efficiently. It provides educational institutions with a faster way to understand student opinions, identify recurring problems, recognize positive teaching practices, and make data-driven improvements to courses and learning environments.

---

## 2. Objectives

The main objectives of this project are:

- To automatically analyze student feedback using NLP techniques.
- To classify feedback into **Positive, Negative, Neutral, or Mixed** sentiment.
- To identify important topics and keywords present in feedback.
- To extract positive and negative aspects mentioned by students.
- To use an LLM for contextual understanding of feedback.
- To generate concise summaries of multiple student responses.
- To provide AI-generated recommendations for improving courses and teaching.
- To support analysis of both individual feedback and large CSV datasets.
- To present the results through an easy-to-use web interface.

---

## 3. Key Features

### Individual Feedback Analysis

Users can enter a single student feedback statement and receive:

- Overall sentiment
- Sentiment explanation
- Important keywords
- Topics identified
- Positive aspects
- Negative aspects
- AI-generated summary
- Improvement suggestions

### Batch CSV Analysis

The application also supports uploading a CSV file containing multiple student feedback responses.

The system can generate:

- Total number of feedback responses
- Sentiment distribution
- Positive/negative/neutral/mixed counts
- Common topics
- Frequently occurring keywords
- Positive aspects
- Negative aspects
- Overall feedback summary
- AI-generated recommendations

### LLM-Based Analysis

The project integrates the **Google Gemini API** to perform contextual analysis of student feedback. The LLM helps understand feedback that may contain multiple opinions, indirect criticism, or mixed sentiments.

For example:

> "The professor teaches very well, but the assignments are difficult and the lab sessions are too short."

The system can identify this as **Mixed Sentiment**, with:

- Positive aspect: Teaching quality
- Negative aspects: Assignment difficulty and short lab sessions
- Topics: Teaching, Assignments, Laboratory

---

## 4. NLP Pipeline

The project follows a structured NLP pipeline:

```text
Student Feedback
       ↓
Text Cleaning
       ↓
Lowercasing
       ↓
Tokenization
       ↓
Stop-word Removal
       ↓
Lemmatization
       ↓
Feature Extraction
       ↓
Sentiment Analysis
       ↓
Topic & Keyword Extraction
       ↓
LLM-Based Contextual Analysis
       ↓
Summary & Recommendations
       ↓
Final Results
## Problem Statement
Educational institutions collect vast amounts of student feedback, but manually analyzing it is time-consuming and subjective. Basic sentiment analysis often fails to capture context or identify sentiment for specific aspects (e.g., teaching vs. assignments). 

## Objectives
Create a hybrid NLP application that combines traditional lightweight NLP techniques with Large Language Models (LLM) to perform deep analysis, aspect-based sentiment extraction, and automated summarization of student feedback.

## Features
1. **Single Feedback Analysis**: Deep dive into individual feedback using LLM to extract topics, sentiment, and aspect-based sentiments.
2. **Batch Processing**: Upload a CSV to process hundreds of feedback items.
3. **Hybrid Architecture**: Uses fast TF-IDF and VADER for batch keyword/sentiment extraction, and LLM API for high-level summarization and recommendations.
4. **Insights Dashboard**: Visualizes sentiment distribution and displays actionable AI-generated recommendations.

## NLP Techniques Used
- **Text Preprocessing**: Tokenization, Stop-word removal, Lemmatization using `NLTK`.
- **Topic Extraction**: TF-IDF using `scikit-learn`.
- **Traditional Sentiment**: VADER Lexicon based rule-based sentiment.
- **LLM Integration**: Google Gemini API for deep semantic understanding, aspect-based sentiment analysis (ABSA), and summarization.

## Architecture/Workflow
1. **Input**: User inputs text or uploads CSV.
2. **Preprocessing**: Text is cleaned, tokenized, and lemmatized.
3. **Pipeline**: 
   - Traditional NLP handles basic classification and keyword extraction efficiently.
   - LLM API handles complex tasks like aspect-based sentiment, overall summarization, and generating actionable suggestions based on structured prompts.

## Project Structure
```
Student-Feedback-Sentiment-Analyzer/
├── app.py                     # Streamlit frontend
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .env.example               # Environment variables template
├── config/
│   └── config.yaml            # Application configuration
├── prompts/
│   ├── sentiment_prompt.txt   # Prompt for general analysis
│   ├── aspect_prompt.txt      # Prompt for ABSA
│   ├── summary_prompt.txt     # Prompt for batch summary
│   └── recommendation_prompt.txt # Prompt for action points
├── src/
│   ├── preprocessing.py       # NLTK preprocessing
│   ├── sentiment.py           # Traditional VADER sentiment
│   ├── topic_extraction.py    # Scikit-learn TF-IDF
│   ├── llm.py                 # Gemini API integration
│   ├── analyzer.py            # Main controller
│   └── utils.py               # Helpers
├── data/
│   └── sample_feedback.csv    # Sample data
└── tests/
    └── test_analyzer.py       # Unit tests
```

## Example Output
**Input**: "The professor teaches very well, but the assignments are difficult and the lab sessions are too short."
**Output**:
- Teaching → Positive
- Assignments → Negative
- Lab Sessions → Negative

## Limitations & Future Improvements
- **Limitations**: Depends on Gemini API rate limits. LLM might rarely hallucinate if prompts are not strictly followed.
- **Future Improvements**: Add fine-tuned small local models (like BERT) for ABSA to remove dependency on external APIs.

