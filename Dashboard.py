import streamlit as st
import base64


#turn on mysql server
# Set page configuration
st.set_page_config(page_title="Restaurant Landing Page", layout="wide")

# Function to encode the image in base64
def get_base64_image(image_file):
    with open(image_file, 'rb') as img:
        return base64.b64encode(img.read()).decode()

# Get the base64 encoded image (replace 'landingbg.png' with your image path)
img_base64 = get_base64_image('landingbg.png')

# Custom CSS to add the background image using base64
st.markdown(
    f"""
    <style>
     @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');


    .stApp {{
        background-image: url("data:image/png;base64,{img_base64}");
        background-size: cover;
        background-position: center;
    }}
   
    .main-header {{
        text-align: center;
        font-size: 8em;
        font-family: 'Great Vibes', cursive;
        color: #fff;
        margin-top: 150px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }}
    .sub-header {{
        text-align: center;
        font-size: 2em;
        font-family: 'Kozuka Gothic Pro', sans-serif;
        color: #fff;
        margin-top: 15px;
    }}
    .menu-btn {{
        display: block;
        margin: 30px 300px;
        padding: 10px 20px;
        font-size: 1.2em;
        color: #fff;
        background-color: #ff6347;
        border-radius: 3px;
        text-align: center;
        font-family: 'Kozuka Gothic Pro', sans-serif;
        text-decoration: none;
        cursor: pointer;
    }}
    
    </style>
    """,
    unsafe_allow_html=True
)

# Main content of the landing page
st.markdown("<h1 class='main-header'>Cafe De Flora </h1>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-header'>Where good food meets good memories!</h2><br><br><br>", unsafe_allow_html=True)
st.markdown(f"""
            
            
            
            
            """)



st.markdown("<h2 class = 'sub-header'> About Us  </h2>", unsafe_allow_html=True)
st.markdown(f"""Welcome to Café de Flore, a place where tradition meets modern elegance in the heart of Delhi. Established in 1887, Café de Flore is one of the oldest and most iconic cafes in the city, known for its timeless charm, artistic heritage, and literary spirit. From famous writers like Jean-Paul Sartre and Simone de Beauvoir to contemporary creatives, Café de Flore has been a gathering place for intellectuals, artists, and travelers for over a century.
At Café de Flore, we pride ourselves on offering a quintessential Parisian experience. Our carefully curated menu features classic French cuisine, from rich croissants and artisanal coffees in the morning to savory quiches, fresh salads, and fine wine throughout the day. Whether you’re here for a leisurely breakfast, a quick afternoon pick-me-up, or an elegant evening meal, we offer a cozy, welcoming atmosphere that captures the spirit of Paris.
Step inside and discover the vibrant ambiance of Café de Flore, where history, culture, and conversation flow as freely as our famous Mocktails!""")

st.markdown(f"""
                        
            



            
            """)
st.markdown("<h2 class = 'sub-header'> Dedicated to a Cause  </h2>", unsafe_allow_html=True)
st.markdown(f"""The cause of Café de Flora serving good food is deeply rooted in its dedication to creating a harmonious blend of flavor, ambiance, and connection. Inspired by the timeless charm of its name, Café de Flora seeks to transport its patrons to a world where every dish is an artful celebration of taste and tradition. The café is driven by a passion for using fresh, locally sourced ingredients and crafting recipes that honor both modern and classic culinary styles. 
Beyond simply serving meals, Café de Flora aims to nurture a sense of belonging, bringing people together in a warm and inviting space that feels like a retreat from the everyday. Its cause extends to promoting sustainability and supporting local artisans, making every dining experience a meaningful celebration of food, culture, and community.""")


st.markdown(f"""
                        
            


            
            
            """)
st.markdown("<h2 class = 'sub-header'> Take a Look!  </h2>", unsafe_allow_html=True)
images = [
    {"path": r"C:\Users\Admin\Desktop\jamia_dbms_proj\images\cafepics\Screenshot 2024-11-29 010118.png", "caption": "Beautiful Landscape"},
    {"path": r"C:\Users\Admin\Desktop\jamia_dbms_proj\images\cafepics\Screenshot 2024-11-29 010127.png", "caption": "Serene Beach"},
    {"path": r"C:\Users\Admin\Desktop\jamia_dbms_proj\images\cafepics\Screenshot 2024-11-29 010139.png", "caption": "Majestic Mountains"}
]

# Display images in the Streamlit app
for img in images:
    st.image(img["path"], use_column_width=True)

# Button to view the menu
#st.markdown("<a href='#' class='menu-btn'> Check out our delicious range! </a>", unsafe_allow_html=True)




# pages = {
#     "Home Page": [
#         st.Page("Login_signup.py", title="Log in/Sign up"),
#         st.Page("youraccount.py", title="Manage your account"),
#     ],
#     "Your Activity": [
#         st.Page("Menu.py", title="View the Menu"),
#         st.Page("Orders.py", title="Place order"),
        
#     ],
# }

# pg = st.navigation(pages)
# pg.run()