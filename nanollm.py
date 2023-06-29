import streamlit as st        # Streamlit as interface
import languagemodels as lm   # To access local language models, does all heavy lifting


lm.set_max_ram('4gb')                  # Set usable ram to 4GB
st.title("Nano LLM")                   # Sets the tittle of the app and spwans a streamlit UI
prompt = st.text_input('Prompt')       # Get prompt/question/instruction from user
if prompt:                             # If there is content in prompt do:
    with st.spinner("Thinking..."):    #   Display spinning animation while generating answer
        answer = lm.do(prompt)         #   Get anser from model
    st.write(answer)                   #   Write answer to app
