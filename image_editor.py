import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown("<h1 style='text-align:center'>Image Editor</h1>", unsafe_allow_html=True)
st.markdown("---")

image = st.file_uploader("Upload ypur image", type=["jpg", "png", "jpeg"])

info = st.empty()
mode = st.empty()
size = st.empty()
format_ = st.empty()

if image:   
    img = Image.open(image)
    st.markdown("<h2 style='text-align:center'>Informations</h2>", unsafe_allow_html=True)
    st.markdown(f"<h6 'style=text-align: center'>Mode: {img.mode}</h6>", unsafe_allow_html=True)
    st.markdown(f"<h6 'style=text-align: center'>Format: {img.format}</h6>", unsafe_allow_html=True)
    st.markdown(f"<h6 'style=text-align: center'>Size: {img.size}</h6>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align:center'>Resizing image</h2>", unsafe_allow_html=True)
    width = st.number_input("Width", value=img.width)
    height = st.number_input("Height", value=img.height)
    
    st.markdown("<h2 style='text-align:center'>Rotation</h2>", unsafe_allow_html=True)
    degree = st.number_input("Degree")
    
    st.markdown("<h2 style='text-align:center'>Filter</h2>", unsafe_allow_html=True)
    filter = st.selectbox("Filters", options=["None", "Blur", "Detail", "Emboss", "Smooth"])
    
    s_btn = st.button("Submit")
    
    if s_btn:
        edited = img.resize((width, height)).rotate(degree)
        if filter != "None":
            if filter == "Blur":
                filtered = edited.filter(BLUR)
            elif filter == "Detail":
                filtered = edited.filter(DETAIL)
            elif filter == "Emboss":
                filtered = edited.filter(EMBOSS),
            else: 
                filtered = edited.filter(SMOOTH)
            st.image(filtered)