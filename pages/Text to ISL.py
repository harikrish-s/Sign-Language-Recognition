import streamlit as st
from PIL import Image

st.header("Text to ISL Conversion")
data = st.text_input("Enter the text you want to convert :")
images = []
for i in data:
    if (i.isnumeric() == True):
        image = Image.open(
        r"Dataset_to_print/"+i+"/"+"1.jpg")
        # st.image(image, caption=i)
        images.append(image)
    elif (i.isalpha() == True):
        if (i.islower() == True):
            j = i.upper()
            del i
            i = j
            image = Image.open(
            r"Dataset_to_print/"+i+"/"+"1.jpg")
            # st.image(image, caption=i)
            images.append(image)
    elif(i.isspace() == True):
        image = Image.open(
        r"Dataset_to_print/"+"space.jpg")
        # st.image(image, caption=i)
        images.append(image)

st.image(images)
