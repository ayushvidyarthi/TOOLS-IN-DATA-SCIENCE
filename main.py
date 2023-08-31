import streamlit as st

st.title("Find the Largest Number")

# Input fields for three numbers
number1 = st.number_input("Enter the 1st number:")
number2 = st.number_input("Enter the 2nd number:")
number3 = st.number_input("Enter the 3rd number:")

# Function to find the largest number
def find_largest_number(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

if st.button("Find Largest"):
    largest = find_largest_number(number1, number2, number3)
    st.write(f"The largest number among {number1}, {number2}, and {number3} is {largest}")
  



