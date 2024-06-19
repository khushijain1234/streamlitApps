import streamlit as st 
import os 
import google.generativeai as genai 
from dotenv import load_dotenv, dotenv_values


st.title("Chatster")
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = API_KEY
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

##Select the model
model = genai.GenerativeModel('gemini-pro')

## Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"assistant",
            "content":"Ask me Anythinggggg...."
        }
    ]

##Display chant messages on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

##Process and store query and response
def llm_function(query):
    response = model.generate_content(query)

    ##Displaying the assistant message
    with st.chat_message("assistant"):
        st.markdown(response.text)

    ##Storing the user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content":query
        }
    )

    ##Storing the assistant message
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content": response.text
        }
    )

 ##Accept user inpit
query = st.chat_input("What's Uppp????")

##Calling the function when input is provided
if query:
    #Displaying the user message
    with st.chat_message("user"):
        st.markdown(query)

    llm_function(query)
