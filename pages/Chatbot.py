import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

def local_css(file_name):
    with open(file_name) as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style.css")

# -------------------------------
# Load environment variables
# -------------------------------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
print("DEBUG API Key:", api_key)



# -------------------------------
# Streamlit UI setup
# -------------------------------
st.markdown("<h1 class='title'>🦠 Ask Anything about COVID!</h1>", unsafe_allow_html=True)

# -------------------------------
# Initialize LLM using OpenRouter
# -------------------------------
llm = ChatOpenAI(
    openai_api_key=api_key,
    openai_api_base="https://openrouter.ai/api/v1",
    model="gpt-4.1-mini",  # You can switch to another model like 'gpt-4.1' or 'gpt-3.5-turbo'
    temperature=0.7,
    max_tokens=400
)

# -------------------------------
# System prompt
# -------------------------------
system_prompt = """
You are a knowledgeable and friendly virtual assistant that provides accurate and up-to-date information about COVID-19. 

Your role is to assist users with:
- General information about COVID-19 and its symptoms
- Guidance on prevention and safety measures
- Updates on testing, vaccination, and booster shots
- Travel and quarantine guidelines
- Steps to take if someone is exposed or tests positive

Be professional, empathetic, and clear in your responses.  
Always prioritize public health and safety.  
If you are unsure about something or if the question is highly specific, politely suggest that the user consult an official health authority or medical professional, such as the **World Health Organization (WHO)** or local public health department.

"""

# -------------------------------
# Conversation Memory
# -------------------------------
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# -------------------------------
# Prompt Template
# -------------------------------
support_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{user_input}")
])

# -------------------------------
# Build the LLM Chain
# -------------------------------
chain = LLMChain(
    llm=llm,
    prompt=support_prompt,
    memory=memory,
    verbose=True  # For debugging in Streamlit terminal
)

# -------------------------------
# Session State for Chat History
# -------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -------------------------------
# User Input
# -------------------------------
user_input = st.text_input("", placeholder="Ask me about covid pandamic...")

if st.button("Send") and user_input:
    try:
        # Add user's message
        st.session_state.chat_history.append(("You", user_input))

        # Create a placeholder
        chat_box = st.empty()

        # Temporary message (Thinking...)
        temp_history = st.session_state.chat_history + [("Assistant", "Thinking...")]
        chat_html = "<div class='chat-box'>"
        for speaker, message in temp_history:
            if speaker == "You":
                chat_html += f"<span class='user-text'>🧑 You: {message}</span>\n\n"
            else:
                chat_html += f"<span class='assistant-text'>🤖 Assistant: {message}</span>\n\n"
        chat_html += "</div>"
        chat_box.markdown(chat_html, unsafe_allow_html=True)

        # Get actual response
        response = chain.run(user_input=user_input)
        st.session_state.chat_history.append(("Assistant", response))

        # Final render
        chat_html = "<div class='chat-box'>"
        for speaker, message in st.session_state.chat_history:
            if speaker == "You":
                chat_html += f"<span class='user-text'> You: {message}</span>\n"
            else:
                chat_html += f"<span class='assistant-text'> Assistant: {message}</span>\n"
        chat_html += "</div>"
        chat_box.markdown(chat_html, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error: {str(e)}")



