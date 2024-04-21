import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

# Streamlit UI components
st.title('Find the Largest Number')

# Creating form for better UI experience
with st.form("my_form"):
    num1 = st.number_input('Enter the first number:', step=1.0)
    num2 = st.number_input('Enter the second number:', step=1.0)
    num3 = st.number_input('Enter the third number:', step=1.0)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        largest = find_largest(num1, num2, num3)
        st.success(f'The largest number is: {largest}')

# Instructions
st.write("Please enter three numbers to find the largest one.")
