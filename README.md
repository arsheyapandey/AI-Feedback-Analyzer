# 🎓 AI-Based Student Feedback Sentiment Analyzer

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

## Installation Instructions

1. **Clone or Download the repository.**
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## API Key Setup
1. Get a free API key from [Google AI Studio](https://aistudio.google.com/).
2. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
3. Edit `.env` and add your key:
   `GEMINI_API_KEY=your_actual_key_here`

## How to Run
```bash
streamlit run app.py
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

