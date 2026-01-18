import pprint
import streamlit as st
from . utils.crewUtils import executeApp

st.title("Emerging Technology Research")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# function to trim dictionary values to the maximum length
def trim_dict_values(data_dict, max_length):
    trimmed_dict = {}
    for key, value in data_dict.items():
        if isinstance(value, str):
            if len(value) > max_length:
                trimmed_dict[key] = value[:max_length]+"..."
            else:
                trimmed_dict[key] = value
        elif isinstance(value, (int, float, complex)):
            trimmed_dict[key] = value
    return trimmed_dict

# function to listen to the agent and task updates in a crew
def step_callback(step):
    # format to be a bit presentable.
    action:str = pprint.pformat(trim_dict_values(step.__dict__,75), width=80, compact=True, depth=1, indent=2)
    if action:
        with st.chat_message("ai", avatar="🤖"):
            st.markdown("#### DEBUG OUT: "+step.__class__.__name__)
            st.write(action)

sessionId = "g1a8c97b-fb67-465a-a229-fc81245fc154"
actorId = "g6502a7c-244d-4111-8713-2f73ffda2553"

# React to user input
if prompt := st.chat_input("Ask me about emerging technologies"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    inputs = {
        'prompt': prompt,
        'sessionId': sessionId,
        'actorId': actorId
    }

    response = executeApp(inputs)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown("#### FINAL OUTPUT:")
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

    