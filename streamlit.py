import streamlit as st
from Retrieval import get_response
import os

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
            background-color: rgba(0, 0, 0, 0.8);
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
        .conversation {{
            background-color: rgba(0, 0, 0, 0.8);
            border-radius: 10px;
            padding: 10px;
            margin-bottom: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

# Set the title of the Streamlit app
st.title("Geeta AI")

# Initialize session state for conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# Create a text input for the user query
user_query = st.text_input("Enter your Problems:")

# Create a button for search
if st.button("Ask Radhey"):
    if user_query:
        try:
            # Get the response from the model
            response = get_response(user_query)
            # Append the user query and response to the conversation history
            st.session_state.history.append({"query": user_query, "response": response})
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.write("Please enter a Problem to search.")

# Display the conversation history
st.subheader("Conversation")
for chat in st.session_state.history:
    st.markdown(f'<div class="conversation"><strong>Problem:</strong> {chat["query"]}<br><strong>Solution:</strong> {chat["response"]}</div>', unsafe_allow_html=True)

# Optionally, you can also add an image
image_path = "data/image.jpg"
if os.path.exists(image_path):
    st.image(image_path, caption="Bhagavad Gita")
else:
    st.warning("Image not found. Please check the path.")
