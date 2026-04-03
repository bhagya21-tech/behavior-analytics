<<<<<<< HEAD
# 📱 App Usage Behavior Analytics System 

An end-to-end data science project that analyzes user interaction logs to uncover behavioral patterns, predict next app usage, detect addiction trends, and generate personalized recommendations.

---

🚀 Project Overview
-
This project simulates real-world product analytics by analyzing how users interact with different applications. 

it provides insight into: 
* 🔥 Most engaging apps 
* 📉 Low Usage apps 
* ⏱ User attention span 
* 🌙 Time-based usage patterns 
* ⚠ Addiction behavior 
* 🔮 Next app prediction
* 🎯 Personalized recommendations 

---

🧠 Key Features 
- 

📊 Behavioral Analytics 

* App-level engagement tracking  
* Attention span analysis
* Time-of-day usage insights 

⚠ Addiction Scoring 

* Calculates addiction score based on session duration and interaction intensity

🧍‍♂️ User Segmentation 

* Clusters users into behavioral groups using KMeans 

🔮 Next App Prediction 

* Predicts which app a user is likely to open next 

* Built using sequence modeling + Random Forest 

🎯 Recommendation System 

* Suggests new apps based on user behavior patterns 

📈 Interactive Dashboard 

* Built with Streamlit  
* Displays insights, predictions, and metrics in real-time 

--- 

🏗 Project Structure
- 

```python
behavior_analytics/
|
├──data/
|   └── raw/app_behavior.csv
|
├──src/
|   ├──__init__.py
|   ├──data_generator.py
|   ├──preprocessing.py
|   ├──feature_engineering.py
|   ├──next_app_model.py
|   ├──model.py
|
├──app/
|   └──app.py
|
├──models/
|   ├── next_app_model.pkl
|   └──label_encoder.pkl
| 
├──requirements.txt
└──README.md
```

---

⚙ Tech Stack 
-

* Python 
* Pandas, Numpy
* Scikit-learn 
* Streamlit 
* Joblib 

---

📊 How  It Works 

1. Data Generation
   * Simulates app usage logs for multiple users

2. Feature Engineering 
   * Engagement score
   * Attention span 
   * Time-based usage categories 

3. Modeling 
   * Random Forest for next app prediction 
   * KMeans for user segmentation

4. Analytics 
   * App-level and user-level insights 

5. Deployment 
   * Interactive dashboard using Streamlit 

---


```python
🚀 How to Run the Project

1️⃣ Clone the repository 
git clone https://github.com/bhagya21-tech/behavior-analytics.git
cd behavior-analytics 

---

2️⃣ Install dependencies 

pip install -r requirements.txt 

---

3️⃣ Generate dataset 

python src/data_generator.py

---

4️⃣ Train models 

python -m src.model 

---

5️⃣ Run the app 

python -m streamlit run app/app.py

---
```

🎯 Business Impact 
- 

This system mimics real-world product analytics used by: 

* Social media platforms 
* Streaming services 
* Mobile applications 

it helps answer key questions like: 

* Which apps drive engagement? 
* when do user drop off? 
* What Keeps users hooked? 
* What should be recommended next? 

---

🙋‍♀️ Author 

Bhagyashri Raut 

---

=======
