import streamlit as st 
import pandas as pd 
import joblib 

from src.feature_engineering import (
    create_features,
    add_behavior_metrics,
    app_level_analysis, 
    app_addiction_score,
    create_user_features, 
    add_clustering, 
    recommend_apps
) 


st.set_page_config(page_title="App Usage  Analytics", layout="wide") 

st.title("📱 App Usage Behavior Analytics Dashboard") 

# Upload file
uploaded_file = st.file_uploader("Upload  CSV", type=["csv"])
 

if uploaded_file:
    df = pd.read_csv(uploaded_file) 
    
    df = create_features(df) 
    df = add_behavior_metrics(df) 
    
    
    # --------------- APP ANALYSIS ---------------
    app_df = app_level_analysis(df) 
    
    st.subheader("🔥 Most Engaging Apps") 
    st.dataframe(app_df.sort_values("total_clicks", ascending=False)) 
    
    st.subheader("📉 Least Used Apps") 
    st.dataframe(app_df.sort_values("total_clicks").head()) 
    
    st.subheader("⏱ Attention Span") 
    st.bar_chart(app_df.set_index("app")["avg_session"]) 
    
    # ------------------ ADDICTION ------------
    st.subheader("⚠ Addiction Score") 
    addiction_df = app_addiction_score(df) 
    st.bar_chart(addiction_df.set_index("app")["addiction_score"]) 
    
    # ------------------ USER SEGMENT -----------
    user_df = create_user_features(df) 
    user_df  = add_clustering(user_df) 
    
    st.subheader("🧠 User Segments") 
    st.bar_chart(user_df["segment"].value_counts())
    
    # ---------------- NEXT APP --------------------
    st.subheader("🔮 Next App Prediction") 
    
    model = joblib.load("models/next_app_model.pkl")
    le = joblib.load("models/label_encoder.pkl") 
    
    
    selected_app = st.selectbox("Current App", df["app"].unique()) 
    hour = st.slider("Hour", 0, 23, 12) 
    
    app_encoded = le.transform([selected_app])[0]
    pred = model .predict([[app_encoded, hour]]) 
    pred_app = le.inverse_transform(pred)[0]
    
    st.success(f"Next app: {pred_app}") 
    
    
    # ---------------- RECOMMEND ---------------
    st.subheader("🎯 Recommendations") 
    
    user_id = st.selectbox("select User", df["user_id"].unique()) 
    recs = recommend_apps(df, user_id) 
    
    st.write("Recommended Apps:", recs) 
    
else: 
    st.info("Upload dataset to  begin") 
    
    