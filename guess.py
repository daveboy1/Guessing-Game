import streamlit as st
import numpy as np
from PIL import Image
img = Image.open("dice.jpg")
st.image(img.resize((500,350)))
import random

st.header("Guessing Game")
st.subheader("Lets have some fun, guess the right number")

st.image("dice.jpg")

x = st. number_input("choose a number from 1-6",step=1)
x = int(x)
y = np.random.randint(1,7)

def gg(x,y):
    if x > 6:
        return(("Invalid number, choose number from 1-6"))
    else:
        st.write(f"Random number is {y}")
        st.write(f"Your choosen number is {x}")
    if x == y:
        st.balloons()
        return("correct")
    else:
        return("try again")

c1,c2 =st.columns(2)        

with c1:
    if st.button("Guess"):
        st.write(gg(x,y))   
with c2:
    if st.button("retry"):
        st.experimental_rerun()