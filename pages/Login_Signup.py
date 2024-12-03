
import streamlit as st
import mysql.connector
import hashlib

# Function to connect to the MySQL database
def create_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost",  # replace with your MySQL host
            user="root",       # replace with your MySQL username
            password="123",    # replace with your MySQL password
            database="rpos"    # replace with your database name
        )
    except:
        st.write ("The sql server is down!")

# Function to hash passwords (for security)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if the user exists
def login_user(username, password):
    conn = create_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hash_password(password)))
    user = cursor.fetchone()
    conn.close()
    if user:
        return True
    return False

# Function to create a new user (Signup)
def create_user(username, password):
    conn = create_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hash_password(password)))
        conn.commit()
        conn.close()
        return True
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        conn.close()
        return False

# Initialize session state for login tracking
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
    st.session_state['username'] = ""

# Function to render the login/signup page
def login_signup_page():
    st.title("Login / Sign Up")

    # Create tabs for Login and Signup
    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    # --- LOGIN FORM ---
    with tab1:
        st.subheader("Login")

        login_username = st.text_input("Username", key="login_username")
        login_password = st.text_input("Password", type="password", key="login_password")

        if st.button("Login"):
            if login_user(login_username, login_password):
                st.session_state['logged_in'] = True
                st.session_state['username'] = login_username
                st.success("Login successful!")
                st.switch_page(r"C:\Users\Admin\Desktop\jamia_dbms_proj\pages\Menu.py")
            else:
                st.error("Invalid username or password. Please try again.")

    # --- SIGNUP FORM ---
    with tab2:
        st.subheader("Sign Up")

        signup_username = st.text_input("Choose a Username", key="signup_username")
        signup_password = st.text_input("Choose a Password", type="password", key="signup_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")

        if st.button("Sign Up"):
            if signup_password != confirm_password:
                st.error("Passwords do not match!")
            else:
                if create_user(signup_username, signup_password):
                    st.success("User created successfully! You can now log in.")
                    
                else:
                    st.error("Username already exists or there was an error.")

# Function to render the main page after login
def main_page():
    st.title(f"Welcome, {st.session_state['username']}!")

    # Add a logout button
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.session_state['username'] = ""
        st.experimental_rerun()

    # Placeholder for account-specific content
    st.write("Welcome to Cafe De Flora! Explore around and find what you like and we will get it delivered for you!")

# Main Application Logic
if st.session_state['logged_in']:
    main_page()  # Show the main page if logged in
else:
    login_signup_page()  # Show the login/signup page if not logged in
