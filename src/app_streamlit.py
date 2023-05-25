import streamlit as st
from streamlit_chat import message
import chat_gpt

# Sets up the OpenAI API configuration using the Streamlit secrets manager.
chat_gpt.setup_openai_api(st.secrets)

# Streamlit to set the page header and icon.
st.set_page_config(
    page_title="ChatGPT",
    page_icon="https://avatars.githubusercontent.com/u/59286869",
    layout="wide",
)

# Initializes the Streamlit session state with default values for the 'prompts'.
if "context" not in st.session_state:
    st.session_state[
        "context"
    ] = "You are an AI assistant that helps people find information and create written content. \
If you don't know something, you reply that you don't know."

if "prompts" not in st.session_state:
    st.session_state["prompts"] = chat_gpt.reset_prompts(st.session_state["context"])


def chat_click():
    if st.session_state["user"] != "":
        user_chat_input = st.session_state["user"]
        st.session_state["prompts"] = chat_gpt.update_prompts(
            st.session_state["prompts"], "user", user_chat_input
        )
        output = chat_gpt.generate_response(
            st.session_state["prompts"],
            st.secrets["MODEL_NAME"],
            st.session_state["temperature"],
            st.session_state["max_tokens"],
            st.session_state["top_p"],
        )
        # if chat_gpt.ERROR_PERFIX in output, we keep the prompts as is and display the error message
        if chat_gpt.ERROR_PERFIX in output:
            # Remove the last prompt, which is the user's input
            st.session_state["prompts"].pop()
            # icon avatar style and the bandaid icon
            message(output.replace(chat_gpt.ERROR_PERFIX, ""), avatar_style="bottts", seed=1)
        else:
            st.session_state["prompts"] = chat_gpt.update_prompts(
                st.session_state["prompts"], "assistant", output
            )
            st.session_state["user"] = ""


def new_topic_click():
    st.session_state["prompts"] = chat_gpt.reset_prompts(st.session_state["context"])
    st.session_state["user"] = ""


chatTab, settingsTab = st.tabs(["💬 Chat", "⚒️ Settings"])

with settingsTab:
    system_message = st.text_area("Bot context:", key="context", height=100)
    max_tokens = st.slider("Max tokens", 0, 32000, 8000, key="max_tokens")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, key="temperature")
    top_p = st.slider("Top p", 0.0, 1.0, 0.95, key="top_p")
    reset_bot_btn = st.button("Reset bot", on_click=new_topic_click)

with chatTab:
    user_input = st.text_area("You:", key="user")

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        chat_button = st.button("Send", on_click=chat_click, use_container_width=True)
    with col4:
        new_topic_button = st.button(
            "New Topic", on_click=new_topic_click, use_container_width=True
        )

    if len(st.session_state["prompts"]) > 1:
        for i in range(len(st.session_state["prompts"]) - 1, 0, -1):
            role = st.session_state["prompts"][i]["role"]
            content = st.session_state["prompts"][i]["content"]
            if role == "assistant":
                message(content, avatar_style="pixel-art-neutral")
            elif role == "user":
                message(content, is_user=True, avatar_style="pixel-art")
