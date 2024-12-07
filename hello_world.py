import os

import streamlit as st
from pydantic_ai import Agent
import nest_asyncio

os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
os.environ["WEATHER_API_KEY"] = st.secrets["WEATHER_API_KEY"]
os.environ["GEO_API_KEY"] = st.secrets["GEO_API_KEY"]

# Show title and description.
st.title("💬 Chatbot")

# Apply nest_asyncio to allow nested event loops
nest_asyncio.apply()

# Create an agent.
@st.cache_resource
def init_agent():
    agent = Agent(  
        'gemini-1.5-flash',
        system_prompt='Be concise, reply with one sentence.',  
    )
    return agent

agent = init_agent()

# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input field to allow the user to enter a message. This will display
# automatically at the bottom of the page.
if prompt := st.chat_input("What is up?"):
    history = "\n".join([f"{message['role']}: message['content']" for message in st.session_state.messages])
    
    # Store and display the current prompt.
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate a response.
    result = agent.run_sync(f"""
    ## Chat history
    {history}

    ## Instruction
    {prompt}
    """)

    # Stream the response to the chat using `st.chat_message`, then store it in session state.
    with st.chat_message("assistant"):
        response = result.data  # ここでレスポンスデータを取得
        st.markdown(response)  # レスポンスを画面に表示
    st.session_state.messages.append({"role": "assistant", "content": response})  # 正しいデータを保存
