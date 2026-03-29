import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Naive Bayes Classifier", page_icon="📊")
st.title("Interactive Naive Bayes Text Classifier")
st.markdown(
    "Type a movie review below and see how a Naive Bayes model classifies it "
    "as **positive** or **negative** sentiment."
)


@st.cache_resource
def train_model():
    df = pd.read_csv("/app/code/data/movie-pang02.csv")
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"], df["class"], test_size=0.25, random_state=1, stratify=df["class"]
    )
    pipeline = Pipeline([
        ("vectorizer", TfidfVectorizer(stop_words="english", min_df=5)),
        ("classifier", MultinomialNB(alpha=1.0)),
    ])
    pipeline.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, pipeline.predict(X_test))
    return pipeline, accuracy


model, test_accuracy = train_model()

st.sidebar.header("Model Info")
st.sidebar.metric("Test Accuracy", f"{test_accuracy:.1%}")
st.sidebar.markdown(
    "**Pipeline:** TfidfVectorizer → MultinomialNB\n\n"
    "**Training data:** 1,500 movie reviews\n\n"
    "**Test data:** 500 movie reviews"
)

SAMPLES = {
    "Loved it": "This movie was absolutely fantastic, I loved every minute of it! The acting was superb and the story kept me on the edge of my seat.",
    "Hated it": "What a terrible waste of time. The plot made no sense, the dialogue was awful, and I wanted to walk out after the first twenty minutes.",
    "Mixed feelings": "The cinematography was beautiful and the lead actor gave a strong performance, but the script was weak and the ending felt rushed and unsatisfying.",
}

if "review_input" not in st.session_state:
    st.session_state.review_input = ""

st.markdown("**Try a sample review:**")
cols = st.columns(len(SAMPLES))
for col, (label, text) in zip(cols, SAMPLES.items()):
    if col.button(label, use_container_width=True):
        st.session_state.review_input = text
        st.rerun()

user_input = st.text_area(
    "Enter a movie review:",
    placeholder="e.g. This movie was absolutely fantastic, I loved every minute of it!",
    height=150,
    key="review_input",
)

classify = st.button("Classify", type="primary", use_container_width=True)

if classify and user_input.strip():
    prediction = model.predict([user_input])[0]
    probabilities = model.predict_proba([user_input])[0]
    classes = model.classes_

    neg_prob = probabilities[list(classes).index("Neg")]
    pos_prob = probabilities[list(classes).index("Pos")]

    if prediction == "Pos":
        st.success(f"**Positive** sentiment (confidence: {pos_prob:.1%})")
    else:
        st.error(f"**Negative** sentiment (confidence: {neg_prob:.1%})")

    col1, col2 = st.columns(2)
    col1.metric("Negative", f"{neg_prob:.1%}")
    col2.metric("Positive", f"{pos_prob:.1%}")
elif classify:
    st.warning("Please enter a review to classify.")
