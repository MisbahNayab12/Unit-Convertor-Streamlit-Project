import streamlit as st

st.title("Unit Converter")

def converter(value: float, convert_from: str, convert_to: str):
    if convert_from == "km" and convert_to == "meter":
        return value * 1000
    elif convert_from == "meter" and convert_to == "cm":
        return value * 100
    elif convert_from == "meter" and convert_to == "km":
        return value / 1000
    elif convert_from == "cm" and convert_to == "meter":
        return value / 100
    else:
        return "Conversion not supported."

value = st.number_input("Enter value to convert:", value=1.0)
convert_from = st.selectbox("Convert from:", ["km", "meter", "cm"])
convert_to = st.selectbox("Convert to:", ["km", "meter", "cm"])

if convert_from != convert_to:
    result = converter(value, convert_from, convert_to)
    st.write(f"{value} {convert_from} is equal to {result} {convert_to}")
else:
    st.write("Please select different units to convert.")
    
