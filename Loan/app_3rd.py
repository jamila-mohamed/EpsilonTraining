import streamlit as st
import pandas as pd
import joblib


Inputs = joblib.load("Inputs.pkl")
Model = joblib.load("Model.pkl")

def prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, Family_Size, Total_Income, Debt_to_Income_Ratio, Monthly_Payment):
    test_df = pd.DataFrame(columns=Inputs)
    test_df.at[0,"Gender"] = Gender
    test_df.at[0,"Married"] = Married
    test_df.at[0,"Dependents"] = Dependents
    test_df.at[0,"Education"] = Education
    test_df.at[0,"Self_Employed"] = Self_Employed
    test_df.at[0,"ApplicantIncome"] = ApplicantIncome
    test_df.at[0,"CoapplicantIncome"] = CoapplicantIncome
    test_df.at[0,"LoanAmount"] = LoanAmount
    test_df.at[0,"Loan_Amount_Term"] = Loan_Amount_Term
    test_df.at[0,"Credit_History"] = Credit_History
    test_df.at[0,"Property_Area"] = Property_Area
    test_df.at[0,"Family_Size"] = Family_Size
    test_df.at[0,"Total_Income"] = Total_Income
    test_df.at[0,"Debt_to_Income_Ratio"] = Debt_to_Income_Ratio
    test_df.at[0,"Monthly_Payment"] = Monthly_Payment
    st.dataframe(test_df)
    result = Model.predict(test_df)[0]
    return result


    
def main():
    st.title("Loan Approval")
    Gender = st.selectbox("Gender" , ['Male', 'Female'])
    Married = st.selectbox("Married" , ['Yes', 'No'])
    Dependents = st.slider("Dependents" , min_value= 0 , max_value=10 , value=0,step=1)
    Education = st.selectbox("Education" , ['Graduate', 'Not Graduate'])
    Self_Employed = st.selectbox("Self_Employed" ,['No', 'Yes'])
    ApplicantIncome = st.slider("ApplicantIncome" , min_value=0, max_value=6000, value=0, step=1)
    CoapplicantIncome = st.slider("CoapplicantIncome" , min_value=0, max_value=6000, value=0, step=1)
    LoanAmount = st.slider("LoanAmount" , min_value=0, max_value=6000, value=0, step=1)
    Loan_Amount_Term = st.slider("Loan_Amount_Term" , min_value=0, max_value=6000, value=0, step=1)
    Credit_History = st.selectbox("Credit_History" , [0, 1])
    Property_Area = st.selectbox("Property_Area" , ['Rural', 'Urban', 'Semiurban'])
    Family_Size = st.slider("Family_Size" , min_value= 0 , max_value=10 , value=0,step=1)
    Total_Income = st.slider("Total_Income" , min_value=0, max_value=6000, value=0, step=1)
    Debt_to_Income_Ratio = st.slider("Debt_to_Income_Ratio" , min_value=0, max_value=6000, value=0, step=1)
    Monthly_Payment = st.slider("Monthly_Payment" , min_value=0, max_value=6000, value=0, step=1)
    
    if st.button("predict"):
        result = prediction(Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area, Family_Size, Total_Income, Debt_to_Income_Ratio, Monthly_Payment)
        label = ["Declined" , "Approved"]
        st.text(f"The Resturant will {label[result]}")
        
if __name__ == '__main__':
    main()    
    
