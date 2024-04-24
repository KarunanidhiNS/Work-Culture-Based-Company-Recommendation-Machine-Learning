import pandas as pd
import random

# Define the questions and options
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

companies = ["ZOHO", "TCS","LTIMindtree","Mphasis","Cognizant","Honeywell", "Microsoft","Tech Mahindra","HCL Technologies","Wipro"]

# Generate the dataset
data = []
for _ in range(9999):
    responses = []
    for i, question in enumerate(questions):
        response = random.choice(options[i])
        responses.append(response)
    company = random.choice(companies)
    data.append(responses + [company])

# Create a DataFrame
df = pd.DataFrame(data, columns=questions + ["Company"])

# Save the DataFrame to a CSV file
df.to_csv("historical_data.csv", index=False)
