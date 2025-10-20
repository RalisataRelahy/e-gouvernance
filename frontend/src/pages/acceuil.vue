<template>
  <div class="home-container">
    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <div class="badge">
          <span class="badge-dot"></span>
          <span>Système National de Gestion de la Population</span>
        </div>
        
        <h1 class="hero-title">
          Bienvenue sur
          <span class="gradient-text">E-Gouvernance Madagascar</span>
        </h1>
        
        <p class="hero-description">
          La plateforme digitale moderne pour la gestion efficace et sécurisée 
          de l'ensemble de la population malgache. Accessible, transparent et innovant.
        </p>
        
        <div class="hero-buttons">
          <button class="btn btn-primary">Accéder au Système</button>
          <button class="btn btn-secondary">En savoir plus</button>
        </div>
      </div>
    </section>

    <!-- Statistiques -->
    <section class="stats-section">
      <div class="stats-grid">
        <div class="stat-card stat-red">
          <div class="stat-number">{{ nbrPersonne }}</div>
          <div class="stat-label">Citoyens enregistrés</div>
        </div>
        <div class="stat-card stat-green">
          <div class="stat-number">6</div>
          <div class="stat-label">Provinces couvertes</div>
        </div>
        <div class="stat-card stat-blue">
          <div class="stat-number">119</div>
          <div class="stat-label">Districts actifs</div>
        </div>
        <div class="stat-card stat-purple">
          <div class="stat-number">99.9%</div>
          <div class="stat-label">Disponibilité</div>
        </div>
      </div>
    </section>

    <!-- Fonctionnalités -->
    <section class="features-section">
      <div class="section-header">
        <h2 class="section-title">Fonctionnalités Principales</h2>
        <p class="section-description">
          Une solution complète pour moderniser la gestion administrative et faciliter 
          l'accès aux services publics à travers tout Madagascar
        </p>
      </div>

      <div class="features-grid">
        <div v-for="feature in features" :key="feature.id" class="feature-card">
          <router-link :to="'/'+feature.root " class="nav-link">
            <div class="feature-icon" v-html="feature.icon"></div>
            <h3 class="feature-title">{{ feature.title }}</h3>
            <p class="feature-description">{{ feature.description }}</p>
          </router-link>
          
        </div>
      </div>
    </section>

    <!-- Provinces -->
    <section class="provinces-section">
      <div class="section-header">
        <h2 class="section-title">Couverture Nationale</h2>
        <p class="section-description">
          Gestion unifiée des 6 provinces de Madagascar avec accès décentralisé
        </p>
      </div>

      <div class="provinces-grid">
        <div v-for="province in provinces" :key="province" class="province-card">
          <div class="province-content">
            
            <div>
              <h3 class="province-name">{{ province }}</h3>
              <p class="province-label">Province de {{ province }}</p>
            </div>
            <svg class="province-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <h2 class="cta-title">Prêt à moderniser la gestion de votre territoire ?</h2>
      <p class="cta-description">
        Rejoignez les administrations qui font confiance à E-Gouvernance Madagascar
      </p>
      <button class="btn btn-cta">Commencer maintenant</button>
    </section>
  </div>
</template>

<script setup>
import { ref ,computed, onMounted} from 'vue';

const data = ref([])

async function reloadInfo() {
  try {
    const res = await fetch('http://127.0.0.1:8000/api/citoyen/')
    data.value = await res.json()
  } catch (error) {
    console.error('Erreur lors du chargement des données:', error)
  }
}

// 👇 computed → se mettra à jour automatiquement quand data change
const nbrPersonne = computed(() => data.value.length)

// Charger les infos au démarrage
onMounted(() => {
  reloadInfo()
})

const features = ref([
  {
    id: 1,
    icon: '<svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"/></svg>',
    title: 'Gestion des Citoyens',
    description: 'Enregistrement et suivi complet de la population malgache',
    root:'list_citoyen'
  },
  {
    id: 2,
    icon: '<svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>',
    title: 'Organisation Territoriale',
    description: 'Gestion par province, région, district et quartier',
    root:''
  },
  {
    id: 3,
    icon: '<svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>',
    title: 'Documents Officiels',
    description: 'Délivrance et gestion des actes administratifs',
    root:''
  },
  {
    id: 4,
    icon: '<svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>',
    title: 'Statistiques en Temps Réel',
    description: 'Analyses démographiques et tableaux de bord',
    root:''
  },
  {
    id: 5,
    icon: '<svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>',
    title: 'Sécurité des Données',
    description: 'Protection avancée des informations personnelles',
    root:''
  },
  {
    id: 6,
    icon: '<svg class="icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>',
    title: 'Recherche Avancée',
    description: 'Accès rapide aux informations citoyennes',
    root:'add_citoyen'
  }
]);

const provinces = ref([
  'Antananarivo',
  'Fianarantsoa',
  'Toamasina',
  'Mahajanga',
  'Toliara',
  'Antsiranana'
]);
</script>

