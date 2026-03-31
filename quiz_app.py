import streamlit as st

# Questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["5", "8", "10", "6"],
        "answer": "8"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "JavaScript", "C++", "All of the above"],
        "answer": "All of the above"
    }
]

st.title("🧠 Quiz Game")

# Session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

# Current question
if st.session_state.q_index < len(questions):
    q = questions[st.session_state.q_index]

    st.subheader(q["question"])

    choice = st.radio("Choose your answer:", q["options"])

    if st.button("Submit"):
        if choice == q["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Wrong! Correct answer is {q['answer']}")

        st.session_state.q_index += 1
        st.rerun()

else:
    st.write(f"🎉 Quiz Finished! Your score: {st.session_state.score}/{len(questions)}")

    if st.button("Restart"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.rerun()
