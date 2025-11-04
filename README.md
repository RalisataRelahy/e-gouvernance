# 🌐 Projet e-Gouvernance

> Une plateforme numérique destinée à moderniser la gestion publique et à renforcer la transparence entre l’État et les citoyens.

---

## 📖 À propos

**e-Gouvernance** est un projet web full-stack visant à digitaliser les services administratifs et à faciliter la communication entre les institutions publiques et les citoyens.  
Le projet a pour objectif de **rendre la gouvernance plus transparente, participative et accessible à tous**.

---

## 🚀 Fonctionnalités principales

- 🧭 Portail citoyen : consultation des informations publiques et des projets en cours  
- 📝 Gestion des demandes et formulaires administratifs en ligne  
- 💬 Espace de dialogue entre citoyens et institutions  
- 📊 Tableau de bord de gestion et de statistiques  
- 🔒 Authentification sécurisée et gestion des utilisateurs  
- 🌍 Interface responsive et moderne

---

## 🏗️ Architecture du projet

### **Frontend**
- Framework : [Vue.js 3](https://vuejs.org/)
- Outil de build : Vite
- Style : CSS3 / Tailwind / Vuetify (selon config)
- Pages principales :
  - `Home.vue`
  - `About.vue`
  - `Dashboard.vue`
  - `Contact.vue`

### **Backend**
- Framework : [Django REST Framework](https://www.django-rest-framework.org/)
- Base de données : MySQL
- API REST :
  - Authentification
  - Gestion des utilisateurs
  - Gestion des données publiques et des requêtes citoyennes

---

## ⚙️ Installation & Exécution

### 1️⃣ Cloner le dépôt

```bash
git clone https://github.com/RalisataRelahy/e-gouvernance.git
cd e-gouvernance

```

Pour lancer le frontend:
```bash
cd frontend
npm install
npm run dev
```

Et pour le backend:
```bash
cd gestionpop
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
python manage.py runserver
```
Structure du projet:
```bash
e-gouvernance/
│
├── backend/
│   ├── manage.py
│   ├── api/
│   └── settings.py
│
├── frontend/
│   ├── src/
│   │   ├── views/
│   │   ├── components/
│   │   └── assets/
│   ├── package.json
│   └── vite.config.js
│
├── Kolotrack/
    ├── src/
        ├── none
├── README.md
└── requirements.txt

