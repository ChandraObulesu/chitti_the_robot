# give me a simple streamlit app that can showcase the use of streamlit and the different components of streamlit
import streamlit as st

#print hello world in streamlit
st.write("hello world")

# give me a button that says click me and when clicked it will print hello world in streamlit
button = st.button("click me")
if button:
    st.write("hello world iam robo speed one tera heads chai kya banega ")

# give me a text input that says enter your name and when entered it will print hello name in streamlit
name = st.text_input("enter your name")
if name:
    st.write(f"hello {name}")

# give me a selectbox that says select your gender and when selected it will print the gender in streamlit
gender = st.selectbox("select your gender", ["male", "female", "other"])
if gender:
    st.write(f"hello {gender}")

# give me a date input that says enter your date of birth and when entered it will print the date of birth in streamlit
area = st.text_area("enter your area")
if area:
    st.write(f"hello {area}")

# give me a file uploader that says upload your file and when uploaded it will print the file in streamlit
file = st.file_uploader("upload your file")
if file:
    st.write(f"hello {file}")

# give me a color picker that says select your color and when selected it will print the color in streamlit
color = st.color_picker("select your color")
if color:
    st.write(f"hello {color}")      
