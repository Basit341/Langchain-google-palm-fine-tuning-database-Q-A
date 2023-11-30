import streamlit as st
from cloths import get_fewshot_db_chain

st.title('Cloths Database Q & A using Google PALM 👕')

question=st.text_input('Question :')

if question:
    chain=get_fewshot_db_chain()
    response=chain.run(question)

    st.header("Answer :")
    st.write(response)