# Stopping the Leak: Predicting E-commerce Churn Before It Happens

### The Problem: Why Customer Retention Matters
In the highly competitive world of e-commerce, acquiring a new customer is significantly more expensive than retaining an existing one. When users stop buying and abandon a platform (known as customer churn), businesses lose their most valuable asset: recurring revenue. The challenge isn't just knowing *that* customers are leaving, but predicting *who* will leave and *why* before they actually do.

For this Terno AI Internship Challenge, I decided to tackle this exact problem. I defined a real-world analytics use case: predicting customer churn using behavioral and transactional data to enable proactive, targeted retention campaigns.

### What I Did: Building the AI Pipeline
I worked with an e-commerce dataset containing customer engagement metrics such as website visits in the last 30 days, total time spent on the site, purchase count, and support ticket history. 

Here is how I structured my AI-assisted workflow:
1. **Data Preparation:** I cleaned the dataset and converted categorical text variables (like Yes/No) into machine-readable numerical formats using Label Encoding.
2. **Exploratory Data Analysis (EDA):** I visualized the churn distribution and plotted a correlation heatmap to understand how different behaviors interact. 
3. **Machine Learning Model:** I trained a Random Forest Classifier to predict whether a customer was at risk of churning.
4. **Evaluation:** I extracted the 'Feature Importances' from the model to understand the driving forces behind user drop-offs.

### The Findings: What the Data Revealed
The results from the model were highly insightful. Instead of customer service issues driving churn, the top predictors were entirely engagement-based:
* **TimeOnSite** emerged as the strongest predictor (36.1% importance).
* **VisitsLast30Days** was a close second (34.2% importance).
* Surprisingly, whether a user raised a **Support Ticket** had almost no impact on their likelihood to churn (only 5% importance).

### Real-World Impact and Business Outcome
This analysis provides a clear, actionable outcome. Instead of blindly sending generic discount codes to all users—which wastes marketing budget—the e-commerce company can use this AI pipeline to monitor engagement. 

If a highly valuable customer suddenly drops their 'TimeOnSite' or stops visiting the platform as frequently, the system can flag them as "High Risk." The marketing team can then trigger an automated, personalized retention campaign, effectively saving the customer relationship and boosting overall profitability.