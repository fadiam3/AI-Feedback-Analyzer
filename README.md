# 🏆 Analyse des Avis Clients avec l'IA  

## 🚀 Objectif du projet  
L’objectif est d’automatiser l’analyse des avis clients en détectant leur **sentiment** (positif, négatif, neutre) et en extrayant les **thèmes principaux** pour aider les entreprises à mieux comprendre leurs clients.

## 📌 Problème adressé  
Les entreprises reçoivent des milliers d’avis clients sur diverses plateformes (Amazon, Google Reviews, Trustpilot...). Analyser manuellement ces avis est chronophage.  
Cette solution IA permet de **gagner du temps** et d’**extraire des insights actionnables**.

## 📂 Données utilisées  
- **Source :** Dataset public Kaggle [Amazon Fine Food Reviews](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)  
- **Colonnes clés :** `reviewText` (texte de l’avis), `Score` (note attribuée), `UserId` (ID client)  
- **Optionnel :** Scraping en temps réel pour enrichir les données  

## 🛠️ Stack Technologique  
- **Langage :** Python 🐍  
- **Data processing :** Pandas, NLTK (Nettoyage du texte)  
- **Analyse des sentiments :**  
  - GPT-4 Turbo (via OpenAI API)  
  - Alternative open-source : DistilBERT (Hugging Face)  
- **Extraction de thèmes :** KeyBERT (modèle basé sur BERT)  
- **Visualisation & UI :**  
  - **Streamlit** (Mini-dashboard interactif)  
  - **Matplotlib** (Graphique des sentiments)  

## 📍 Workflow du projet  
### 1️⃣ Collecte et Exploration des Données  
- Chargement du dataset Kaggle / Scraping  
- Visualisation initiale des avis clients  

### 2️⃣ Prétraitement des Données  
- Suppression des valeurs manquantes et des doublons  
- Nettoyage des textes (tokenisation, suppression des stopwords, stemming)  

### 3️⃣ Analyse des Sentiments  
- Envoi des avis à **GPT-4 Turbo** pour classifier en **positif / neutre / négatif**  
- Alternative sans API : **DistilBERT** (modèle open-source NLP)  

### 4️⃣ Extraction des Thèmes  
- Utilisation de **GPT-4** ou **KeyBERT** pour détecter les thématiques des avis  
- Exemples de thèmes extraits : **"Service client"**, **"Qualité du produit"**, **"Prix"**  

### 5️⃣ Déploiement et Visualisation  
- **Dashboard interactif** avec Streamlit  
- **Graphique des sentiments** pour observer la tendance globale  
- **Moteur de recherche** pour explorer les avis par mots-clés  

## 🎯 Résultats et Impact  
✅ **Automatisation de l’analyse des avis clients** → Gain de temps pour les équipes  
✅ **Détection rapide des tendances et des problèmes récurrents**  
✅ **Aide à la prise de décision** (Ex : Identifier les aspects négatifs d’un produit/service)  

### 📊 **Cas d’usage potentiel en entreprise :**  
- Suivi de l’e-réputation d’une marque  
- Analyse des avis clients pour améliorer un service/produit  
- Optimisation du support client en détectant les points bloquants  

## 🚀 Comment l’essayer ?  
 

---

💡 **N’hésite pas à forker le repo et proposer des améliorations !** 🔥
