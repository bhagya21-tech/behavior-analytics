import pandas as pd 
import numpy as np 
import random 

apps = ["Instagram", "YouTube", "WhatsApp", "Netflix", "LinkedIn"] 


def generate_data(n_users=500):
    data = [] 
    
    for user in range(n_users): 
        sessions = random.randint(10, 40) 
        
        for _ in range(sessions):
            app = random.choice(apps)
            session_length = np.random.exponential(scale=8) 
            clicks = np.random.randint(1, 50) 
            scroll_depth = np.random.uniform(0, 1)
            hour = random.randint(0, 23)             
             
            data.append([
                 user,
                 app,
                 session_length, 
                 clicks, 
                 scroll_depth,
                 hour,
            ])
            
    df = pd.DataFrame(data, columns=[
        "user_id", "app",  "session_length", "clicks", 
        "scroll_depth", "hour"
    ])
    
    return df 

if __name__ == "__main__": 
    df = generate_data()
    df.to_csv("data/raw/app_behavior.csv", index=False) 
    
    