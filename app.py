
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Charger les données (Remplace par ton fichier CSV final si besoin)
df = pd.read_csv('processed_feedback.csv')  # Remplace par le vrai fichier CSV

# Titre du dashboard
st.title('📊 AI Feedback Analyzer')

# 1️⃣ **Afficher le tableau des avis analysés**
st.subheader("📝 Avis Clients Analyés")
st.dataframe(df[['cleaned_text', 'sentiment_gpt', 'themes']])

# 2️⃣ **Graphique des sentiments**
st.subheader("📈 Répartition des Sentiments")

# Compter les sentiments
sentiment_counts = df['sentiment_gpt'].value_counts()

# Générer le graphique
fig, ax = plt.subplots()
ax.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', startangle=90, colors=['green', 'gray', 'red'])
ax.axis('equal')  # Pour un cercle parfait

st.pyplot(fig)

# 3️⃣ **Recherche d'avis**
st.subheader("🔎 Rechercher un avis")
search_term = st.text_input("Entrez un mot-clé pour filtrer les avis :", "")
if search_term:
    filtered_df = df[df['cleaned_text'].str.contains(search_term, case=False, na=False)]
    st.dataframe(filtered_df[['cleaned_text', 'sentiment_gpt', 'themes']])
