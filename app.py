# app.py
import streamlit as st

st.title('streamlit test!')

tab1, tab2= st.tabs(['Tab A' , 'Tab B'])
    
with tab1:
  #tab A 를 누르면 표시될 내용
  st.write('merong')
    
with tab2:
  #tab B를 누르면 표시될 내용 
  st.write('hiiiii')
