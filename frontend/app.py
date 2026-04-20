import streamlit as st
import requests

st.set_page_config(page_title="AI Tutor", layout="wide")

st.title("🎓 AI Learning Assistant")

if "history" not in st.session_state:
    st.session_state.history = []

query = st.text_input("Ask a question")

if st.button("Ask"):
    try:
        res = requests.post(
            "http://localhost:8000/chat/",
            params={"query": query}
        )

        data = res.json()
        answer = data.get("response", "No response from server")

    except Exception as e:
        answer = f"Error: {str(e)}"

    st.session_state.history.append((query, answer))


st.divider()

for q, a in reversed(st.session_state.history):
    st.markdown(f"**🧑 You:** {q}")
    st.markdown(f"**🤖 AI:** {a}")