import pickle
import string
import streamlit as st
import webbrowser
import os
global Lrdetect_Model



# Get the full path to 'model.pckl'
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model.pckl')

# Print debug information
print("Current working directory:", os.getcwd())
print(f"Does '{model_path}' exist? {os.path.exists(model_path)}")

# Open the 'model.pckl' file using the full path
try:
    LrdetectFile = open(model_path, 'rb')
    Lrdetect_Model = pickle.load(LrdetectFile)
    LrdetectFile.close()
except FileNotFoundError:
    st.error(f"Error: 'model.pckl' file not found at {model_path}. Make sure the file exists in the correct location.")
    st.stop()

st.title("Language Detection Tool")
input_test = st.text_input("Provide your text input here", 'Hello my name is Katie')

button_clicked = st.button("Get Language Name")
if button_clicked:
    st.text(Lrdetect_Model.predict([input_test]))


