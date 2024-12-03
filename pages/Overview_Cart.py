import streamlit as st
import pandas as pd

st.title("Your Cart")
if not st.session_state.cart:
    st.write("Your cart is empty.")
else:
    total_price = 0
    cart_data = []
    for item in st.session_state.cart:
        cart_data.append({"Item": item["name"], "Quantity": item["quantity"], "Price": item["price"]})
        total_price += item["price"] * item["quantity"]
    df = pd.DataFrame(cart_data)

    custom_index = [f"{i + 1}" for i in range(len(cart_data))]
    df.index = custom_index
    st.table(df)
    st.write(f"Total Price: Rs.{total_price:.2f}")
    
    st.session_state.totalprice = total_price

    if st.button("Proceed to Payment"):
        st.switch_page(r"C:\Users\Admin\Desktop\jamia_dbms_proj\pages\Payment.py")
    #     st.session_state.cart.clear()  # Clear cart after payment
    #     # Set query parameters to force a rerun with page change
    #     st.experimental_set_query_params(page="menu")
    #     st.session_state.page = "menu"

    

# # if st.button("Back to Menu"):
# #     # Set query parameters to force a rerun with page change
# #     st.experimental_set_query_params(page="menu")
# #     st.session_state.page = "menu"
