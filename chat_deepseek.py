# https://github.com/laxmimerit/ollama-chatbot

import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)
st.markdown("""
<style>
    /* Main container background */
    .stApp {
        background: #f0f2f6;
    }
    
    /* Chat message styling */
    .message {
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 1.5rem;
        max-width: 80%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        line-height: 1.6;
        font-size: 16px;
    }
    
    .user-message {
        background: #4a90e2;
        color: white;
        margin-left: auto;
    }
    
    .assistant-message {
        background: #ffffff;
        margin-right: auto;
        border: 1px solid #e0e0e0;
    }
    
    /* Avatar styling */
    .avatar {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        margin-right: 1rem;
        object-fit: cover;
    }
    
    /* Input form styling */
    .stForm {
        background: white;
        padding: 1.5rem;
        border-radius: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* History container */
    .history-container {
        background: white;
        padding: 2rem;
        border-radius: 1.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Submit button styling */
    .stButton>button {
        background: #4a90e2 !important;
        color: white !important;
        border: none !important;
        padding: 12px 25px !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        background: #357abd !important;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)
st.title("🧠 DeepSeek AI Assistant")
st.markdown("---")
st.markdown("🌟 *Powered by Ollama & LangChain | 1.5B Parameter LLM*")
with st.sidebar:
    st.header("⚙️ Configuration")
    st.image("https://avatars.githubusercontent.com/u/102314025?s=200&v=4", width=120)
    st.markdown("""
    **Model Details**  
    🔹 Name: DeepSeek-R1 1.5B  
    🔹 Context Window: 4k tokens  
    🔹 Training Data: Diverse multilingual corpus  
    🔹 Capabilities:  
    - Natural Language Understanding  
    - Code Generation  
    - Contextual Conversations  
    - Creative Writing  
    """)
    st.markdown("---")
    if st.button("🧹 Clear Chat History"):
        st.session_state['chat_history'] = []
        st.experimental_rerun()
model_name = "deepseek-r1:1.5b"
model = ChatOllama(model=model_name, base_url="http://localhost:11434")
if "chat_history" not in st.session_state:
    st.session_state['chat_history'] = []
system_message = SystemMessagePromptTemplate.from_template(
    "You are an expert AI assistant specialized in software development and technical writing. "
    "Provide concise, accurate answers with code examples when relevant. "
    "Format code blocks properly and explain complex concepts clearly."
)
def generate_response(chat_history):
    chat_template = ChatPromptTemplate.from_messages(chat_history)
    chain = chat_template | model | StrOutputParser()
    return chain.invoke({})
def get_history():
    chat_history = [system_message]
    for chat in st.session_state['chat_history']:
        chat_history.append(HumanMessagePromptTemplate.from_template(chat['user']))
        chat_history.append(AIMessagePromptTemplate.from_template(chat['assistant']))
    return chat_history

with st.container():
    st.markdown('<div class="history-container">', unsafe_allow_html=True)
    for chat in st.session_state['chat_history']:
        cols = st.columns([1, 10])
        with cols[1]:
            st.markdown(f"""
            <div class="message user-message">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <img src="https://cdn-icons-png.flaticon.com/512/1077/1077114.png" class="avatar">
                    <strong style="font-size: 18px;">You</strong>
                </div>
                {chat['user']}
            </div>
            """, unsafe_allow_html=True)
        cols = st.columns([10, 1])
        with cols[0]:
            st.markdown(f"""
            <div class="message assistant-message">
                <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712095.png" class="avatar">
                    <strong style="font-size: 18px;">DeepSeek</strong>
                </div>
                {chat['assistant']}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
with st.form("chat_form"):
    cols = st.columns([8, 1])
    user_input = cols[0].text_input(
        "Ask me anything...",
        placeholder="Type your message here...",
        label_visibility="collapsed"
    )
    submitted = cols[1].form_submit_button("🚀 Send")
    
    if submitted and user_input:
        with st.spinner("🔮 Generating response..."):
            prompt = HumanMessagePromptTemplate.from_template(user_input)
            chat_history = get_history()
            chat_history.append(prompt)
            response = generate_response(chat_history)
            st.session_state['chat_history'].append({
                'user': user_input,
                'assistant': response
            })
            st.experimental_rerun()
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; margin-top: 2rem;">
    <p>🔐 Your conversations are private and never stored</p>
    <p>🤖 Powered by DeepSeek-R1 1.5B LLM</p>
    <p>💻 Running locally via Ollama</p>
</div>
""", unsafe_allow_html=True)