import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Portfolio", layout="centered")

st.sidebar.header('Welcome')
page=st.sidebar.radio("To view",["introduction","skill","project 1"])

if page=='introduction':
   
    st.title("Hello, I'm Sabarinathan V!")
    st.write("Welcome to my portfolio. I am a graphic designer, passionate about creating visually compelling stories and engaging brand experiences..")

    st.header("About Me")
    st.write("""
 Iam a data analyst with a strong focus on statistical analysis and data visualization.
Here, you can explore some of the projects I have worked on, my skills, and my background.
""")

elif page=='skill':

    st.header("Skills")
    st.write("""
- *Programming Languages*: Python.
- *Frameworks*: Streamlit,HTML,CSS,etc.
- *Tools*: Git.
""")
elif page=='project 1':
    st.header("Projects")

    st.subheader("Project 1:Head or Tail game")
    st.write("Pictures of project done.")
    st.image("photo.png", width=300) 