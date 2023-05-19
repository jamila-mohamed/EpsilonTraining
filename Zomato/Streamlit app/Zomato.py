import streamlit as st
import joblib
import pandas as pd

# Load the model and scaler
model = joblib.load("random_forest.joblib")
scaler = joblib.load("scaler.joblib")

# Function to predict the rating
def predict_rating(input_data):
    # Map "False" and "True" options back to 0 and 1
    input_data["online_order"] = input_data["online_order"].map({"No": 0, "Yes": 1})
    input_data["book_table"] = input_data["book_table"].map({"No": 0, "Yes": 1})
    
    # Preprocess the data using the scaler
    input_data = scaler.transform(input_data)
    
    # Predict using the loaded model
    output = model.predict(input_data)
    
    return output[0]

# Define the app
def app():
    # Set the title
    st.set_page_config(page_title="Zomato", page_icon=":pizza:", layout="wide")

    st.markdown(
    """
    <style>
        body {
            background-color: #FBBF77;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

    st.markdown(
    """
    <style>
        .stButton>button {
            width: 100%;
            height: 50px;
            font-size: 30px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
    
     # Add CSS to center the title
    st.markdown("<h1 style='text-align: center; color: #ff4500;'>Restaurant Quality Predictor</h1><h3 style='text-align: center'>Based on Zomato's dataset</h3>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("")
    
    st.markdown("<h6 style='text-align: left;'>This application uses a pre-trained machine learning model called Random Forest to predict the likelihood of a new restaurant in Bangalore being good or not based on various user inputs. These inputs include factors such as online ordering, table booking, location, restaurant type, cuisine, cost, and type of meal.</h6>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("")

    # Add labels to the form inputs
    st.markdown("<h6 style='text-align: center;'>Fill us in on the delicious details: <span>🔽</span></h6>", unsafe_allow_html=True)
    
    online_order = st.selectbox("**Online Order**", ["No", "Yes"])
    book_table = st.selectbox("**Book Table**", ["No", "Yes"])
    location = st.slider("**Location**", 0, 85, 0)
    rest_type = st.slider("**Restaurant Type**", 0, 50, 0)
    cuisines = st.slider("**Cuisines**", 0, 1184, 0)
    cost = st.number_input("**Approximate Cost for Two People**", value=0)
    listed_in = st.slider("**Type of Meal**", 0, 6, 0)
    
    # Convert the user inputs to a pandas dataframe
    user_inputs = {
        "online_order": online_order,
        "book_table": book_table,
        "location": location,
        "rest_type": rest_type,
        "cuisines": cuisines,
        "approx_cost(for two people)": cost,
        "listed_in(type)": listed_in
    }
    input_data = pd.DataFrame(user_inputs, index=[0])
    
    # Predict the rating using the loaded model
    predicted_rating = predict_rating(input_data)
    
    # Display the predicted rating
    st.markdown("---")
    st.write("")
    st.write("")

    if st.button("**Ready?**"):
        if predicted_rating == 0.0:
            st.markdown("<h3 style='text-align: center; color: #ff4500;'>Likely unsuccessful</h3>", unsafe_allow_html=True)
        elif predicted_rating == 1.0:
            st.markdown("<h3 style='text-align: center; color: #ff4500;'>Likely successful</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='text-align: center;'>The predicted rating is: {:.1f}</h3>".format(predicted_rating), unsafe_allow_html=True)

    st.write("")

    
# Run the app
if __name__ == "__main__":
    app()