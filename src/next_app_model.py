import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
from sklearn.ensemble import RandomForestClassifier 
import joblib 

def train_next_app_model(df): 
    df = df.sort_values(["user_id", "hour"])
    
    df["next_app"] = df.groupby("user_id")["app"].shift(-1) 
    df = df.dropna() 
    
    le = LabelEncoder()
    df["app_encoded"] = le.fit_transform(df["app"]) 
    df["next_app_encoded"] = le.transform(df["next_app"]) 
    
    X = df[["app_encoded", "hour"]]
    y = df["next_app_encoded"] 
    
    model = RandomForestClassifier() 
    model.fit(X, y) 
    
    joblib.dump(model, "models/next_app_model.pkl") 
    joblib.dump(le, "models/label_encoder.pkl") 
    
    print("Next app model trained!") 
    