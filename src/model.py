import pandas as pd
from src.preprocessing import preprocess 
from src.feature_engineering import create_features 
from src.next_app_model import train_next_app_model 

def train(): 
    df = pd.read_csv("data/raw/app_behavior.csv") 
    
    df = preprocess(df) 
    df = create_features(df) 
    
    # Train next app model 
    train_next_app_model(df) 
    
    print("All models trained successfully!") 
    
if __name__ == "__main__": 
    train()
    
    