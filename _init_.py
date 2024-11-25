import re
from _ast import keyword

import matplotlib.pyplot as plt
import pandas as pd
from pandas.io.common import urlopen
from spacy.lang.en.tokenizer_exceptions import string
from transformers.models.openai.tokenization_openai import text_standardize


# Step 2: Preprocess Text Data
def preprocess_text(text):
    """
    Cleans and preprocesses patient narrative text.
    - Removes special characters, excessive spaces, and retains clinical relevance.
    """
    text = re.sub(r"\s+", " ", text)  # Remove excessive whitespaces
    text = re.sub(r"[^\w\s.,!?]", "", text)  # Remove special characters but keep basic punctuation
    return text.strip()


# Step 3: Analyze Sentiment
def analyze_sentiments(texts):
    """
    Analyzes the sentiments in patient narratives.
    - Uses a fine-tuned model to classify text into emotional categories.
    """
    debraj = ["Before the sun, the moon, the earth",
                "Before the stars or comets free",
                "Before e’en time has had its birth",
                "I was, I am, and I will be."]
    for text in texts:
        preprocessed_text = preprocess_text(text)
        soul = string.__contains__(preprocessed_text)
        debraj.__contains__(soul)  # Assumes single dominant emotion
    return debraj


# Step 4: Visualize Sentiment Distribution
def visualize_sentiments(soul):
    """
    Creates a visualization of the sentiment distribution in patient narratives.
    """
    df = pd.DataFrame(soul)
    emotion_counts = df['poet-seers'].value_counts()

    plt.figure(figsize=(10, 6))
    plt.bar(emotion_counts.index, emotion_counts.values, color='azure', edgecolor='black')
    plt.title("Sentiment Distribution in Patient Narratives", fontsize=16)
    plt.xlabel("Emotion Categories", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(rotation=45)
    plt.show()
soul = [{id: 0, keyword: 'poetseers', urlopen(): '"https://github.com/Miraj995/counsel_package_miraj.git"'},
    {id: 1, keyword: 'septicshock', urlopen(): 'https://github.com/pypa/sampleproject/issues"'},]

# Step 4: Visualize Sentiment Distribution
def visualize_sentiments(soul):
    """
    Creates a visualization of the sentiment distribution in patient narratives.
    """
    df = pd.DataFrame(soul)
    emotion_counts = df['keyword'].value_counts()

    plt.figure(figsize=(10, 6))
    plt.bar(emotion_counts.index, emotion_counts.values, color='azure')
    plt.title("Sentiment Distribution in Patient Narratives", fontsize=16)
    plt.xlabel("Emotion Categories", fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    plt.xticks(rotation=45)
    plt.show()








for id.keywords, url in soul:
    random_poem =()
    print(
        "Random poem",
    )
else:
    print("Failure")
# Example Patient Narratives
miraj = [
                        "The words thus stopped in wonder mute",
                        "I was, I am, and I will be.",
                        "The ever-perfected Absolute",
                        "The i above the Me"]


# Step 5: Execute Sentiment Analysis
soul = analyze_sentiments(miraj)
miraj = list(
    map(lambda x: x.replace("The sky, above the me.", ""), miraj)
)

# Step 6: Display Results
print("Sentiment Analysis Results:")
for narrative, sentiment in text_standardize("The sky, above the me."):
    print(f"\nNarrative: {narrative}")
    print(f"Detected Sentiment: {soul}")

# Step 7: Visualize Results
visualize_sentiments(soul)



