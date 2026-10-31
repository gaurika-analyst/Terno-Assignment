# Terno AI Internship Challenge: E-Commerce Churn Prediction

## 📌 Overview
This repository contains an end-to-end Machine Learning pipeline to predict customer churn in an e-commerce setting. The project analyzes behavioral and transactional data to identify high-risk customers, enabling proactive retention strategies.

## 📂 Project Structure
- `notebook.ipynb`: Complete Exploratory Data Analysis (EDA), data preprocessing, and Random Forest model training.
- `blog_draft.md`: A business-focused blog post translating model insights into actionable retention strategies.
- `ecommerce_churn.xlsx`: The dataset used for model training.
- `bonus.py`: A standalone CLI inference script simulating churn prediction on new, unseen customer data.

## 🚀 Key Findings
- **TimeOnSite** (36.1%) and **VisitsLast30Days** (34.2%) are the strongest predictors of churn.
- Customer support tickets have minimal impact on retention in this specific dataset.
- **Business Action:** Automated retention triggers should be deployed when a user's site engagement drops, rather than waiting for support complaints.

## 💻 How to Run
1. Install dependencies: 
   ```bash
   pip install pandas scikit-learn matplotlib seaborn openpyxl

2. Run the Jupyter Notebook to view the EDA and model evaluation.
3. Execute the bonus inference script in the terminal to see a real-time prediction simulation:
   ```bash
   python bonus.py
