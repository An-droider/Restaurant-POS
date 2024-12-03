
# import streamlit as st
# import os
# import pandas as pd

# # Set page configuration
# st.set_page_config(page_title="Food Menu", layout="wide")

# # Initialize the cart in session state as a list
# if "cart" not in st.session_state:
#     st.session_state.cart = []

# # Initialize the current page in session state
# if "page" not in st.session_state:
#     st.session_state.page = "menu"  # Default to menu page

# # Sample menu items divided into categories
# menu_items = {
#     "Appetizers": [
#         {"name": "Spring Rolls", "image": r"images\spring rolls.jpg", "price": 599},
#         {"name": "Garlic Bread", "image": r"images\Garlic Bread.jpg", "price": 399},
#         {"name": "Mozzarella Sticks", "image": r"images\Mozzarella sticks.jpg", "price": 399},
#         {"name": "Bruschetta", "image": r"images\Bruschetta.jpg", "price": 399},
#         {"name": "Chicken Wings", "image": r"images\Chicken Wings.jpg", "price": 399},
#         {"name": "Stuffed Mushrooms", "image": r"images\Stuffed Mushrooms.jpg", "price": 399},
#         {"name": "Nachos", "image": r"images\Nachos.jpg", "price": 399},
#         {"name": "Onion Rings", "image": r"images\onion rings.jpg", "price": 399},
#         {"name": "Spinach Artichoke Dip", "image": r"images\Spinach Artichoke Dip.jpg", "price": 399},
#         {"name": "Quesadillas", "image": r"images\Quesadillas.jpg", "price": 399},
#         {"name": "Crispy Calamari", "image": r"images\Crispy Calamari.jpg", "price": 399},
#         {"name": "Cheese Balls", "image": r"images\Cheese Balls.jpg", "price": 399},
#         {"name": "Hummus and Pita", "image": r"images\Hummus and Pita.jpg", "price": 399},
#     ],
#     "Main Course": [
#         {"name": "Margherita Pizza", "image": r"images\Margherita Pizza.jpg", "price": 1099},
#         {"name": "Cheeseburger", "image": r"images\Cheeseburger.jpg", "price": 899},
#         {"name": "Grilled Chicken Sandwich", "image": r"images\Grilled Chicken Sandwich.jpg", "price": 9.99},
#         {"name": "Spaghetti Bolognese", "image": r"images\Spaghetti Bolognese.jpg", "price": 999},
#         {"name": "Grilled Salmon", "image": r"images\Grilled Salmon.jpg", "price": 999},
#         {"name": "Chicken Alfredo Pasta", "image": r"images\Chicken Alfredo Pasta.jpg", "price": 999},
#         {"name": "Vegetarian Stir Fry", "image": r"images\Vegetarian Stir Fry.jpg", "price": 999},
#         {"name": "Chicken Parmigiana", "image": r"images\Chicken Parmigiana.jpg", "price": 999},
#         {"name": "Fish and Chips", "image": r"images\Fish and Chips.jpg", "price": 999},
#         {"name": "Lamb Curry", "image": r"images\Lamb Curry.jpg", "price": 999},
#         {"name": "Shrimp Scampi", "image": r"images\Shrimp Scampi.jpg", "price": 99},
#         {"name": "Vegetable Lasagna", "image": r"images\Vegetable Lasagna.jpg", "price": 999},
#     ],
#     "Desserts": [
#         {"name": "Chocolate Lava Cake", "image": r"images\Chocolate Lava Cake.jpg", "price": 699},
#         {"name": "Cheesecake", "image": r"images\Cheesecake.jpg", "price": 499},
#         {"name": "Tiramisu", "image": r"images\Tiramisu.jpg", "price": 699},
#         {"name": "Apple Pie", "image": r"images\Apple Pie.jpg", "price": 499},
#         {"name": "Ice Cream Sundae", "image": r"images\Cheesecake.jpg", "price": 699},
#         {"name": "Brownie with Ice Cream", "image": r"images\Ice Cream Sundae.jpg", "price": 499},
#         {"name": "Fruit Tart", "image": r"images\Brownie with Ice Cream.jpg", "price": 699},
#         {"name": "Banoffee Pie", "image": r"images\Banoffee Pie.jpg", "price": 499},
#     ]
# }

# # Check if the image files exist (in the local system) to avoid errors
# def check_image_files(category_items):
#     valid_items = []
#     for item in category_items:
#         if os.path.exists(item["image"]):
#             valid_items.append(item)
#         else:
#             st.warning(f"Image for {item['name']} not found at {item['image']}")
#     return valid_items

