<template>
  <transition name="fade">
    <div v-if="visible" class="splash">
      <!-- Motif traditionnel malgache en arrière-plan -->
      <div class="background-pattern"></div>
      
      <!-- Éléments décoratifs animés -->
      <div class="ravinala ravinala-left"></div>
      <div class="ravinala ravinala-right"></div>
      
      <!-- Contenu principal -->
      <div class="content">
        <div class="logo-container">
          <img src="../assets/logo_mada.jpeg" alt="Logo E-Gouvernance" class="logo" />
          <div class="logo-ring"></div>
        </div>
        
        <h1 class="title">E-Gouvernance</h1>
        <p class="subtitle">Tonga soa • Bienvenue</p>
        
        <!-- Barre de chargement stylisée -->
        <div class="loading-bar">
          <div class="loading-progress"></div>
        </div>
      </div>
      
      <!-- Motif décoratif bas -->
      <div class="bottom-decoration">
        <div class="wave"></div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const visible = ref(true)

onMounted(() => {
  setTimeout(() => {
    visible.value = false
  }, 3000) // disparaît après 3s pour profiter des animations
})
</script>

<style scoped>
.splash {
  position: fixed;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #108b00 0%, #58c41e 50%, #6bff8b 100%);
  color: white;
  z-index: 9999;
  overflow: hidden;
}

/* Motif traditionnel malgache */
.background-pattern {
  position: absolute;
  inset: 0;
  background-image: 
    repeating-linear-gradient(45deg, transparent, transparent 35px, rgba(255,255,255,0.03) 35px, rgba(255,255,255,0.03) 70px),
    repeating-linear-gradient(-45deg, transparent, transparent 35px, rgba(255,255,255,0.03) 35px, rgba(255,255,255,0.03) 70px);
  opacity: 0.5;
}

/* Ravinala (arbre du voyageur) stylisé */
.ravinala {
  position: absolute;
  width: 200px;
  height: 300px;
  opacity: 0.15;
  animation: float 4s ease-in-out infinite;
}

.ravinala::before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  width: 8px;
  height: 100px;
  background: rgba(255,255,255,0.3);
  transform: translateX(-50%);
}

.ravinala::after {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  width: 180px;
  height: 180px;
  background: radial-gradient(ellipse at center, transparent 20%, rgba(255,255,255,0.2) 20%, rgba(255,255,255,0.2) 22%, transparent 22%),
              radial-gradient(ellipse at center, transparent 25%, rgba(255,255,255,0.2) 25%, rgba(255,255,255,0.2) 27%, transparent 27%),
              radial-gradient(ellipse at center, transparent 30%, rgba(255,255,255,0.2) 30%, rgba(255,255,255,0.2) 32%, transparent 32%);
  border-radius: 50% 50% 0 0;
  transform: translateX(-50%);
}

.ravinala-left {
  left: -50px;
  top: 20%;
  animation-delay: 0s;
}

.ravinala-right {
  right: -50px;
  top: 30%;
  animation-delay: 2s;
}

/* Contenu principal */
.content {
  position: relative;
  z-index: 10;
  text-align: center;
  animation: slideUp 0.8s ease-out;
}

/* Logo avec animation */
.logo-container {
  position: relative;
  margin-bottom: 2rem;
  animation: scaleIn 0.6s ease-out;
}

.logo {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  box-shadow: 0 8px 32px rgba(0,0,0,0.3);
  border: 4px solid rgba(255,255,255,0.9);
  position: relative;
  z-index: 2;
}

.logo-ring {
  position: absolute;
  inset: -10px;
  border: 3px solid rgba(255,255,255,0.4);
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
}

/* Titre */
.title {
  font-size: 2.5rem;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
  letter-spacing: 2px;
  animation: fadeInText 1s ease-out 0.3s both;
}

.subtitle {
  font-size: 1.2rem;
  font-weight: 300;
  margin: 0 0 2rem 0;
  opacity: 0.9;
  font-style: italic;
  animation: fadeInText 1s ease-out 0.5s both;
}

/* Barre de chargement */
.loading-bar {
  width: 200px;
  height: 4px;
  background: rgba(255,255,255,0.2);
  border-radius: 2px;
  overflow: hidden;
  margin: 0 auto;
}

.loading-progress {
  height: 100%;
  background: linear-gradient(90deg, #FFFFFF 0%, #FFD700 50%, #FFFFFF 100%);
  border-radius: 2px;
  animation: loading 2s ease-in-out infinite;
  box-shadow: 0 0 10px rgba(255,215,0,0.5);
}

/* Décoration bas */
.bottom-decoration {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 80px;
  overflow: hidden;
}

.wave {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 200%;
  height: 100%;
  background: linear-gradient(180deg, transparent, rgba(255,255,255,0.1));
  border-radius: 100% 100% 0 0;
  animation: wave 3s ease-in-out infinite;
}

/* Animations */
@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes scaleIn {
  from {
    opacity: 0;
    transform: scale(0.5) rotate(-10deg);
  }
  to {
    opacity: 1;
    transform: scale(1) rotate(0);
  }
}

@keyframes fadeInText {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1);
    opacity: 0.4;
  }
  50% {
    transform: scale(1.1);
    opacity: 0.8;
  }
}

@keyframes loading {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(100%);
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

@keyframes wave {
  0%, 100% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(-25%);
  }
}

/* Transition de sortie */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.8s ease;
}

.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
</style>