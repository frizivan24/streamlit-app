import streamlit as st
import pandas as pd
import numpy as np

st.header("Friz Ivan P. Estoria")
st.write("Welcome to my first Streamlit web application!")

st.subheader("Sample Data")
df = pd.DataFrame({
    "Subject": ["Math", "Science", "English", "History"],
    "Score": [88, 92, 85, 90],
})
st.dataframe(df)

st.subheader("Bar Chart")
st.bar_chart(df.set_index("Subject"))

st.subheader("Line Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

st.subheader("Interactive Widgets")
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

age = st.slider("Select your age", 0, 100, 20)
st.write(f"You selected: {age}")

if st.button("Click me"):
    st.success("Button clicked!")
