import os
import streamlit as st

from get_response import get_response

# Streamlit app
# Title
st.set_page_config(page_title="Local Llama")

# Header
st.title("Local Llama")

# Initializing chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat messages from history on app rerun
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

text = st.chat_input(placeholder="AMA!")

# React to user input
if text:
        # Content to be given to Model
        input = text
        # Display user message in chat message container
        st.chat_message("user").markdown(text)

        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": text})

        # Get response
        response = st.chat_message("assistant").write_stream(get_response(input=st.session_state.messages))

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})