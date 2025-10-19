<template>
  <header class="header">
    <div class="header-content">
      <div class="logo-section">
        <img src="../assets/logo_mada.jpeg" alt="Logo Madagascar" class="logo">
        <div class="title-section">
          <h1>E-GOUVERNANCE</h1>
          <p class="subtitle">Repoblikan'i Madagasikara</p>
        </div>
      </div>
      
      <nav class="navigation">
        <router-link to="/" class="nav-link">
          Accueil
        </router-link>
        <router-link to="/add_citoyen" class="nav-link">
          Ajouter un citoyen
        </router-link>
        <router-link to="/list_citoyen" class="nav-link">
          Liste des citoyens
        </router-link>
      </nav>
    </div>
    
    <!-- Bande aux couleurs du drapeau -->
    <div class="flag-stripe">
      <div class="stripe white"></div>
      <div class="stripe red"></div>
      <div class="stripe green"></div>
    </div>
  </header>
</template>

<script setup>
</script>

<style scoped>
.header {
  position: relative;
  background: linear-gradient(135deg, #1a5f3f 0%, #2d8659 100%);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  overflow: hidden;
}

.header::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: 
    radial-gradient(circle at 20% 50%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 50%, rgba(255, 255, 255, 0.05) 0%, transparent 50%);
  pointer-events: none;
}

.header-content {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  max-width: 1400px;
  margin: 0 auto;
  z-index: 1;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 20px;
}

.logo {
  width: 80px;
  height: 80px;
  object-fit: contain;
  border: 3px solid white;
  border-radius: 50%;
  background: white;
  padding: 5px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.title-section {
  display: flex;
  flex-direction: column;
}

h1 {
  margin: 0;
  font-size: 28px;
  font-weight: 700;
  color: white;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
  letter-spacing: 1px;
}

.subtitle {
  margin: 4px 0 0 0;
  font-size: 13px;
  color: rgba(255, 255, 255, 0.95);
  font-style: italic;
  letter-spacing: 0.5px;
}

.navigation {
  display: flex;
  gap: 8px;
  align-items: center;
}

.nav-link {
  display: flex;
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


.nav-link:hover {
  background: rgba(255, 255, 255, 0.25);
  border-color: rgba(255, 255, 255, 0.4);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.nav-link:hover .nav-icon {
  transform: scale(1.2);
}

.nav-link.router-link-active {
  background: white;
  color: #1a5f3f;
  border-color: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

/* Bande drapeau Madagascar */
.flag-stripe {
  border-top: 5px solid white ;
  display: flex;
  height: 20px;
  width: 100%;
}

.stripe {
  flex: 1;
}

.stripe.white {
  background: white;
}

.stripe.red {
  background: #FC3D32;
}

.stripe.green {
  background: #007E3A;
}

/* Responsive */
@media (max-width: 1024px) {
  .header-content {
    flex-direction: column;
    gap: 20px;
    padding: 20px 30px;
  }
  
  .navigation {
    width: 100%;
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .nav-link {
    font-size: 14px;
    padding: 10px 16px;
  }
}

@media (max-width: 640px) {
  .logo {
    width: 60px;
    height: 60px;
  }
  
  h1 {
    font-size: 20px;
  }
  
  .subtitle {
    font-size: 11px;
  }
  
  .nav-link {
    padding: 8px 12px;
    font-size: 13px;
  }
  
  .nav-icon {
    font-size: 16px;
  }
}
</style>