
import streamlit as st
import httpx

# Page configuration
st.set_page_config(
    page_title="SmartSupport AI",
    page_icon="🤖",
    layout="centered"
)

# FastAPI address
API_URL = "http://127.0.0.1:8000/ask"

# Application heading
st.title("🤖 SmartSupport AI")
st.caption("Your AI-powered customer support assistant")

st.divider()

# Store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept customer question
if question := st.chat_input("Ask your question here..."):

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Get answer from FastAPI
    with st.chat_message("assistant"):
        with st.spinner("SmartSupport AI is thinking..."):
            try:
                response = httpx.post(
                    API_URL,
                    json={"question": question},
                    timeout=120.0
                )

                response.raise_for_status()
                answer = response.json()["answer"]

            except httpx.ConnectError:
                answer = "Cannot connect to the AI API. Please check whether the API server is running."

            except httpx.HTTPError:
                answer = "Sorry, something went wrong while contacting the AI service."

            st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
