<script setup>
import { defineProps, ref, onMounted } from 'vue'

const props = defineProps({
  id: {
    type: String,
    required: true
  }
})

const user = ref(null)
const message = ref('')

async function loadUser() {
  try {
    const res = await fetch(`http://127.0.0.1:8000/api/citoyen/${props.id}/`)
    if (res.ok) {
      user.value = await res.json()
    } else {
      message.value = 'Citoyen non trouvé ❌'
    }
  } catch (error) {
    message.value = 'Erreur de connexion au serveur'
    console.error('Erreur:', error)
  }
}

onMounted(() => {
  loadUser()
})
</script>

<template>
  <div v-if="user" class="infoUser">
    <h2>Informations du Citoyen</h2>
    
    <!-- INFORMATIONS PERSONNELLES -->
    <div class="info-section">
      <h3>Informations Personnelles</h3>
      <p><strong>Nom complet :</strong> {{ user.nom_complet || `${user.nom} ${user.prenoms}` }}</p>
      <p><strong>Nom :</strong> {{ user.nom }}</p>
      <p><strong>Prénoms :</strong> {{ user.prenoms }}</p>
      <p><strong>Sexe :</strong> {{ user.get_sexe_display || (user.sexe === 'M' ? 'Masculin' : user.sexe === 'F' ? 'Féminin' : 'Autre') }}</p>
      <p><strong>Date de naissance :</strong> {{ user.date_naissance }}</p>
      <p><strong>Âge :</strong> {{ user.age }} ans</p>
      <p><strong>Lieu de naissance :</strong> {{ user.lieu_naissance }}</p>
      <p><strong>Nationalité :</strong> {{ user.nationalite }}</p>
      <p><strong>Situation familiale :</strong> {{ user.get_situation_familiale_display || 
        (user.situation_familiale === 'C' ? 'Célibataire' : 
         user.situation_familiale === 'M' ? 'Marié(e)' : 
         user.situation_familiale === 'D' ? 'Divorcé(e)' : 
         user.situation_familiale === 'V' ? 'Veuf/Veuve' : 
         user.situation_familiale === 'U' ? 'Union libre' : 'Non spécifié') }}</p>
    </div>

    <!-- DOCUMENTS D'IDENTITÉ -->
    <div class="info-section">
      <h3>Documents d'Identité</h3>
      <p><strong>Numéro CIN :</strong> {{ user.numero_cin }}</p>
      <p v-if="user.numero_passeport"><strong>Numéro passeport :</strong> {{ user.numero_passeport }}</p>
      <p v-if="user.numero_securite_sociale"><strong>Numéro sécurité sociale :</strong> {{ user.numero_securite_sociale }}</p>
      <p v-if="user.numero_contribuable"><strong>Numéro contribuable :</strong> {{ user.numero_contribuable }}</p>
    </div>

    <!-- INFORMATIONS DE RÉSIDENCE -->
    <div class="info-section">
      <h3>Adresse</h3>
      <p><strong>Adresse :</strong> {{ user.adresse }}</p>
      <p><strong>Province :</strong> {{ user.province }}</p>
      <p v-if="user.region"><strong>Région :</strong> {{ user.region }}</p>
      <p><strong>Commune :</strong> {{ user.commune }}</p>
      <p><strong>Quartier :</strong> {{ user.quartier }}</p>
      <p v-if="user.code_postal"><strong>Code postal :</strong> {{ user.code_postal }}</p>
      <p><strong>Téléphone :</strong> {{ user.telephone }}</p>
      <p v-if="user.email"><strong>Email :</strong> {{ user.email }}</p>
    </div>

    <!-- INFORMATIONS PROFESSIONNELLES -->
    <div v-if="user.profession || user.employeur" class="info-section">
      <h3>Informations Professionnelles</h3>
      <p v-if="user.profession"><strong>Profession :</strong> {{ user.profession }}</p>
      <p v-if="user.employeur"><strong>Employeur :</strong> {{ user.employeur }}</p>
      <p v-if="user.situation_professionnelle"><strong>Situation professionnelle :</strong> 
        {{ user.get_situation_professionnelle_display || 
          (user.situation_professionnelle === 'A' ? 'Actif' : 
           user.situation_professionnelle === 'C' ? 'Chômeur' : 
           user.situation_professionnelle === 'E' ? 'Étudiant' : 
           user.situation_professionnelle === 'R' ? 'Retraité' : 
           user.situation_professionnelle === 'I' ? 'Indépendant' : 
           user.situation_professionnelle === 'F' ? 'Fonctionnaire' : 'Non spécifié') }}
      </p>
      <p v-if="user.revenu_annuel"><strong>Revenu annuel :</strong> {{ user.revenu_annuel }} Ar</p>
    </div>

    <!-- INFORMATIONS ÉDUCATIVES -->
    <div v-if="user.niveau_education || user.diplome" class="info-section">
      <h3>Éducation</h3>
      <p v-if="user.niveau_education"><strong>Niveau d'éducation :</strong> 
        {{ user.get_niveau_education_display || 
          (user.niveau_education === 'P' ? 'Primaire' : 
           user.niveau_education === 'S' ? 'Secondaire' : 
           user.niveau_education === 'B' ? 'Baccalauréat' : 
           user.niveau_education === 'U' ? 'Universitaire' : 
           user.niveau_education === 'M' ? 'Master' : 
           user.niveau_education === 'D' ? 'Doctorat' : 'Non spécifié') }}
      </p>
      <p v-if="user.diplome"><strong>Diplôme :</strong> {{ user.diplome }}</p>
      <p v-if="user.etablissement"><strong>Établissement :</strong> {{ user.etablissement }}</p>
    </div>

    <!-- INFORMATIONS SANITAIRES -->
    <div v-if="user.groupe_sanguin || user.allergies" class="info-section">
      <h3>Informations Sanitaires</h3>
      <p v-if="user.groupe_sanguin"><strong>Groupe sanguin :</strong> {{ user.groupe_sanguin }}</p>
      <p v-if="user.allergies"><strong>Allergies :</strong> {{ user.allergies }}</p>
      <p><strong>Couverture médicale :</strong> {{ user.couverture_medicale ? 'Oui' : 'Non' }}</p>
      <p v-if="user.nom_medecin_traitant"><strong>Médecin traitant :</strong> {{ user.nom_medecin_traitant }}</p>
    </div>

    <!-- INFORMATIONS CIVIQUES -->
    <div v-if="user.bureau_vote || user.situation_militaire" class="info-section">
      <h3>Informations Civiques</h3>
      <p v-if="user.bureau_vote"><strong>Bureau de vote :</strong> {{ user.bureau_vote }}</p>
      <p v-if="user.circonscription_electorale"><strong>Circonscription électorale :</strong> {{ user.circonscription_electorale }}</p>
      <p v-if="user.situation_militaire"><strong>Situation militaire :</strong> {{ user.situation_militaire }}</p>
    </div>

    <!-- INFORMATIONS DES PARENTS -->
    <div v-if="user.nom_pere || user.nom_mere" class="info-section">
      <h3>Informations des Parents</h3>
      <p v-if="user.nom_pere"><strong>Nom du père :</strong> {{ user.nom_pere }}</p>
      <p v-if="user.nom_mere"><strong>Nom de la mère :</strong> {{ user.nom_mere }}</p>
      <p v-if="user.profession_pere"><strong>Profession du père :</strong> {{ user.profession_pere }}</p>
      <p v-if="user.profession_mere"><strong>Profession de la mère :</strong> {{ user.profession_mere }}</p>
    </div>

    <!-- MÉTADONNÉES -->
    <div class="info-section">
      <h3>Informations Techniques</h3>
      <p><strong>Date d'enregistrement :</strong> {{ user.date_enregistrement }}</p>
      <p v-if="user.date_modification"><strong>Dernière modification :</strong> {{ user.date_modification }}</p>
      <p><strong>Statut :</strong> {{ user.est_actif ? 'Actif' : 'Inactif' }}</p>
    </div>
  </div>

  <div v-else class="loading">
    <p>{{ message || 'Chargement des informations...' }}</p>
  </div>
</template>

<style scoped>
.infoUser {
  max-width: 800px;
  margin: 20px auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.info-section {
  background: white;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 8px;
  border-left: 4px solid #4f46e5;
}

.info-section h3 {
  color: #4f46e5;
  margin-bottom: 15px;
  border-bottom: 2px solid #e5e7eb;
  padding-bottom: 8px;
}

.info-section p {
  margin: 8px 0;
  line-height: 1.5;
}

.info-section strong {
  color: #374151;
  min-width: 200px;
  display: inline-block;
}

.loading {
  text-align: center;
  padding: 40px;
  color: #6b7280;
  font-size: 18px;
}

h2 {
  color: #1f2937;
  text-align: center;
  margin-bottom: 30px;
  border-bottom: 3px solid #4f46e5;
  padding-bottom: 10px;
}

/* Responsive */
@media (max-width: 768px) {
  .infoUser {
    margin: 10px;
    padding: 15px;
  }
  
  .info-section {
    padding: 15px;
  }
  
  .info-section strong {
    min-width: 150px;
    display: block;
    margin-bottom: 5px;
  }
}
</style>