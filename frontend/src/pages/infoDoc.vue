<template>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <div class="infoDoc">
    <!-- Navigation -->
    <nav>
        <div class="container nav-container">
            <ul class="nav-links">
                <li><router-link to="/" class="active">Accueil</router-link></li>
                <div class="filter-buttons">
                    <li><button class="active" v-for="type in types":key="type" @click="setFilter(type)":class="{ active: activeFilter === type }"> {{ type === 'all' ? 'Tous' : type }}</button></li>
                </div>
            </ul>
            <div class="search-box">
                <i class="fas fa-search"></i>
                <input type="text" v-model="searchQuery" placeholder="Rechercher un document...">
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h2>Documents administratifs Malagasy</h2>
            <p>Trouvez toutes les informations nécessaires sur les documents administratifs à Madagascar : pièces requises, procédures, lieux de dépôt et délais de traitement.</p>
            <a href="#documents" class="btn">Explorer les documents-></a>
        </div>
    </section>
    <!-- Main Content -->
    <div class="container main-content">
        <!-- Documents Grid -->
        <div class="documents-section" id="documents">
            <h2 style="margin-bottom: 1.5rem; color: var(--primary);">Documents les plus demandés</h2>
            <div class="documents-grid">
                <!-- Carte d'identité -->
                <div 
                    v-for="doc in filteredDocuments" 
                    :key="doc.id"
                    class="document-card animate-card"
                    :class="`delay-${(doc.id - 1) % 6}`"
                    >
      <div class="card-header" :style="{ backgroundColor: doc.couleur }">
        <i :class="doc.icon"></i>
        <h3>{{ doc.nom }}</h3>
      </div>
      
      <div class="card-body">
        <div class="doc-info">
          <h3>{{ doc.description1 }}</h3>
          <p>{{ doc.description2 }}</p>
        </div>
        
        <div class="doc-details">
          <h4><i class="fas fa-folder-open"></i> 
            {{ doc.type === 'etat-civil' ? 'Procédure :' : 'Dossier requis :' }}
          </h4>
          <ul>
            <li v-for="(requis, index) in doc.docRequis" :key="index">
              <i class="fas fa-check-circle"></i> {{ requis }}
            </li>
          </ul>
          
          <h4><i class="fas fa-map-marker-alt"></i> Lieu de dépôt :</h4>
          <p>{{ doc.lieu_depot }}</p>
          
          <div v-if="doc.delai" class="delai-info">
            <h4><i class="fas fa-clock"></i> Délai estimé :</h4>
            <p>{{ doc.delai }}</p>
          </div>
        </div>
        
        <div class="doc-actions">
          <button @click="showDetails(doc)" class="btn-outline">
            <i class="fas fa-info-circle"></i> Plus d'infos
          </button>
          <button @click="downloadForm(doc)" class="btn-outline">
            <i class="fas fa-download"></i> Formulaire
          </button>
        </div>
      </div>
    </div>
            </div>
        </div>
        <!-- Sidebar -->
        <aside class="sidebar">
            <h3><i class="fas fa-link"></i> Accès rapide</h3>
            <ul class="quick-links">
                <li><a href="#"><i class="fas fa-file-pdf"></i> Télécharger tous les formulaires</a></li>
                <li><a href="#"><i class="fas fa-map-marked-alt"></i> Localiser les administrations</a></li>
                <li><a href="#"><i class="fas fa-question-circle"></i> Foire aux questions</a></li>
                <li><a href="#"><i class="fas fa-calendar-alt"></i> Calculateur de délais</a></li>
                <li><a href="#"><i class="fas fa-euro-sign"></i> Tarifs et frais</a></li>
            </ul>

            <div class="info-box">
                <h4><i class="fas fa-lightbulb"></i> Conseil pratique</h4>
                <p>Préparez toujours des photocopies de tous vos documents. Les administrations gardent souvent les copies et vérifient les originaux.</p>
            </div>

            <div class="info-box">
                <h4><i class="fas fa-clock"></i> Délais de traitement</h4>
                <p>Les délais peuvent varier selon l'administration. Prévoyez toujours un délai supplémentaire pour vos démarches.</p>
            </div>

            <div class="info-box">
                <h4><i class="fas fa-exclamation-triangle"></i> Attention</h4>
                <p>Vérifiez la validité de vos documents. Les actes de naissance et justificatifs de domicile ont généralement une durée de validité de 3 mois.</p>
            </div>
        </aside>
    </div>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-column">
                    <h3>Documents Administratifs Madagascar</h3>
                    <p>Votre guide complet pour toutes les démarches administratives à Madagascar.</p>
                    <div style="margin-top: 1rem;">
                        <a href="#" class="btn" style="margin-right: 10px;"><i class="fas fa-envelope"></i> Contact</a>
                        <a href="#" class="btn-outline" style="color: white; border-color: white;"><i class="fas fa-info-circle"></i> À propos</a>
                    </div>
                </div>
                <div class="footer-column">
                    <h3>Liens utiles</h3>
                    <ul class="footer-links">
                        <li><a href="https://www.presidence.gov.mg/" target="_blank">Site officiel du gouvernement</a></li>
                        <li><a href="https://www.madaclic.com/" target="_blank">Madaclick - Guichet unique</a></li>
                        <li><a href="https://www.impots.mg/accueil" target="_blank">Direction Générale des Impôts</a></li>
                        <li><a href="https://www.pn.gov.mg/passport/" target="_blank">Office Malagasy des Passeports</a></li>
                        <li><a href="https://observatoire-territoire.mg/" target="_blank">Service des Domaines</a></li>
                    </ul>
                </div>
                <div class="footer-column">
                    <h3>Catégories de documents</h3>
                    <ul class="footer-links">
                        
                        <li><a href="#">Documents fiscaux</a></li>
                        <li><a href="#">Documents fonciers</a></li>
                        <li><a href="#">Documents commerciaux</a></li>
                        <li><a href="#">Documents de voyage</a></li>
                    </ul>
                </div>
                
            </div>
            <div class="copyright">
                <p>&copy; 2023 Documents Administratifs Madagascar. Tous droits réservés.</p>
            </div>
        </div>
    </footer>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
