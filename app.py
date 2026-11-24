import streamlit as st

st.title("🎲 Probability Learning App")

# Markdown section
st.markdown("""
## Probability Quiz

This app helps you test your knowledge of probability.

### Features
- Multiple-choice quiz
- User information form
- Difficulty selection
- Score evaluation
- Interactive widgets
""")

# Widget 1 : Text Input
name = st.text_input("Enter your name:")

# Widget 2 : Slider
age = st.slider("Select your age:", 15, 60, 20)

# Widget 3 : Selectbox
level = st.selectbox(
    "Choose difficulty level:",
    ["Beginner", "Intermediate", "Advanced"]
)

# Widget 4 : Checkbox
show_info = st.checkbox("Show probability tip")

if show_info:
    st.info("The probability of an event is a number between 0 and 1.")

# Widget 5 : Radio Buttons
q1 = st.radio(
    "1. What is the probability of getting Heads on a fair coin?",
    ["1/4", "1/2", "1"]
)

q2 = st.radio(
    "2. What is the probability of rolling a 6 on a fair die?",
    ["1/6", "1/3", "1/2"]
)

q3 = st.radio(
    "3. If P(A)=0.7, what is P(Aᶜ)?",
    ["0.3", "0.7", "1.7"]
)

q4 = st.radio(
    "4. The sum of all probabilities in a sample space is:",
    ["0", "1", "100"]
)

q5 = st.radio(
    "5. Two mutually exclusive events satisfy:",
    ["P(A∩B)=0", "P(A∩B)=1", "P(A)=P(B)"]
)

# Button
if st.button("Submit"):

    score = 0

    if q1 == "1/2":
        score += 1
    if q2 == "1/6":
        score += 1
    if q3 == "0.3":
        score += 1
    if q4 == "1":
        score += 1
    if q5 == "P(A∩B)=0":
        score += 1

    st.write(f"### {name}, your score is {score}/5")

    if score >= 4:
        st.success("Excellent! You have a strong understanding of probability.")
    elif score >= 2:
        st.warning("Average result. Keep practicing!")
    else:
        st.error("Insufficient result. Review the basics and try again.")

    st.info(f"Selected level: {level} | Age: {age}")
