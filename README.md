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

The **AI-Based Student Feedback Sentiment Analyzer** is an NLP and Generative AI-based web application developed to automatically analyze and understand student feedback. The system processes textual feedback provided by students and identifies the overall sentiment, important topics, keywords, positive aspects, negative aspects, and areas that require improvement.

The project combines **traditional Natural Language Processing techniques with Large Language Model (LLM) capabilities** to provide more meaningful and contextual insights from student feedback. Instead of simply classifying feedback as positive or negative, the application attempts to understand what students liked, what problems they faced, and what improvements can be made.

The application provides an interactive **Streamlit-based web interface** through which users can enter individual feedback or upload a CSV file containing multiple student responses.

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

