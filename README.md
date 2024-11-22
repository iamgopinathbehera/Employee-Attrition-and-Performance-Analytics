# 🚀 **Employee Attrition and Performance Analytics**

This repository contains analysis and predictive modeling focused on understanding employee attrition. The goal is to provide actionable insights and accurate predictions to help organizations enhance employee retention strategies.

---

## **Overview** 📝

### 1. **Exploratory Data Analysis (EDA)**

- **Objective:** Explore the dataset to uncover patterns and insights related to employee attrition.
- **Key Findings:**
  - 📊 **Attrition Rate:** 16% of employees left the company.
  - 📈 **Major Factors Influencing Attrition:**
    - **Overtime:** Employees working overtime are more likely to leave.
    - **Job Satisfaction:** Lower job satisfaction correlates with higher attrition.
    - **Income Levels:** Employees with lower monthly income are at greater risk of leaving.
  - **Visualizations:** Pie charts, histograms, and correlation heatmaps highlight feature distributions and relationships.

### 2. **Model Training**
- **Objective:** Develop and evaluate predictive models to classify employees likely to leave.

#### **Key Steps:**
- 🛠️ Preprocessed data (handled categorical variables, missing values, and scaling).
- ⚙️ Evaluated multiple machine learning models, including Logistic Regression, Random Forest, and Gradient Boosting.
- 📊 Compared models using performance metrics like accuracy, precision, and recall.

#### **Model Results:**
- 🤖 **Logistic Regression:** ~85% accuracy
- 🌲 **Random Forest:** ~89% accuracy
- 🌟 **Gradient Boosting:** ~91% accuracy

---

## **Visualizations** 📉
- **EDA:** Includes a pie chart for attrition distribution and bar plots showing feature importance.
- **Model Performance:** Displays accuracy comparisons across models using bar graphs.

---

## **Streamlit App** 🌐

A Streamlit app is included for an interactive exploration of the insights and predictions from this project.

### **How to Run the App**
1. **Install Streamlit:**
   ```shell
   pip install streamlit

---

Open the link provided in the terminal (e.g., http://localhost:8501) to access the app.

- How to Use ⚙️
**1.EDA Notebook**
Run the EDA - <i>Employee Attrition and Performance Analytics.ipynb<i> to explore the dataset and gain insights.

Key Outputs: Visualizations and initial statistical observations.

**2.Model Training Notebook**
Use the Model Training - <i>Employee Attrition and Performance Analytics.ipynb<i> to preprocess data and build models.

Evaluate models to identify the best approach for predicting attrition.


Key Findings and Recommendations 🔑

**Insights**:

- 🕒 Employees with excessive overtime, low satisfaction, or inadequate pay are at risk of leaving.
- 💼 Retention programs targeting these factors could significantly reduce attrition.

Actionable Steps:

⚖️ Improve work-life balance by minimizing overtime hours.
📋 Regularly survey job satisfaction and implement measures to address concerns.
💰 Review compensation structures to ensure competitive pay.

**Requirements**📦

Python 3.13

**Libraries:**

📚 Data Handling: pandas, numpy
📊 Visualization: matplotlib, seabornm plotly
🤖 Machine Learning: scikit-learn
🌐 Web App: streamlit

**Dataset 📂**
- The dataset includes anonymized employee records such as demographic details, job roles, satisfaction levels, income, and performance ratings.


