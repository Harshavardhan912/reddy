import streamlit as st
import joblib
model = joblib.load('spam_ham_dataset')
st.title('SPAM-HAM CLASSIFIER')
ip=st.text_input('enter your message')
op=model.predict([ip])
if st.button('Predict'):
 st.title(op[0])
    
