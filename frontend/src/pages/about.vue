<template>
  <div class="about-container">
    <section class="header">
      <h1>À propos du projet e-Gouvernance</h1>
      <p>Une initiative numérique pour une administration plus proche, plus transparente et plus efficace.</p>
    </section>

    <section class="mission">
      <h2>Notre mission</h2>
      <p>
        Le projet e-Gouvernance a pour ambition de moderniser la gestion publique à travers la transformation
        digitale. Nous mettons la technologie au service de l’État et des citoyens pour simplifier les démarches,
        améliorer la transparence et renforcer la participation citoyenne.
      </p>
    </section>

    <section class="vision">
      <h2>Notre vision</h2>
      <p>
        Bâtir un écosystème numérique où chaque citoyen peut interagir facilement avec les services publics,
        accéder à l’information en temps réel et participer activement aux décisions qui façonnent sa communauté.
      </p>
    </section>

    <section class="values">
      <h2>Nos valeurs</h2>
      <ul>
        <li><strong>Transparence :</strong> garantir une visibilité claire des actions publiques.</li>
        <li><strong>Accessibilité :</strong> rendre les services administratifs disponibles à tous, sans barrière géographique.</li>
        <li><strong>Innovation :</strong> adopter des solutions modernes pour répondre aux défis d’aujourd’hui.</li>
        <li><strong>Participation :</strong> encourager l’implication citoyenne dans la gouvernance locale et nationale.</li>
      </ul>
    </section>

    <section class="team">
      <h2>Notre équipe</h2>
      <p>
        Ce projet est porté par une équipe de jeunes développeurs, analystes et innovateurs
        engagés pour une administration plus efficace et connectée au citoyen.
      </p>
      <div class="team-grid">
        <div class="member" v-for="member in team" :key="member.name">
            
          <img src="../assets/nekena.png" alt="Photo de {{ member.name }}" />
          <h3>{{ member.name }}</h3>
          <p>{{ member.role }}</p>
        </div>
      </div>
    </section>

    <footer>
      <p>&copy; 2025 e-Gouvernance — Tous droits réservés.</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'About',
  data() {
    return {
      team: [
        { name: 'Nekena', role: 'Développeur principal', photo: "../assets/nekena.png" },
    ]
    };
  },
};
</script>

<style scoped>
.about-container {
  max-width: 1000px;
  margin: 40px auto;
  padding: 0 20px;
  font-family: "Poppins", sans-serif;
  line-height: 1.7;
  color: #333;
}

.header {
  text-align: center;
  margin-bottom: 40px;
}

.header h1 {
  color: #005c97;
  font-size: 2.4em;
  margin-bottom: 10px;
}

.mission, .vision, .values, .team {
  margin-bottom: 40px;
}

.values ul {
  list-style: none;
  padding: 0;
}

.values li {
  margin-bottom: 10px;
}

.team-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.member {
  text-align: center;
  width: 200px;
}

.member img {
  width: 100%;
  border-radius: 50%;
  border: 3px solid #005c97;
}

footer {
  text-align: center;
  margin-top: 50px;
  color: #777;
  font-size: 0.9em;
}
</style>