# # Add an item to the cart with quantity
# def add_to_cart(item):
#     # Check if item is already in cart, if yes update quantity
#     for cart_item in st.session_state.cart:
#         if cart_item['name'] == item['name']:
#             cart_item['quantity'] += 1
#             st.success(f"Added another {item['name']} to cart!")
#             return
#     # If not in cart, add new item
#     st.session_state.cart.append({"name": item["name"], "price": item["price"], "quantity": 1})
#     st.success(f"Added {item['name']} to cart!")

# # Display a section (Appetizers, Main Course, Desserts) with food items
# def display_menu_section(category, items):
#     st.header(category)
#     valid_items = check_image_files(items)
    
#     # Create a grid layout for each section
#     cols = st.columns(3)  # Adjust number of columns based on layout preference
#     for i, item in enumerate(valid_items):
#         with cols[i % 3]:
#             st.image(item["image"], use_column_width=True)
#             st.write(item["name"])
#             st.write(f"Rs.{item['price']:.2f}")
#             if st.button(f"Add to Cart", key=f"add_{item['name']}"):
#                 add_to_cart(item)

# # Display the menu page
# def menu_page():
#     st.title("Food Menu")
#     st.write("Browse through and select items to add to your cart.")
    
#     # Display each section (Appetizers, Main Course, Desserts)
#     for category, items in menu_items.items():
#         display_menu_section(category, items)
    
#     if st.button("Go to Cart"):
#          # Set query parameters to force a rerun with page change
#          st.switch_page(r"C:\Users\Admin\Desktop\jamia_dbms_proj\pages\Overview_Cart.py")


# # Main function to handle navigation between pages
# def main():
#     menu_page()
#     # # Check for query params to set the page
#     # query_params = st.experimental_get_query_params()
#     # if "page" in query_params:
#     #     st.session_state.page = query_params["page"][0]
    
#     # # Show the appropriate page based on session state
#     # if st.session_state.page == "menu":
#     #     menu_page()
#     # elif st.session_state.page == "cart":
#     #     cart_page()

# if __name__ == "__main__":
#     main()

import streamlit as st
import os
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Food Menu", layout="wide")

# Initialize the cart in session state as a list
if "cart" not in st.session_state:
    st.session_state.cart = []

# Sample menu items divided into categories
menu_items = {
    "Appetizers": [
        {"name": "Spring Rolls", "image": r"images\spring rolls.jpg", "price": 599},
        {"name": "Garlic Bread", "image": r"images\Garlic Bread.jpg", "price": 399},
        {"name": "Mozzarella Sticks", "image": r"images\Mozzarella sticks.jpg", "price": 399},
        {"name": "Bruschetta", "image": r"images\Bruschetta.jpg", "price": 399},
        {"name": "Chicken Wings", "image": r"images\Chicken Wings.jpg", "price": 399},
        {"name": "Stuffed Mushrooms", "image": r"images\Stuffed Mushrooms.jpg", "price": 399},
        {"name": "Nachos", "image": r"images\Nachos.jpg", "price": 399},
        {"name": "Onion Rings", "image": r"images\onion rings.jpg", "price": 399},
        {"name": "Spinach Artichoke Dip", "image": r"images\Spinach Artichoke Dip.jpg", "price": 399},
        {"name": "Quesadillas", "image": r"images\Quesadillas.jpg", "price": 399},
        {"name": "Crispy Calamari", "image": r"images\Crispy Calamari.jpg", "price": 399},
        {"name": "Cheese Balls", "image": r"images\Cheese Balls.jpg", "price": 399},
        {"name": "Hummus and Pita", "image": r"images\Hummus and Pita.jpg", "price": 399},
    ],
    "Main Course": [
        {"name": "Margherita Pizza", "image": r"images\Margherita Pizza.jpg", "price": 599},
        {"name": "Cheeseburger", "image": r"images\Cheeseburger.jpg", "price": 899},
        {"name": "Grilled Chicken Sandwich", "image": r"images\Grilled Chicken Sandwich.jpg", "price":799},
        {"name": "Spaghetti Bolognese", "image": r"images\Spaghetti Bolognese.jpg", "price": 999},
        {"name": "Grilled Salmon", "image": r"images\Grilled Salmon.jpg", "price": 999},
        {"name": "Chicken Alfredo Pasta", "image": r"images\Chicken Alfredo Pasta.jpg", "price": 999},
        {"name": "Vegetarian Stir Fry", "image": r"images\Vegetarian Stir Fry.jpg", "price": 999},
        {"name": "Chicken Parmigiana", "image": r"images\Chicken Parmigiana.jpg", "price": 999},
        {"name": "Fish and Chips", "image": r"images\Fish and Chips.jpg", "price": 999},
        {"name": "Lamb Curry", "image": r"images\Lamb Curry.jpg", "price": 999},
        {"name": "Shrimp Scampi", "image": r"images\Shrimp Scampi.jpg", "price": 199},
        {"name": "Vegetable Lasagna", "image": r"images\Vegetable Lasagna.jpg", "price": 999},
    ],
    "Desserts": [
        {"name": "Chocolate Lava Cake", "image": r"images\Chocolate Lava Cake.jpg", "price": 699},
        {"name": "Cheesecake", "image": r"images\Cheesecake.jpg", "price": 499},
        {"name": "Tiramisu", "image": r"images\Tiramisu.jpg", "price": 699},
        {"name": "Apple Pie", "image": r"images\Apple Pie.jpg", "price": 499},
        {"name": "Ice Cream Sundae", "image": r"images\Cheesecake.jpg", "price": 699},
        {"name": "Brownie with Ice Cream", "image": r"images\Ice Cream Sundae.jpg", "price": 499},
        {"name": "Fruit Tart", "image": r"images\Brownie with Ice Cream.jpg", "price": 699},
        {"name": "Banoffee Pie", "image": r"images\Banoffee Pie.jpg", "price": 499},
    ]
}