<style scoped>
.home-container {
  min-height: 100vh;
  background: linear-gradient(135deg, #fef2f2 0%, #ffffff 50%, #f0fdf4 100%);
}

/* Hero Section */
.hero-section {
  position: relative;
  padding: 5rem 2rem;
  overflow: hidden;
}
.nav-link {
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  color: white;
  text-decoration: none;
  font-weight: 600;
  font-size: 15px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  transition: all 0.3s ease;
  border: 2px solid transparent;
  backdrop-filter: blur(10px);
}
.hero-overlay {
  position: absolute;
  inset: 0;
  opacity: 0.05;
  pointer-events: none;
}

.hero-overlay::before {
  content: '';
  position: absolute;
  top: 5rem;
  left: 2.5rem;
  width: 16rem;
  height: 16rem;
  background: #dc2626;
  border-radius: 50%;
  filter: blur(80px);
}

.hero-overlay::after {
  content: '';
  position: absolute;
  bottom: 5rem;
  right: 2.5rem;
  width: 24rem;
  height: 24rem;
  background: #16a34a;
  border-radius: 50%;
  filter: blur(80px);
}

.hero-content {
  max-width: 70rem;
  margin: 0 auto;
  text-align: center;
  position: relative;
  z-index: 1;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: #fef2f2;
  color: #b91c1c;
  padding: 0.5rem 1rem;
  border-radius: 9999px;
  font-size: 0.875rem;
  font-weight: 500;
  margin-bottom: 1.5rem;
}

.badge-dot {
  width: 0.5rem;
  height: 0.5rem;
  background: #dc2626;
  border-radius: 50%;
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.hero-title {
  font-size: 3.75rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 1.5rem;
  line-height: 1.1;
}

.gradient-text {
  display: block;
  margin-top: 0.5rem;
  background: linear-gradient(to right, #dc2626, #16a34a);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-size: 1.25rem;
  color: #4b5563;
  margin-bottom: 2rem;
  max-width: 48rem;
  margin-left: auto;
  margin-right: auto;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 1rem 2rem;
  border-radius: 0.5rem;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
}

.btn-primary {
  background: linear-gradient(to right, #dc2626, #b91c1c);
  color: white;
  box-shadow: 0 10px 15px -3px rgba(220, 38, 38, 0.3);
}

.btn-primary:hover {
  transform: scale(1.05);
  box-shadow: 0 20px 25px -5px rgba(220, 38, 38, 0.4);
}

.btn-secondary {
  background: white;
  color: #374151;
  border: 2px solid #d1d5db;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}

.btn-secondary:hover {
  border-color: #dc2626;
  color: #dc2626;
}

/* Stats Section */
.stats-section {
  padding: 3rem 2rem;
  background: white;
}

.stats-grid {
  max-width: 70rem;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.stat-card {
  text-align: center;
  padding: 2rem 1.5rem;
  border-radius: 0.75rem;
}

.stat-red { background: linear-gradient(135deg, #fef2f2, #fee2e2); }
.stat-green { background: linear-gradient(135deg, #f0fdf4, #dcfce7); }
.stat-blue { background: linear-gradient(135deg, #eff6ff, #dbeafe); }
.stat-purple { background: linear-gradient(135deg, #faf5ff, #f3e8ff); }

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.stat-red .stat-number { color: #dc2626; }
.stat-green .stat-number { color: #16a34a; }
.stat-blue .stat-number { color: #2563eb; }
.stat-purple .stat-number { color: #9333ea; }

.stat-label {
  color: #6b7280;
  font-size: 0.875rem;
}

/* Sections communes */
.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 1rem;
}

.section-description {
  color: #6b7280;
  max-width: 42rem;
  margin: 0 auto;
  font-size: 1.125rem;
}

/* Features Section */
.features-section {
  padding: 5rem 2rem;
}

.features-grid {
  max-width: 70rem;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  border: 1px solid #f3f4f6;
  transition: all 0.3s;
}

.feature-card:hover {
  transform: translateY(-0.5rem);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.15);
}

.feature-icon {
  color: #dc2626;
  margin-bottom: 1rem;
}

.icon {
  width: 3rem;
  height: 3rem;
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 0.75rem;
}

.feature-description {
  color: #6b7280;
}

/* Provinces Section */
.provinces-section {
  padding: 5rem 2rem;
  background: linear-gradient(135deg, #f9fafb, #ffffff);
}

.provinces-grid {
  max-width: 70rem;
  margin: 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.province-card {
  background: white;
  padding: 1.5rem;
  border-radius: 0.75rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
  border-left: 4px solid #dc2626;
  transition: all 0.3s;
}

.province-card:hover {
  border-left-color: #16a34a;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.15);
}

.province-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.province-name {
  font-size: 1.125rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 0.25rem;
}

.province-label {
  font-size: 0.875rem;
  color: #6b7280;
}

.province-icon {
  width: 2rem;
  height: 2rem;
  color: #dc2626;
  transition: color 0.3s;
}

.province-card:hover .province-icon {
  color: #16a34a;
}

/* CTA Section */
.cta-section {
  padding: 5rem 2rem;
  background: linear-gradient(to right, #dc2626, #16a34a);
  text-align: center;
}

.cta-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: white;
  margin-bottom: 1.5rem;
}

.cta-description {
  font-size: 1.25rem;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 2rem;
}

.btn-cta {
  background: white;
  color: #dc2626;
  padding: 1rem 2.5rem;
  font-size: 1.125rem;
  font-weight: 700;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
}

.btn-cta:hover {
  background: #f9fafb;
}

/* Responsive */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .cta-title {
    font-size: 2rem;
  }
  
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
</style>