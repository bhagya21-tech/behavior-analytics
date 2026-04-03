
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

# UI CONFIG # 

st.set_page_config(
    
    page_title="App Analytics Dashboard", 
    layout="wide"
) 

# --------------- CUSTOM CSS ---------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
section[data-testid="stsidebar"] {
    background-color: #111827;
}
.metric-card { 
    background-color: #1f2937;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ------------ SIDEBAR ----------------
st.sidebar.title("📱 App Analytics")
page = st.sidebar.radio("Navigate", [
    "Dashboard", 
    "App Insights",
    "User Segments", 
    "Prediction",
    "Recommendations"
])

# Upload file
uploaded_file = st.sidebar.file_uploader("Upload  CSV", type=["csv"])
 

if uploaded_file:
    df = pd.read_csv(uploaded_file) 
    
    df = create_features(df) 
    df = add_behavior_metrics(df) 
    
    
    # --------------- DASHBOARD ---------------
    if page == "Dashboard": 
        st.title("📊 Overview") 
        
        col1, col2, col3 = st.columns(3) 
        
        col1.metric("Total Users", df["user_id"].nunique())
        col2.metric("Avg Session", round(df["session_length"].mean(), 2))
        col3.metric("Total Clicks", int(df["clicks"].sum()))
        
        st.markdown("---") 
        
        st.subheader("⏱ Attention Span") 
        app_df = app_level_analysis(df) 
        st.bar_chart(app_df.set_index("app")["avg_session"]) 
        
    # ---------------- APP INSIGHTS ----------------
    elif page == "App Insights": 
        st.title("🔥 App Insights")
        
        app_df = app_level_analysis(df) 
        
        col1, col2 = st.columns(2) 
        
        with col1: 
            st.subheader("Top Apps") 
            st.dataframe(app_df.sort_values("total_clicks", ascending=False))
            
        with col2: 
            st.subheader("Low Usage Apps") 
            st.dataframe(app_df.sort_values("total_clicks").head())
            
        st.markdown("---") 
        
        st.subheader("⚠ Addiction Score")
        addiction_df = app_addiction_score(df)
        st.bar_chart(addiction_df.set_index("app")["addiction_score"]) 
        
        # ---------------- USER SEGMENTS -------------
    elif page == "User Segments": 
        st.title("🧠 User Behavior Clusters") 
        
        user_df = create_user_features(df) 
        user_Df = add_clustering(user_df)
        
        st.bar_chart(user_df["segment"].value_counts())
        
        st.markdown("---")
        
        st.dataframe(user_df.head())
        
        # ------------------- PREDICTION ----------------
    elif page == "Prediction": 
        st.title("🔮 Next App Prediction") 
    
        model = joblib.load("models/next_app_model.pkl") 
        le = joblib.load("models/label_encoder.pkl") 
        
        col1, col2 = st.columns(2) 
        
        with col1:
            selected_app = st.selectbox("Current App", df["app"].unique()) 
            
        with col2: 
            hour = st.slider("Hour", 0, 23, 12) 
            
        app_encoded = le.transform([selected_app])[0]
        pred = model.predict([[app_encoded, hour]])
        pred_app = le.inverse_transform(pred)[0] 
        
        st.success(f"📱 Next App: {pred_app}") 
        
    
    # ------------------ RECOMMENDATION ---------------
    elif page == "Recommendations":
        st.title("🎯 Smart Recommendations") 
        
        user_id = st.selectbox("Select USer", df["user_id"].unique())
        
         
        recs = recommend_apps(df, user_id)
        
        st.markdown("### Recommended Apps") 
        for app in recs:
            st.write(f"👉 {app}") 
            
    else: 
        st.title("📱 App Usage Analytics") 
        st.info("Upload your dataset from the sidebar to begin")
        
    