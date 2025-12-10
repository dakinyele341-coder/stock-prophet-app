import streamlit as st

# Try to import the Hugging Face pipeline; if unavailable, we'll use a fallback
try:
    from transformers import pipeline
    HF_AVAILABLE = True
    hf_error = None
except Exception as e:
    HF_AVAILABLE = False
    hf_error = str(e)

# 1. Title of your Web App
st.title("🤖 My First AI Sentiment Analyzer")

# 2. Create a text box for the user
user_input = st.text_input("Type a sentence here (e.g., 'I love coding!'):")


def simple_fallback_sentiment(text: str):
    """Very small rule-based fallback sentiment classifier.

    This is intentionally simple: it counts positive/negative words and
    returns a label and a confidence-like score between 0 and 1.
    """
    POS = {
        "love", "like", "good", "great", "awesome", "excellent", "happy",
        "nice", "fantastic", "positive", "enjoy", "enjoyed"
    }
    NEG = {
        "hate", "dislike", "bad", "terrible", "awful", "sad", "angry",
        "horrible", "negative", "worse", "worst"
    }
    tokens = [w.strip(".,!?;:") .lower() for w in text.split()]
    pos_count = sum(1 for t in tokens if t in POS)
    neg_count = sum(1 for t in tokens if t in NEG)

    if pos_count + neg_count == 0:
        # no signal — neutral-ish
        return "NEUTRAL", 0.0

    if pos_count >= neg_count:
        score = pos_count / (pos_count + neg_count)
        return "POSITIVE", float(score)
    else:
        score = neg_count / (pos_count + neg_count)
        return "NEGATIVE", float(score)


# 3. If the user types something, run the AI (or fallback)
if user_input:
    label = None
    score = None

    if HF_AVAILABLE:
        try:
            classifier = pipeline("sentiment-analysis")
            result = classifier(user_input)
            label = result[0]["label"]
            score = float(result[0]["score"]) if "score" in result[0] else None
        except Exception as e:
            hf_error = str(e)
            HF_AVAILABLE = False

    if not HF_AVAILABLE:
        # Use the simple fallback classifier and show a notice to the user
        label, score = simple_fallback_sentiment(user_input)
        st.info("Hugging Face model not available — using local fallback classifier.")
        if hf_error:
            st.caption(f"(Model load error: {hf_error})")

    # Display the result on the screen
    st.write(f"### The AI thinks this is: **{label}**")
    if score is not None:
        st.write(f"Confidence Score: {score:.4f}")