import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder
import numpy as np


def main():
    st.title("Company Culture Preference Survey")

    # Questions and options
    questions = [
        "Do you prefer a structured or flexible work environment?",
        "Are you more comfortable with a formal or casual work atmosphere?",
        "How do you prefer to collaborate with colleagues?",
        "Are you more productive when working independently or as part of a team?",
        "Do you prefer a hands-on, directive management style, or do you prefer more autonomy and freedom?",
        "How do you respond to feedback and guidance from supervisors?",
        "How important is work-life balance to you, and what initiatives or policies do you appreciate in this regard?",
        "What values do you prioritize in a workplace?",
        "How important is it for you to work for a company that aligns with your personal values and beliefs?",
        "What are your expectations regarding career development opportunities within a company?",
        "How do you respond to constructive feedback, and what type of feedback culture do you thrive in?",
        "How do you prefer to celebrate successes and achievements in the workplace?"
    ]
    options = [
        ["Structured", "Flexible"],
        ["Formal", "Casual"],
        ["Face-to-face", "Virtually", "Combination"],
        ["Independently", "Part of a team"],
        ["Hands-on", "Autonomy"],
        ["Regular check-ins", "Independence"],
        ["Very important", "Moderately important", "Not important"],
        ["Diversity and inclusivity", "Innovation", "Sustainability"],
        ["Very important", "Moderately important", "Not important"],
        ["Strong opportunities for growth and advancement", "Structured training programs and mentorship opportunities"],
        ["Open to feedback and appreciate a culture of continuous improvement", "Prefer positive reinforcement and recognition for achievements"],
        ["Team celebrations and recognition", "Personal recognition and rewards", "Promotion"]
    ]

    # Initialize dictionary to store user responses
    user_responses = {}

    # Iterate over questions and options
    for i, question in enumerate(questions):
        st.subheader(f"Question {i + 1}: {question}")
        option = st.radio(f"Your answer for Question {i + 1}:", options[i], key=f"question_{i}")

        # Store user's choice
        user_responses[question] = option

    # Submit button
    if st.button("Submit Survey"):
        # Determine companies based on user responses
        recommended_companies = get_companies(user_responses)
        if recommended_companies:
            st.success(f"Recommended companies based on your preferences: {', '.join(recommended_companies)}")
        else:
            st.error("No matching companies found based on your preferences.")

def get_companies(responses):
    # Load historical data
    historical_data = pd.read_csv("historical_data.csv")

    # Concatenate historical data and user responses
    all_data = pd.concat([historical_data, pd.DataFrame(responses, index=[0])])

    # One-hot encode categorical variables
    encoder = OneHotEncoder(drop='first', sparse=False)
    all_data_encoded = encoder.fit_transform(all_data.drop(columns=["Company"]))

    # Prepare data for training
    X = all_data_encoded[:-1]  # Exclude the user response from training data
    y = all_data["Company"][:-1]  # Exclude the user response from target data

    # Train model
    model = RandomForestClassifier(random_state=42, class_weight='balanced')
    model.fit(X, y)

    # One-hot encode user responses
    user_responses_encoded = all_data_encoded[-1].reshape(1, -1)

    # Predict using user responses
    predicted_companies = model.predict(user_responses_encoded)

    return predicted_companies.tolist()

if __name__ == "__main__":
    main()
