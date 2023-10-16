import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2) #st is the module, columns is the method
                           #this method will return two column objects

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Eseose Odion")
    content = """Introducing Eseose Odion, a dynamic and multifaceted individual at the ripe age of 22.
    Eseose is a graduate of The University of Sheffield, where she successfully earned a Master of Computer Systems Engineering degree. 
    But that's just the beginning of her remarkable journey. Eseose is a true polymath, donning the hats of a Python programmer, software engineer, developer, graphic designer, and artist.
    Currently, she's immersed in the exciting pursuit of building a striking portfolio while honing her programming prowess, all in preparation to dazzle prospective employers with her diverse and innovative skill set.
    Eseose Odion is undeniably a captivating blend of technical finesse and creative flair, destined for a promising and vibrant career in the world of technology and design.
    """
    st.info(content)


content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)