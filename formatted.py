from langchain.agents import ConversationalChatAgent, AgentExecutor
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.tools import DuckDuckGoSearchRun
import streamlit as st

st.set_page_config(page_title="LangChain: Chat with search", page_icon="🦜")
st.title("🦜 LangChain: Chat with search")
st.write("Welcome to LangChain! You can chat with the AI by entering your questions below.")

# Sidebar for settings and information
st.sidebar.title("Settings")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
if st.sidebar.button("Reset chat history"):
    msgs.clear()
    msgs.add_ai_message("How can I help you?")
    st.session_state.steps = {}

# Chat history and memory initialization
msgs = StreamlitChatMessageHistory()
memory = ConversationBufferMemory(
    chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
)

# Avatars for human and AI
avatars = {"human": "👤", "ai": "🤖"}
for idx, msg in enumerate(msgs.messages):
    with st.chat_message(avatars[msg.type]):
        st.markdown(f"{avatars[msg.type]} {msg.content}")

# Chat input
prompt_placeholder = "Enter your question here (e.g., Who won the Women's U.S. Open in 2018?)"
if prompt := st.chat_input(placeholder=prompt_placeholder):
    st.chat_message("user").write(prompt)

    # Check for OpenAI API key
    if not openai_api_key:
        st.error("Please add your OpenAI API key in the sidebar to continue.")
        st.stop()

    # Chat agent and execution
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, streaming=True)
    tools = [DuckDuckGoSearchRun(name="Search")]
    chat_agent = ConversationalChatAgent.from_llm_and_tools(llm=llm, tools=tools)
    executor = AgentExecutor.from_agent_and_tools(
        agent=chat_agent,
        tools=tools,
        memory=memory,
        return_intermediate_steps=True,
        handle_parsing_errors=True,
    )
    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = executor(prompt, callbacks=[st_cb])
        formatted_response = f"**{response['output']}**"  # Example of bold formatting
        st.markdown(formatted_response)
