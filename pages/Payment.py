import streamlit as st
import random

# Streamlit UI
st.title("Payment Details")

# Form to collect user payment details

if 'totalprice' in st.session_state:
    total_price = st.session_state.totalprice
    st.write(f"Total Price to be Paid: Rs.{total_price:.2f}")
else:
    st.write("No total price found. Please go back to the cart.")

with st.form(key='payment_form'):
    name = st.text_input("Full Name", placeholder="Enter your full name")
    card_number = st.text_input("Card Number", type='password', placeholder="Enter your card number")
    card_expiry = st.text_input("Expiry Date (MM/YY)", placeholder="MM/YY")
    card_cvc = st.text_input("CVC", type='password', placeholder="Enter your CVC")
    
    submit_button = st.form_submit_button("Submit Payment")

if submit_button:
    # Display the collected information (for demo purposes only)
    st.success("Payment details submitted successfully!")
    st.session_state['order_number'] = random.randint(1,100000)

    st.switch_page(r"C:\Users\Admin\Desktop\jamia_dbms_proj\pages\View_Bill.py")
    #st.session_state.cart.clear()  # Clear cart after payment
    # Set query parameters to force a rerun with page change
    # st.experimental_set_query_params(page="menu")
    # st.session_state.page = "menu"







