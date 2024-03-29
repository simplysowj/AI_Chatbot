import streamlit as st
from PIL import Image
from constant import *

def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        

local_css(r"C:\Users\simpl\Downloads\Portfolio-sowjanya\portfolio-template-LLM\style\style.css")


st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

img_4 = Image.open(r"C:\Users\simpl\Downloads\Portfolio-sowjanya\portfolio-template-LLM\images\4.png")
img_5 = Image.open(r"C:\Users\simpl\Downloads\Portfolio-sowjanya\portfolio-template-LLM\images\5.png")
img_6 = Image.open(r"C:\Users\simpl\Downloads\Portfolio-sowjanya\portfolio-template-LLM\images\6.png")
img_7 = Image.open(r"C:\Users\simpl\Downloads\Portfolio-sowjanya\portfolio-template-LLM\images\7.png")
img_8 = Image.open(r"C:\Users\simpl\Downloads\Portfolio-sowjanya\portfolio-template-LLM\images\8.png")
img_9 = Image.open(r"C:\Users\simpl\Downloads\Portfolio-sowjanya\portfolio-template-LLM\images\9.png")

st.title("🫶 Certifications")

col1, col2, col3,col4,col5,col6 = st.columns(6)

with col1:
   st.image(img_4)
   
with col2:
   st.image(img_5)

with col3:
   st.image(img_6)
with col4:
   st.image(img_7)
   
with col5:
   st.image(img_8)

with col6:
   st.image(img_9)
