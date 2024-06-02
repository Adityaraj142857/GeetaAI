# import streamlit as st
# from Retrieval import get_response
# import os

# # Set the title of the Streamlit app
# st.title("Geeta AI")

# # Create a text input for the user query
# user_query = st.text_input("Enter your Problem:")

# # Create a button for search
# if st.button("Ask Radhey"):
#     if user_query:
#         try:
#             # Get the response from the model
#             response = get_response(user_query)
#             # Display the response
#             st.write(response)
#         except Exception as e:
#             st.error(f"An error occurred: {e}")
#     else:
#         st.write("Please enter a query to search.")

# Optionally, you can also add an image
# image_path = "path/to/your/image.jpg"
# if os.path.exists(image_path):
#     st.image(image_path, caption="Bhagavad Gita")
# else:
#     st.warning("Image not found. Please check the path.")


############################################################33333
import streamlit as st
from Retrieval import get_response
import os

# Set the title of the Streamlit app
st.title("Geeta AI")

# Custom CSS to add a background image and style the app
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://images.unsplash.com/photo-1624030275207-77bac1c83be3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
            background-size: cover;
        }}
        .stTextInput > div > div > input {{
            background-color: rgba(255, 255, 255, 0.8);
        }}
        .stButton > button {{
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            transition-duration: 0.4s;
        }}
        .stButton > button:hover {{
            background-color: white;
            color: black;
            border: 2px solid #4CAF50;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

# Create a text input for the user query
user_query = st.text_input("Enter your Problem:")

# Create a button for search
if st.button("Ask Radhey"):
    if user_query:
        try:
            # Get the response from the model
            response = get_response(user_query)
            # Display the response
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.write("Please enter a query to search.")