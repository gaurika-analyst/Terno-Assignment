import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')

def train_and_predict():
    print("🚀 Initializing Terno Churn Prediction Pipeline...\n")
    
    # 1. Load and prepare historical data
    df = pd.read_excel('ecommerce_churn.xlsx')
    le = LabelEncoder()
    df['HasSupportTicket'] = le.fit_transform(df['HasSupportTicket'])
    df['Churned'] = le.fit_transform(df['Churned'])
    
    X = df.drop(['UserID', 'Churned'], axis=1)
    y = df['Churned']
    
    # 2. Train Model
    model = RandomForestClassifier(random_state=42, n_estimators=100)
    model.fit(X, y)
    print("✅ Model trained successfully on historical data.")
    
    # 3. Simulate a new customer prediction
    print("\n📊 Simulating prediction for a NEW customer...")
    
    # Dummy data for a customer whose engagement has dropped
    new_customer = pd.DataFrame({
        'VisitsLast30Days': [2],
        'TimeOnSite': [15.5],
        'PurchaseCount': [1],
        'HasSupportTicket': [0] # 0 = No
    })
    
    prediction = model.predict(new_customer)
    probability = model.predict_proba(new_customer)[0][1]
    
    print(f"Customer Profile: {new_customer.to_dict(orient='records')[0]}")
    
    # Business logic output
    if prediction[0] == 1:
        print(f"\n⚠️  ALERT: High Risk of Churn! (Probability: {probability:.0%})")
        print("💡 Action: Trigger automated retention email with a personalized discount.")
    else:
        print(f"\n✅ Customer is Safe. (Churn Probability: {probability:.0%})")

if __name__ == "__main__":
    train_and_predict()