const activeFilter = ref('all')
const searchQuery = ref('')
const documents = ref([
  {
    id: 1,
    nom: "Carte Nationale d'Identité (CNI)",
    icon: "fas fa-id-card",
    description1: "Document d'identification principal",
    description2: "La Carte Nationale d'Identité est le document d'identité officiel pour tout citoyen malgache majeur.",
    docRequis: [
      "Acte de naissance (original récent)",
      "Justificatif de domicile",
      "Ancienne CNI (si renouvellement)",
      "2 photos d'identité",
      "Timbre fiscal"
    ],
    lieu_depot: "Commune de résidence (Bureau d'État Civil)",
    couleur: "#00843d",
    type: "identite"
  },
{ id: 2, 
    nom: "Passeport", 
    icon: "fas fa-passport", 
    description1: "Document de voyage international", 
    description2: "Le passeport malgache est nécessaire pour voyager à l'étranger.", 
    docRequis: [ "CNI originale et valide", "Acte de naissance (original récent)", "Justificatif de domicile", "2 photos d'identité biométriques", "Ancien passeport (si renouvellement)" ], 
    lieu_depot: "Office Malagasy des Passeports (OMP)", 
    couleur: "#ff671f", type: "voyage" 
}, 
{ id: 3, 
    nom: "Numéro d'Identification Fiscale (NIF)", 
    icon: "fas fa-file-invoice-dollar", 
    description1: "Identifiant fiscal unique", 
    description2: "Le NIF est obligatoire pour toute personne physique ou morale exerçant une activité économique.", 
    docRequis: [ "Formulaire de demande NIF", "Copie de la CNI", "Justificatif de domicile", "Timbre fiscal" ], 
    lieu_depot: "Centre des Services des Impôts (CSI)", 
    couleur: "#00843d", 
    type: "fiscal" 
}, 
{
    id:6,
    nom:"Duplicata CIN",
    icon:"fas fa-person",
    description1: "Document de duplicata", 
    description2: "Duplicata:En cas de perte de l'original CIN.", 
    docRequis: [ "1-Declaration de perte", "4-Photo d'identite", "CIN photocopie ou infos a propos du CIN", "4-photos d'identité biométriques" ,], 
    lieu_depot: "Commissariat Centrale", 
    couleur: "#ff671f", 
    type: "identite" 
},
{
    id:6,
    nom:"Declaration de Perte d'un Document",
    icon:"fas fa-none",
    description1: "Document de declaration de perte d'un document", 
    description2: "En cas de perte d'un document administratif.", 
    docRequis: [ "1-Certificat de residence", "2-Photo d'identite", , "4000Ar"], 
    lieu_depot: "Commissariat de Police", 
    couleur: "#ff671f",
    type: "identite" 
},
{ id: 4, 
    nom: "Titre Foncier", 
    icon: "fas fa-home", 
    description1: "Preuve de propriété immobilière", 
    description2: "Le titre foncier est le seul document qui prouve une propriété immobilière incontestable à Madagascar.",
    docRequis: [ "Requête en inscription", "Certificat de propriété ou ancien titre", "Plan de bornage", "Acte de vente", "Certificat de non-révendication" ], lieu_depot: "Conservation Foncière (Service des Domaines)",
     couleur: "#00843d", 
     type: "foncier", 
     delai: "Plusieurs mois"
}, { 
    id: 5,
     nom: "Acte de Naissance",
      icon: "fas fa-birthday-cake", 
      description1: "Document d'état civil fondamental", description2: "L'acte de naissance est requis pour la plupart des démarches administratives.", docRequis: [ "Se rendre à la mairie du lieu de naissance", "Fournir les noms et date de naissance", "Présenter une pièce d'identité" ], lieu_depot: "Mairie du lieu de naissance", couleur: "#ff671f", type: "etat-civil", delai: "Immédiat" }, { id: 6, nom: "Permis de Conduire", icon: "fas fa-id-card-alt", description1: "Autorisation de conduire", description2: "Document obligatoire pour conduire un véhicule à moteur sur le territoire malgache.", docRequis: [ "Formulaire de demande", "Copie de la CNI", "Copie de l'acte de naissance", "Certificat médical", "Photos d'identité", "Timbre fiscal" ], lieu_depot: "Centre de formation agréé ou service des permis", couleur: "#00843d", type: "transport", delai: "2 à 4 semaines" }
  // ... tes autres documents
])
const types = ['all', 'identite', 'voyage', 'fiscal', 'foncier', 'etat-civil', 'transport']
// Documents filtrés dynamiquement selon recherche ET type
const filteredDocuments = computed(() => {
  let filtered = documents.value

  // Filtrer par type
  if (activeFilter.value !== 'all') {
    filtered = filtered.filter(doc => doc.type === activeFilter.value)
  }

  // Filtrer par recherche
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(doc =>
      doc.nom.toLowerCase().includes(query) ||
      (doc.type && doc.type.toLowerCase().includes(query))
    )
  }

  return filtered
});
function setFilter(type) {
  activeFilter.value = type
}
</script>


