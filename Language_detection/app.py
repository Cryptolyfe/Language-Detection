import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('/Users/katie.kirby/projects/language_detection/Language_detection/model.pckl', 'rb')


#LrdetectFile = open('model.pckl','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title("Language Detection Tool")
input_test = st.text_input("provide your text input here", 'Hello my name is Katie ')

button_clicked = st.button("Get Language Name")
if button_clicked:
	st.text(Lrdetect_Model.predict([input_test]))
