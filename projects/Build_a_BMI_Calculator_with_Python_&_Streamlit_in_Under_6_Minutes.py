import streamlit as st

# Custom CSS for whole page black background and content area styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: white;
        }
        
        body {
            background-color: white;
            color: white;
            font-family: 'Arial', sans-serif;
            padding: 20px;
        }

        .stDeployButton {
            display: none;
        }

        /* Style for input boxes and buttons */
        .stTextInput, .stNumberInput, .stRadio, .stButton {
            border-radius: 10px;
            border: 2px solid #fff;
            padding: 10px;
            background-color: pink;
            color: black;
            transition: background-color 0.3s ease, box-shadow 0.3s ease;
        }

        /* Hover effect for input boxes and buttons */
        .stTextInput:hover, .stNumberInput:hover, .stRadio:hover, .stButton:hover {
            background-color: #f1f1f1;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.7);
        }

        /* Styling for title and subtitles */
        h1, h2 {
            color: white !important;
        }

        /* Force black background on all containers */
        div[data-testid="stAppViewContainer"], 
        div[data-testid="stHeader"],
        div[data-baseweb="select"] {
            background-color: black !important;
        }

        /* Style for results text */
        .element-container {
            color: white !important;
        }

        /* Make all paragraph text blue */
        p {
            color: green !important;
        }

        /* Style for markdown text */
        .css-16idsys p {
            color: pink !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def calculate_bmi(weight, height):
    """Calculate BMI given weight and height."""
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """Classify the BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def user_interface():
    st.title("BMI Calculator")
    
    # Select weight and height units
    weight_unit = st.radio("Select your weight unit:", ("Kilograms (kg)", "Pounds (lbs)"))
    height_unit = st.radio("Select your height unit:", ("Meters (m)", "Centimeters (cm)"))
    
    # Input weight and convert if necessary
    if weight_unit == "Kilograms (kg)":
        weight = st.number_input("Enter your weight in kilograms (e.g., 70):", min_value=20.0, step=0.1)
    else:
        weight = st.number_input("Enter your weight in pounds (e.g., 154):", min_value=44.0, step=0.1)
        weight = weight / 2.205  # Convert pounds to kilograms
    
    # Input height and convert if necessary
    if height_unit == "Meters (m)":
        height = st.number_input("Enter your height in meters (e.g., 1.75):", min_value=0.5, step=0.01)
    else:
        height = st.number_input("Enter your height in centimeters (e.g., 175):", min_value=50.0, step=0.1)
        height = height / 100  # Convert centimeters to meters
    
    if weight > 0 and height > 0:
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        classification = classify_bmi(bmi)
        
        # Display results
        st.write(f"Your BMI is: **{bmi:.2f}**")
        
        # Show all categories
        st.subheader("BMI Categories:")
        st.write("""
        - **Underweight**: BMI less than 18.5  
        - **Normal weight**: BMI between 18.5 and 24.9  
        - **Overweight**: BMI between 25 and 29.9  
        - **Obesity**: BMI 30 or more  
        """, unsafe_allow_html=True)
        
        # Display user's category
        st.write(f"Based on your BMI, you are classified as: **{classification}**", unsafe_allow_html=True)
    else:
        st.write("Please enter valid weight and height values.")

if __name__ == "__main__":
    user_interface()
