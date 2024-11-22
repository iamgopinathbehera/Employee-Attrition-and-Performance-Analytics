import streamlit as st
import pickle
import numpy as np

# Load the trained Random Forest model

with open(r'C:\Users\ASUS\ML Domain Studies\Machine Learning\Employee Attrition and Performance Analytics\model\best_random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# App title and description
st.title("🧑‍💻 Employee Attrition Prediction")
st.image("attrition_banner.png", use_column_width=True) 
st.markdown(
    """
    Predict whether an employee is likely to leave the organization using the latest data and machine learning model. 
    Simply fill in the details below, and we'll provide the prediction!
    """
)

# Input form with constraints and emojis
st.sidebar.header("Enter Employee Details")

# Helper function for constrained numeric input with proper formatting
def constrained_input(label, min_value, max_value, default, step, is_float=True):
    """
    Helper function to streamline input with correct typing and formatting
    """
    format_str = "%.1f" if is_float else "%.0f"
    value = st.sidebar.number_input(
        label,
        min_value=float(min_value) if is_float else int(min_value),
        max_value=float(max_value) if is_float else int(max_value),
        value=float(default) if is_float else int(default),
        step=float(step) if is_float else int(step),
        format=format_str
    )
    return value

inputs = {}

# Numeric fields with constraints
inputs['Age'] = constrained_input("Age", 18, 65, 30, 1)
inputs['DailyRate'] = constrained_input("Daily Rate", 0, 1000, 200, 10)
inputs['DistanceFromHome'] = constrained_input("Distance From Home (km)", 0, 50, 10, 1)
inputs['Education'] = constrained_input("Education Level (1: Low, 5: High)", 1, 5, 3, 1)
inputs['EnvironmentSatisfaction'] = constrained_input("Environment Satisfaction (1: Low, 5: High)", 1, 5, 3, 1)
inputs['HourlyRate'] = constrained_input("Hourly Rate ($)", 10, 150, 50, 1, is_float=True)
inputs['JobInvolvement'] = constrained_input("Job Involvement (1: Low, 5: High)", 1, 5, 3, 1)
inputs['JobLevel'] = constrained_input("Job Level", 1, 5, 2, 1)
inputs['JobSatisfaction'] = constrained_input("Job Satisfaction (1: Low, 5: High)", 1, 5, 3, 1)
inputs['MonthlyIncome'] = constrained_input("Monthly Income ($)", 1000, 50000, 5000, 500)
inputs['MonthlyRate'] = constrained_input("Monthly Rate ($)", 1000, 100000, 20000, 1000)
inputs['NumCompaniesWorked'] = constrained_input("Number of Companies Worked", 0, 15, 2, 1)
inputs['PercentSalaryHike'] = constrained_input("Percent Salary Hike (%)", 0, 50, 10, 1, is_float=True)
inputs['PerformanceRating'] = constrained_input("Performance Rating (1: Low, 5: High)", 1, 5, 3, 1)
inputs['RelationshipSatisfaction'] = constrained_input("Relationship Satisfaction (1: Low, 5: High)", 1, 5, 3, 1)
inputs['TotalWorkingYears'] = constrained_input("Total Working Years", 0, 50, 10, 1)
inputs['TrainingTimesLastYear'] = constrained_input("Training Times Last Year", 0, 10, 3, 1)
inputs['WorkLifeBalance'] = constrained_input("Work-Life Balance (1: Low, 5: High)", 1, 5, 3, 1)
inputs['YearsAtCompany'] = constrained_input("Years at Company", 0, 40, 5, 1)
inputs['YearsInCurrentRole'] = constrained_input("Years in Current Role", 0, 20, 3, 1)
inputs['YearsSinceLastPromotion'] = constrained_input("Years Since Last Promotion", 0, 15, 2, 1)
inputs['YearsWithCurrManager'] = constrained_input("Years With Current Manager", 0, 15, 3, 1)

# Categorical fields
inputs['Gender'] = 1 if st.sidebar.selectbox("Gender (👩 / 👨)", ['Male', 'Female']) == 'Male' else 0
inputs['OverTime'] = 1 if st.sidebar.selectbox("Overtime (⌚ Yes/No)", ['Yes', 'No']) == 'Yes' else 0

# One-hot encoded categorical fields
categories = [
    'BusinessTravel_Non-Travel', 'BusinessTravel_Travel_Frequently', 'BusinessTravel_Travel_Rarely',
    'Department_Human Resources', 'Department_Research & Development', 'Department_Sales',
    'EducationField_Human Resources', 'EducationField_Life Sciences', 'EducationField_Marketing',
    'EducationField_Medical', 'EducationField_Other', 'EducationField_Technical Degree',
    'JobRole_Healthcare Representative', 'JobRole_Human Resources', 'JobRole_Laboratory Technician',
    'JobRole_Manager', 'JobRole_Manufacturing Director', 'JobRole_Research Director',
    'JobRole_Research Scientist', 'JobRole_Sales Executive', 'JobRole_Sales Representative',
    'MaritalStatus_Divorced', 'MaritalStatus_Married', 'MaritalStatus_Single'
]

for category in categories:
    inputs[category] = 1 if st.sidebar.checkbox(category.replace("_", " ")) else 0

# Prediction button
if st.sidebar.button("Predict Attrition 💡"):
    # Prepare input array
    input_values = np.array(list(inputs.values())).reshape(1, -1)
    
    # Prediction
    prediction = model.predict(input_values)[0]
    
    # Display result
    if prediction == 1:
        st.error("🔴 The employee is likely to leave the organization.")
        st.image("leaving.png", caption="Employee at risk!", use_column_width=True)  
    else:
        st.success("🟢 The employee is likely to stay with the organization.")
        st.image("stayings.png", caption="Employee retention strong!", use_column_width=True)  
