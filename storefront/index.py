import streamlit as st

# Define a function for each page
def home():
    st.title("🏠 Home Page")
    st.write("Welcome to the Home Page of our multi-page Streamlit app!")

def menu_page():
    st.title("🍔 Menu Page")
    st.write("This is the Menu Page where users can view food items.")
    menu = {
        "Pizza": 10.99,
        "Burger": 7.99,
        "Fries": 2.99,
        "Salad": 5.99,
        "Soda": 1.99
    }

    st.write("### Available Menu Items:")
    for item, price in menu.items():
        st.write(f"{item}: ${price}")

def order_page():
    st.title("🛒 Order Page")
    st.write("This is the Order Page where users can place an order.")
    
    # Store user's order
    menu = {
        "Pizza": 10.99,
        "Burger": 7.99,
        "Fries": 2.99,
        "Salad": 5.99,
        "Soda": 1.99
    }
    
    order = {}
    for item, price in menu.items():
        quantity = st.number_input(f"{item} (${price})", min_value=0, max_value=10, step=1)
        if quantity > 0:
            order[item] = quantity
    
    # Calculate the total price
    if order:
        total_price = sum(menu[item] * quantity for item, quantity in order.items())
        st.write("### Your Order:")
        for item, quantity in order.items():
            st.write(f"{item}: {quantity} x ${menu[item]:.2f} = ${menu[item] * quantity:.2f}")
        st.write(f"**Total: ${total_price:.2f}**")
        
        if st.button("Submit Order"):
            st.success("Thank you for your order!")
    else:
        st.write("Please select at least one item to order.")

def about_page():
    st.title("ℹ️ About Page")
    st.write("This is the About Page. Learn more about our app and team here.")

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Menu", "Order", "About"])

# Render the selected page
if selection == "Home":
    home()
elif selection == "Menu":
    menu_page()
elif selection == "Order":
    order_page()
elif selection == "About":
    about_page()
