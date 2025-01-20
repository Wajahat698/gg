import streamlit as st

# Custom CSS to style Streamlit buttons like GPT
st.markdown("""
    <style>
    /* Centering the header text */
    .center-header {
        text-align: center;
        font-family: Arial, sans-serif;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .sub-header {
        text-align: center;
        font-family: Arial, sans-serif;
        font-size: 18px;
        color: gray;
        margin-bottom: 40px;
    }

    /* Styling Streamlit buttons to match GPT design */
    div.stButton > button {
        background-color: #ffffff;
        border: 1px solid #e5e5e5;
        border-radius: 12px;
        padding: 15px 20px;
        font-family: Arial, sans-serif;
        font-size: 18px;
        font-weight: 500;
        color: #000000;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        transition: transform 0.2s ease, background-color 0.3s ease, box-shadow 0.3s ease;
        width: 100%; /* Ensures buttons are consistent in size */
        max-width: 600px; /* Restricts width for larger screens */
        margin: 10px auto; /* Center-aligns buttons */
    }

    /* Hover effect for buttons */
    div.stButton > button:hover {
        background-color: #f7f7f7;
        box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.15);
        transform: translateY(-2px);
    }

    /* Responsive adjustments */
    @media (max-width: 768px) {
        div.stButton > button {
            font-size: 16px;
            padding: 12px 15px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="center-header">Get answers. Find inspiration. Be more productive.</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Free to use. Easy to try. Let us help you with writing, learning, and more.</div>', unsafe_allow_html=True)

# Suggestions
suggestions = [
    "Write a text inviting my neighbors to a barbecue",
    "Give me ideas for what to do with my kids' art",
    "Help me study vocabulary for a college entrance exam",
    "Write a message that goes with a kitten gif for a friend on a rough day"
]

# Display buttons in a vertical layout
for suggestion in suggestions:
    if st.button(suggestion, key=suggestion):
        # Trigger Python function or action here
        st.write(f"You clicked: {suggestion}")