# Check if the image files exist to avoid errors
def check_image_files(category_items):
    valid_items = []
    for item in category_items:
        if os.path.exists(item["image"]):
            valid_items.append(item)
        else:
            st.warning(f"Image for {item['name']} not found at {item['image']}")
    return valid_items

# Add an item to the cart with quantity
def add_to_cart(item):
    # Check if item is already in cart, if yes update quantity
    for cart_item in st.session_state.cart:
        if cart_item["name"] == item["name"]:
            cart_item["quantity"] += 1
            st.success(f"Added another {item['name']} to cart!")
            return
    # If not in cart, add as new item
    st.session_state.cart.append({"name": item["name"], "price": item["price"], "quantity": 1})
    st.success(f"Added {item['name']} to cart!")

# Display a section (Appetizers, Main Course, Desserts) with food items
def display_menu_section(category, items):
    st.header(category)
    valid_items = check_image_files(items)
    
    cols = st.columns(3)  # Create grid layout
    for i, item in enumerate(valid_items):
        with cols[i % 3]:
            st.image(item["image"], use_column_width=True)
            st.write(item["name"])
            st.write(f"Rs.{item['price']:.2f}")
            if st.button(f"Add to Cart", key=f"add_{item['name']}"):
                add_to_cart(item)

# Display the menu page
def menu_page():
    st.title("Food Menu")
    st.write("Browse through and select items to add to your cart.")
    
    # Display each section (Appetizers, Main Course, Desserts)
    for category, items in menu_items.items():
        display_menu_section(category, items)
    
    if st.button("Go to Cart"):
        st.switch_page(r"C:\Users\Admin\Desktop\jamia_dbms_proj\pages\Overview_Cart.py")

# Display the cart page
def cart_page():
    st.title("Your Cart")
    
    # Check if the cart is empty
    if not st.session_state.cart:
        st.write("Your cart is empty.")
        if st.button("Back to Menu"):
            st.switch_page(r"C:\Users\Admin\Desktop\jamia_dbms_proj\pages\Menu.py")
    else:
        total_price = 0
        cart_data = []

        # Process cart items
        for item in st.session_state.cart:
            cart_data.append({
                "Item": item["name"],
                "Quantity": item["quantity"],
                "Price per Unit": item["price"],
                "Total Price": item["price"] * item["quantity"]
            })
            total_price += item["price"] * item["quantity"]

        # Convert to DataFrame and display as a table
        df = pd.DataFrame(cart_data)
        st.table(df)
        st.write(f"Total Price: Rs.{total_price:.2f}")

        # Proceed to payment button
        if st.button("Proceed to Payment"):
            st.switch_page(r"C:\Users\Admin\Desktop\jamia_dbms_proj\pages\Payment.py")

        # Option to go back to menu
        if st.button("Back to Menu"):
            st.switch_page(r"C:\Users\Admin\Desktop\jamia_dbms_proj\pages\Menu.py")

# Main function
def main():
    # Default to menu page
    menu_page()

if __name__ == "__main__":
    main()