<style scoped>
    :root {
        --primary: #00843d;
        --primary-light: #e6f4ea;
        --secondary: #ff671f;
        --dark: #333;
        --light: #f8f9fa;
        --gray: #6c757d;
        --border-radius: 8px;
        --shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        --transition: all 0.3s ease;
    }

    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    html{
        scroll-behavior: smooth;
    }
    /* Style moderne de la barre de défilement */
    ::-webkit-scrollbar {
    width: 3px;
    }

    ::-webkit-scrollbar-track {
    background: #f1f1f1;
    border-radius: 10px;
    }

    ::-webkit-scrollbar-thumb {
    background: var(--primary);
    border-radius: 10px;
    transition: background 0.3s ease;
    }

    ::-webkit-scrollbar-thumb:hover {
    background: #006b32;
    }

    /* Pour Firefox */
    * {
    scrollbar-width: thin;
    scrollbar-color: var(--primary) #f1f1f1;
    }
    body {
        background-color: #f5f7fa;
        color: var(--dark);
        line-height: 1.6;
    }

    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }

    /* Header Styles */
    header {
        background: linear-gradient(135deg, var(--primary), #006b32);
        color: white;
        padding: 2rem 0;
        box-shadow: var(--shadow);
    }

    .header-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .logo {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    .logo i {
        font-size: 2.5rem;
    }

    .logo h1 {
        font-size: 1.8rem;
        font-weight: 700;
    }

    .tagline {
        font-size: 1rem;
        opacity: 0.9;
        margin-top: 5px;
    }

    /* Navigation */
    nav {
        background-color: white;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        position: sticky;
        top: 0;
        z-index: 100;
    }

    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 0;
    }

    .nav-links {
        display: flex;
        list-style: none;
        gap: 2rem;
    }

    .nav-links a {
        text-decoration: none;
        color: var(--dark);
        font-weight: 500;
        padding: 0.5rem 1rem;
        border-radius: var(--border-radius);
        transition: var(--transition);
    }

    .nav-links a:hover, .nav-links a.active {
        background-color: var(--primary-light);
        color: var(--primary);
    }

    .search-box {
        display: flex;
        align-items: center;
        background: var(--light);
        border-radius: 50px;
        padding: 0.5rem 1rem;
        width: 300px;
    }

    .search-box input {
        border: none;
        background: transparent;
        padding: 0.5rem;
        width: 100%;
        outline: none;
    }

    /* Hero Section */
    .hero {
        background: linear-gradient(rgba(0, 132, 62, 0.67), rgba(0, 107, 50, 0.9)), url('https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Flag_of_Madagascar.svg/1280px-Flag_of_Madagascar.svg.png');
        background-size: cover;
        background-position: center;
        color: white;
        padding: 4rem 0;
        text-align: center;
        margin-bottom: 2rem;
        border-radius: 0 0 var(--border-radius) var(--border-radius);
    }

    .hero h2 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .hero p {
        font-size: 1.2rem;
        max-width: 700px;
        margin: 0 auto 2rem;
    }
.filter-buttons {
  margin-bottom: 1.5rem;
}

.filter-buttons button {
  margin-right: 0.5rem;
  padding: 0.5rem 1rem;
  border: 1px solid #00843d;
  border-radius: 5px;
  background: transparent;
  cursor: pointer;
  transition: 0.3s;
}

.filter-buttons button.active,
.filter-buttons button:hover {
  background-color: #00843d;
  color: white;
}
    .btn {
        display: inline-block;
        background-color: var(--secondary);
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        transition: var(--transition);
        border: none;
        cursor: pointer;
    }

    .btn:hover {
        background-color: #e55c1a;
        transform: translateY(-3px);
        box-shadow: 0 5px 15px rgba(255, 103, 31, 0.3);
    }

    /* Main Content */
    .main-content {
        display: grid;
        grid-template-columns: 1fr 300px;
        gap: 2rem;
        margin: 2rem 0;
    }

    .documents-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1.5rem;
    }

    .document-card {
        background: white;
        border-radius: var(--border-radius);
        overflow: hidden;
        box-shadow: var(--shadow);
        transition: var(--transition);
    }

    .document-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
    }

    .card-header {
        background-color: var(--primary);
        color: white;
        padding: 1.2rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .card-header i {
        font-size: 1.5rem;
    }

    .card-body {
        padding: 1.5rem;
    }

    .doc-info {
        margin-bottom: 1.2rem;
    }

    .doc-info h3 {
        color: var(--primary);
        margin-bottom: 0.5rem;
        font-size: 1.2rem;
    }

    .doc-info p {
        color: var(--gray);
        font-size: 0.95rem;
    }

    .doc-details {
        border-top: 1px solid #eee;
        padding-top: 1rem;
    }

    .doc-details h4 {
        margin-bottom: 0.8rem;
        color: var(--dark);
        font-size: 1rem;
    }

    .doc-details ul {
        list-style-type: none;
        margin-bottom: 1.2rem;
    }

    .doc-details li {
        padding: 0.3rem 0;
        display: flex;
        align-items: flex-start;
        gap: 8px;
    }

    .doc-details li i {
        color: var(--primary);
        margin-top: 4px;
        font-size: 0.8rem;
    }

    .doc-actions {
        display: flex;
        justify-content: space-between;
        margin-top: 1rem;
    }

    .btn-outline {
        background: transparent;
        border: 1px solid var(--primary);
        color: var(--primary);
        padding: 0.5rem 1rem;
        border-radius: var(--border-radius);
        text-decoration: none;
        font-size: 0.9rem;
        transition: var(--transition);
    }

    .btn-outline:hover {
        background: var(--primary-light);
    }

    /* Sidebar */
    .sidebar {
        background: white;
        border-radius: var(--border-radius);
        padding: 1.5rem;
        box-shadow: var(--shadow);
        height: fit-content;
        position: sticky;
        top: 100px;
    }

    .sidebar h3 {
        color: var(--primary);
        margin-bottom: 1.2rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid var(--primary-light);
    }

    .quick-links {
        list-style: none;
        margin-bottom: 2rem;
    }

    .quick-links li {
        margin-bottom: 0.8rem;
    }

    .quick-links a {
        text-decoration: none;
        color: var(--dark);
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 0.5rem;
        border-radius: var(--border-radius);
        transition: var(--transition);
    }

    .quick-links a:hover {
        background: var(--primary-light);
        color: var(--primary);
    }

    .info-box {
        background: var(--primary-light);
        padding: 1.2rem;
        border-radius: var(--border-radius);
        margin-top: 1.5rem;
    }

    .info-box h4 {
        color: var(--primary);
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Footer */
    footer {
        padding: 5rem 2rem;
        background: linear-gradient(to right, #dc2626, #16a34a);
        text-align: center;
        padding: 3rem 0 1.5rem;
        margin-top: 3rem;
    }

    .footer-content {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        margin-bottom: 2rem;
    }

    .footer-column h3 {
        color: var(--secondary);
        margin-bottom: 1.2rem;
        font-size: 1.2rem;
    }

    .footer-links {
        list-style: none;
    }

    .footer-links li {
        margin-bottom: 0.8rem;
    }

    .footer-links a {
        color: #ccc;
        text-decoration: none;
        transition: var(--transition);
    }

    .footer-links a:hover {
        color: white;
        padding-left: 5px;
    }

    .copyright {
        text-align: center;
        padding-top: 1.5rem;
        border-top: 1px solid #444;
        color: #aaa;
        font-size: 0.9rem;
    }

    /* Responsive Design */
    @media (max-width: 992px) {
        .main-content {
            grid-template-columns: 1fr;
        }
        
        .sidebar {
            position: static;
        }
    }

    @media (max-width: 768px) {
        .header-content {
            flex-direction: column;
            text-align: center;
            gap: 1rem;
        }
        
        .nav-container {
            flex-direction: column;
            gap: 1rem;
        }
        
        .nav-links {
            flex-wrap: wrap;
            justify-content: center;
        }
        
        .search-box {
            width: 100%;
            max-width: 400px;
        }
        
        .hero h2 {
            font-size: 2rem;
        }
        
        .documents-grid {
            grid-template-columns: 1fr;
        }
    }
</style>