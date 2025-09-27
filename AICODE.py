import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import os

# --- Configuration ---
PROJECT_PATH = r'D:\SQL PROJECT'
DATA_FILE = os.path.join(PROJECT_PATH, 'OUTPUT.csv')

def predict_high_risk_sellers():
    """
    Trains a machine learning model to predict high-risk sellers.
    """
    print("--- Starting Step 6: AI Power-Up ---")
    
    # Load the data exported from our SQL query
    df = pd.read_csv(DATA_FILE)

    # --- Feature Engineering ---
    # Define what we consider "high risk". Let's say a risk_score of 4 or more.
    # This becomes our target variable (what we want to predict).
    df['is_high_risk'] = (df['risk_score'] >= 4).astype(int)

    # Define our features (the inputs to the model)
    features = ['total_orders', 'cancellation_rate_percent', 'avg_review_score']
    X = df[features]
    y = df['is_high_risk']

    # --- Model Training ---
    # Split data into a training set and a testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize and train the Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    print("✅ Model training complete.")

    # --- Model Evaluation ---
    # Make predictions on the test data
    y_pred = model.predict(X_test)
    
    # Calculate the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {accuracy:.2%}")
    print("\nThis means the model can predict whether a seller is high-risk with this level of accuracy.")
    
    # Show a confusion matrix for more detail
    print("\nConfusion Matrix:")
    print(pd.DataFrame(confusion_matrix(y_test, y_pred),
                       columns=['Predicted Not High-Risk', 'Predicted High-Risk'],
                       index=['Actual Not High-Risk', 'Actual High-Risk']))

if __name__ == "__main__":
    predict_high_risk_sellers()