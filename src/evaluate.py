from sklearn.metrics import classification_report 
import joblib 
import pandas as pd 

from src.preprocessing import preprocess 
from src.feature_engineering import create_features , create_user_features

 
def evaluate():
    df = pd.read_csv("data/raw/user_behavior.csv") 
    
    df = preprocess(df) 
    df = create_features(df) 
    
    X = df.drop(["drop_off", "user_id"], axis=1) 
    y = df["drop_off"]
    
    model = joblib.load("models/model.pkl") 
    
    preds = model.predict(X) 
    
    print(classification_report(y, preds)) 
    
if __name__ == "__main__": 
    evaluate()