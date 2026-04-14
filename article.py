import streamlit as st 
import back_gen 

st.header("Article Generator")
topic = st.text_input("Enter the topic for the article:") # user input store here
st.write("The workflow is as follows:") 

# Display the button to trigger the article generation
if st.button("Generate"):
    st.write("Generating article...")
    # Here you would call your workflow to generate the article
    initial_state = {'Topic': topic} 
     
    # generate the article using the workflow
    result = back_gen.workflow.invoke(initial_state)
    st.subheader("Generated Article")
    st.write(result['article']) 