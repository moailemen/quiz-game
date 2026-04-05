import streamlit as st

# Questions
questions = [
    {
        "question": "What is my nickname?",
        "options": ["Mo", "Pooja", "Lonely", "Jey"],
        "answer": "Lonely"
    },

    {
        "question": "What is my birth month?",
        "options": ["January", "February", "October", "July"],
        "answer": "January"
    },
    {
        "question": "Where do I presently reside?",
        "options": ["Canada", "England", "Iran", "Nigeria"],
        "answer": "England"
    },
    
    {
        "question": "Who is my Mentor?",
        "options": ["Dayo", "Ayor", "Senior", "Myself"],
        "answer": "Senior"
    },
    {
        "question": "Which Programming Language do use I prefer?",
        "options": ["Python", "JavaScript", "C++", "All of the above"],
        "answer": "Python"
    }
]

st.title("🧠 Quiz Game 🧠 How well do you know me?")

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
    st.write(f"🎉 Quiz Finished! ❤️ You know me well!❤️ Your score: {st.session_state.score}/{len(questions)}")

    if st.button("Restart"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.rerun()
