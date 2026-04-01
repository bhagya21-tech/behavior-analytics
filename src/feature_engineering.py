import pandas as pd 
from sklearn.cluster import KMeans 


def create_features(df): 
    df = df.copy()
    
    df["engagement_scores"] = (
        df["clicks"] * 0.4 + 
        df["scroll_depth"] * 100 * 0.6
        
    )
    
    
    return df 

def add_behavior_metrics(df):
    df["attention_span"] = df["session_length"]
    
    df["usage_type"] = df["session_length"].apply(
        lambda x: "High" if x > 10 else "Low"
    )
    
    df["time_category"] = df["hour"].apply(
        lambda x: "Night" if x >= 20 else
                  "Morning" if x < 12 else "Day"
    )
    
    return df

def app_level_analysis(df): 
    app_df = df.groupby("app").agg({
        "session_length": "mean",
        "clicks": "sum",
        "scroll_depth": "mean"
    }).reset_index()
    
    app_df.rename(columns={
        "session_length": "avg_session",
        "clicks": "total_clicks",
        "scroll_depth": "avg_scroll"
    }, inplace=True)
    
    return app_df 


def app_addiction_score(df):
    app_addiction = df.groupby("app").agg({
        "session_length": "mean",
        "clicks": "mean"
    }).reset_index() 
    
    app_addiction["addiction_score"] = (
        app_addiction["session_length"] * 0.6 + 
        app_addiction["clicks"] * 0.4
    )
    
    return app_addiction.sort_values("addiction_score", ascending=False) 


def create_user_features(df):
    user_df = df.groupby("user_id").agg({
        "session_length": "mean", 
        "clicks": "sum", 
        "scroll_depth": "mean"
    }).reset_index() 
    
    user_df.rename(columns={
        "session_length": "avg_session", 
        "clicks": "total_clicks", 
        "scroll_depth": "avg_scroll"
    }, inplace=True)
    
    return user_df

def add_clustering(user_df):
    features = user_df[["avg_session", "total_clicks", "avg_scroll"]]
    
    kmeans = KMeans(n_clusters=3, random_state=42)
    user_df["segment"] = kmeans.fit_predict(features) 
    
    return user_df 

def recommend_apps(df, user_id): 
    user_data = df[df["user_id"] == user_id] 
    
    top_apps = user_data["app"].value_counts().index.tolist()
    all_apps = df["app"].unique().tolist()
    
    recommendations = [app for app in all_apps if app not in top_apps] 
    
    return recommendations[:3] 

