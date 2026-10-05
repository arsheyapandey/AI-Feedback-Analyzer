import streamlit as st
import pandas as pd
import plotly.express as px
from dotenv import load_dotenv
import os

from src.utils import load_config
from src.analyzer import FeedbackAnalyzer

# Load environment variables
load_dotenv()

# Streamlit Page Config
st.set_page_config(page_title="AI Feedback Analyzer", page_icon="🎓", layout="wide")

def get_analyzer():
    config = load_config()
    return FeedbackAnalyzer(config)

analyzer = get_analyzer()

# Sidebar
st.sidebar.title("🎓 AI Analyzer Settings")
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key or api_key == "your_gemini_api_key_here":
    st.sidebar.warning("GEMINI_API_KEY is not set. LLM features will be disabled.")
else:
    st.sidebar.success("GEMINI_API_KEY is configured.")

st.title("🎓 AI-Based Student Feedback Sentiment Analyzer")

tab1, tab2, tab3 = st.tabs(["Single Feedback", "Batch Analysis", "Insights Dashboard"])

with tab1:
    st.header("Analyze Single Feedback")
    user_input = st.text_area("Enter student feedback:")
    if st.button("Analyze Feedback"):
        if user_input:
            with st.spinner("Analyzing with NLP & LLM..."):
                res = analyzer.analyze_single(user_input)
                
                if "error" in res:
                    st.error(res["error"])
                else:
                    llm_res = res.get("llm_analysis", {})
                    st.subheader("📊 Feedback Analysis")
                    
                    sentiment = str(llm_res.get("sentiment", "Unknown")).upper()
                    st.markdown(f"**Overall Sentiment:** `{sentiment}`")
                    
                    st.markdown("**Positive Aspects:**")
                    pos_aspects = llm_res.get("positive_aspects", [])
                    if pos_aspects:
                        for asp in pos_aspects:
                            st.markdown(f"• {asp}")
                    else:
                        st.markdown("• None")
                        
                    st.markdown("**Negative Aspects:**")
                    neg_aspects = llm_res.get("negative_aspects", [])
                    if neg_aspects:
                        for asp in neg_aspects:
                            st.markdown(f"• {asp}")
                    else:
                        st.markdown("• None")

                    st.markdown("**Topics:**")
                    topics = llm_res.get("main_topics", [])
                    if topics:
                        for top in topics:
                            st.markdown(f"• {top}")
                    else:
                        st.markdown("• None")

                    st.markdown("**Keywords:**")
                    keywords = llm_res.get("important_keywords", [])
                    st.markdown(", ".join(keywords) if keywords else "None")

                    st.markdown("**🤖 AI Summary:**")
                    st.info(llm_res.get("short_summary", ""))

                    st.markdown("**💡 Suggested Improvements:**")
                    suggestions = llm_res.get("suggested_improvements", [])
                    for idx, sug in enumerate(suggestions, 1):
                        st.markdown(f"{idx}. {sug}")

                    aspects = res.get("aspects", [])
                    if isinstance(aspects, list) and len(aspects) > 0:
                        st.markdown("---")
                        st.markdown("**🔍 Aspect-Based Breakdown:**")
                        for aspect in aspects:
                            st.markdown(f"• **{aspect.get('aspect')}** → `{aspect.get('sentiment')}` (*{aspect.get('reason')}*)")
        else:
            st.warning("Please enter feedback.")

with tab2:
    st.header("Batch Analysis")
    
    sample_csv_path = os.path.join("data", "sample_feedback.csv")
    if os.path.exists(sample_csv_path):
        with open(sample_csv_path, "rb") as file:
            st.download_button(
                label="📥 Download Sample CSV File",
                data=file,
                file_name="sample_feedback.csv",
                mime="text/csv"
            )
            
    uploaded_file = st.file_uploader("Upload CSV containing a 'feedback' column", type=["csv"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if 'feedback' not in df.columns:
                st.error("CSV must contain a 'feedback' column.")
            else:
                st.write(f"Found {len(df)} feedback entries.")
                if st.button("Analyze Batch"):
                    with st.spinner("Processing batch with NLP & LLM..."):
                        feedbacks = df['feedback'].dropna().tolist()
                        batch_res = analyzer.analyze_batch(feedbacks)
                        
                        if "error" in batch_res:
                            st.error(batch_res["error"])
                        else:
                            st.session_state["batch_res"] = batch_res
                            st.success("Analysis Complete! Go to Insights Dashboard tab.")
        except Exception as e:
            st.error(f"Error reading CSV: {e}")

with tab3:
    st.header("Insights Dashboard")
    if "batch_res" in st.session_state:
        res = st.session_state["batch_res"]
        results_df = pd.DataFrame(res["individual_results"])
        
        col1, col2, col3 = st.columns(3)
        total = len(results_df)
        pos = len(results_df[results_df['sentiment'] == 'Positive'])
        neg = len(results_df[results_df['sentiment'] == 'Negative'])
        neu = len(results_df[results_df['sentiment'] == 'Neutral'])
        
        col1.metric("Total Feedback", total)
        col2.metric("Positive", f"{(pos/total)*100:.1f}%")
        col3.metric("Negative", f"{(neg/total)*100:.1f}%")
        
        # Chart
        st.subheader("Sentiment Distribution")
        fig = px.pie(results_df, names='sentiment', title='Feedback Sentiment Distribution', color='sentiment',
                     color_discrete_map={'Positive':'green', 'Neutral':'gray', 'Negative':'red'})
        st.plotly_chart(fig, use_container_width=True)
        
        col_topics, col_llm = st.columns(2)
        with col_topics:
            st.subheader("Most Discussed Topics (TF-IDF)")
            st.write(", ".join(res.get("top_keywords", [])))
            
        with col_llm:
            st.subheader("AI-Generated Overall Summary")
            st.info(res.get("summary", "N/A"))
            
        st.subheader("AI-Generated Recommendations")
        for idx, rec in enumerate(res.get("recommendations", [])):
            st.write(f"{idx+1}. {rec}")
            
    else:
        st.info("Please run Batch Analysis first.")
