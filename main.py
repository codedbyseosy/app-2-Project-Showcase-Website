import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1, col2 = st.columns(2) #st is the module, columns is the method
                           #this method will return two column objects & store them in the two variables

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Eseose Odion")
    content = """Hello, I'm Eseose Odion, a 22-year-old with a passion for technology and creativity. 
    I hold a Master's degree in Computer Systems Engineering from The University of Sheffield. 
    My journey in the tech world has been nothing short of diverse and exciting, as I proudly wear multiple hats – 
    I'm a Python programmer, a software engineer, a developer, a graphic designer, and an artist. Currently, my focus
    is on two things: building a captivating portfolio that showcases my creative and technical skills, and sharpening 
    my programming abilities to present the best version of myself to future employers. I'm on a mission to bring innovation 
    and artistry together in the world of technology
    """
    st.info(content)


content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5]) #these are the ratio dimensions of each column, basically their widths

df = pandas.read_csv("data.csv", sep=";") #sep can be omitted if the data in the files are separated by ","

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"]) #method to add an image to the page
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
