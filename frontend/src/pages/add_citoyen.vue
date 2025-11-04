<template>
  <div class="form-container">
    <h1>Enregistrement d'un Citoyen</h1>
    <p v-if="message" :class="{'success': success, 'error': !success}">{{ message }}</p>

    <form @submit.prevent="submitForm">
      <!-- INFORMATIONS PERSONNELLES -->
      <fieldset>
        <legend>Informations Personnelles</legend>
        <div class="form-row">
          <input v-model="formData.nom" placeholder="Nom*" required />
          <input v-model="formData.prenoms" placeholder="Prénoms*" required />
        </div>
        <div class="form-row">
          <select v-model="formData.sexe" required>
            <option value="">Sexe*</option>
            <option value="M">Masculin</option>
            <option value="F">Féminin</option>
            <option value="A">Autre</option>
          </select>
          <input v-model="formData.date_naissance" type="date" placeholder="Date de naissance*" required />
        </div>
        <div class="form-row">
          <input v-model="formData.lieu_naissance" placeholder="Lieu de naissance*" required />
          <input v-model="formData.nationalite" placeholder="Nationalité*" required value="Malagasy" />
        </div>
        <select v-model="formData.situation_familiale" class="full-width">
          <option value="">Situation familiale</option>
          <option value="C">Célibataire</option>
          <option value="M">Marié(e)</option>
          <option value="D">Divorcé(e)</option>
          <option value="V">Veuf/Veuve</option>
          <option value="U">Union libre</option>
        </select>
      </fieldset>

      <!-- DOCUMENTS D'IDENTITÉ -->
      <fieldset v-if="formData.age>18">
        <legend>Documents d'Identité</legend>
        <input v-model="formData.numero_cin" placeholder="Numéro CIN*" required maxlength="14"/>
        <input v-model="formData.numero_passeport" placeholder="Numéro de passeport" required maxlength="14"/>
        <input v-model="formData.numero_securite_sociale" placeholder="Numéro sécurité sociale" required maxlength="14"/>
        <input v-model="formData.numero_contribuable" placeholder="Numéro contribuable" required maxlength="14"/>
      </fieldset>
      <!-- SECTION PHOTO ET BIOMÉTRIE -->
      <fieldset>
        <legend>Photo et Données Biométriques</legend>
        
        <!-- Upload de photo -->
        <div class="photo-upload">
          <label class="upload-label">
            <input 
              type="file" 
              @change="handlePhotoUpload" 
              accept="image/*" 
              class="file-input"
            />
            <div class="upload-area">
              <span v-if="!formData.photo">📷 Choisir une photo</span>
              <div v-else class="photo-preview">
                <img :src="photoPreviewUrl" alt="Preview" class="preview-image" />
                <button type="button" @click="removePhoto" class="remove-btn">✕</button>
              </div>
            </div>
          </label>
          <p class="help-text">Format: JPG, PNG • Max: 2MB • Taille recommandée: 300x400px</p>
        </div>

        <!-- Données biométriques optionnelles -->
        <div class="biometric-section">
          <h4>Données Biométriques (Optionnel)</h4>
          
          <!-- Empreintes digitales -->
          <div class="fingerprint-upload">
            <label>
              <input 
                type="file" 
                @change="handleFingerprintUpload" 
                accept=".dat,.bin,.template"
                class="file-input"
              />
              <div class="upload-area">
                <span v-if="!formData.empreinte_digitale">🔒 Importer empreinte digitale</span>
                <span v-else class="file-name">Empreinte importée ✓</span>
              </div>
            </label>
            <p class="help-text">Format: fichiers biométriques (.dat, .bin)</p>
          </div>

          <!-- Scan facial optionnel -->
          <div class="facial-scan">
            <button 
              type="button" 
              @click="startFacialScan" 
              :disabled="isScanning"
              class="scan-btn"
            >
              {{ isScanning ? 'Scan en cours...' : '📸 Scanner visage' }}
            </button>
            <div v-if="facialData" class="scan-result">
              <span>Données faciales capturées ✓</span>
              <button type="button" @click="clearFacialData" class="clear-btn">Effacer</button>
            </div>
          </div>
        </div>
      </fieldset>
      <!-- INFORMATIONS DE RÉSIDENCE -->
      <fieldset>
        <legend>Adresse</legend>
        <textarea v-model="formData.adresse" placeholder="Adresse complète*" required class="full-width"></textarea>
        <div class="form-row">
            <select v-model="formData.province">
              <option value="">Choisir une province</option>
              <option v-for="prov in provinces" :key="prov.id" :value="prov.id">
                {{ prov.nom }}
              </option>

          </select>

<!-- Sélecteur dynamique des régions -->
          <select 
                name="region" 
                id="region" 
                v-model="formData.region"
                v-if="regions[formData.province]"
              >
                <option 
                  v-for="region in regions[formData.province]" 
                  :key="region"
                  :value="region"
                >
                  {{ region }}
                </option>
              </select>


        </div>
        <div class="form-row">
          <input v-model="formData.commune" placeholder="Commune*" required />
          <input v-model="formData.quartier" placeholder="Quartier*" required />
        </div>
        <div class="form-row">
          <input v-model="formData.code_postal" placeholder="Code postal" />
          <input v-model="formData.telephone" placeholder="Téléphone*" required />
        </div>
        <input v-model="formData.email" type="email" placeholder="Email" class="full-width" />
      </fieldset>

      <!-- INFORMATIONS PROFESSIONNELLES -->
      <fieldset>
        <legend>Informations Professionnelles</legend>
        <div class="form-row">
          <input v-model="formData.profession" placeholder="Profession" />
          <input v-model="formData.employeur" placeholder="Employeur" />
        </div>
        <select v-model="formData.situation_professionnelle" class="full-width">
          <option value="">Situation professionnelle</option>
          <option value="A">Actif</option>
          <option value="C">Chômeur</option>
          <option value="E">Étudiant</option>
          <option value="R">Retraité</option>
          <option value="I">Indépendant</option>
          <option value="F">Fonctionnaire</option>
        </select>
        <input v-model="formData.revenu_annuel" type="number" placeholder="Revenu annuel" step="0.01" />
      </fieldset>

      <!-- INFORMATIONS ÉDUCATIVES -->
      <fieldset>
        <legend>Éducation</legend>
        <select v-model="formData.niveau_education" class="full-width">
          <option value="">Niveau d'éducation</option>
          <option value="P">Primaire</option>
          <option value="S">Secondaire</option>
          <option value="B">Baccalauréat</option>
          <option value="U">Universitaire</option>
          <option value="M">Master</option>
          <option value="D">Doctorat</option>
        </select>
        <input v-model="formData.diplome" placeholder="Diplôme obtenu" class="full-width" />
        <input v-model="formData.etablissement" placeholder="Établissement" class="full-width" />
      </fieldset>

      <!-- INFORMATIONS SANITAIRES -->
      <fieldset>
        <legend>Informations Sanitaires</legend>
        <div class="form-row">
          <select v-model="formData.groupe_sanguin">
            <option value="">Groupe sanguin</option>
            <option value="A+">A+</option>
            <option value="A-">A-</option>
            <option value="B+">B+</option>
            <option value="B-">B-</option>
            <option value="AB+">AB+</option>
            <option value="AB-">AB-</option>
            <option value="O+">O+</option>
            <option value="O-">O-</option>
          </select>
          <label class="checkbox-label">
            <input v-model="formData.couverture_medicale" type="checkbox" />
            Couverture médicale
          </label>
        </div>
        <textarea v-model="formData.allergies" placeholder="Allergies connues" class="full-width"></textarea>
        <input v-model="formData.nom_medecin_traitant" placeholder="Médecin traitant" class="full-width" />
      </fieldset>

      <!-- INFORMATIONS CIVIQUES -->
      <fieldset>
        <legend>Informations Civiques</legend>
        <input v-model="formData.bureau_vote" placeholder="Bureau de vote" class="full-width" />
        <input v-model="formData.circonscription_electorale" placeholder="Circonscription électorale" class="full-width" />
        <input v-model="formData.situation_militaire" placeholder="Situation militaire" class="full-width" />
      </fieldset>

      <!-- INFORMATIONS DES PARENTS -->
      <fieldset>
        <legend>Informations des Parents</legend>
        <div class="form-row">
          <input v-model="formData.nom_pere" placeholder="Nom du père" />
          <input v-model="formData.nom_mere" placeholder="Nom de la mère" />
        </div>
        <div class="form-row">
          <input v-model="formData.profession_pere" placeholder="Profession du père" />
          <input v-model="formData.profession_mere" placeholder="Profession de la mère" />
        </div>
      </fieldset>

      <button type="submit">Enregistrer le Citoyen</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted, reactive,watch } from 'vue'

const formData = reactive({
  // Informations personnelles
  nom: '',
  prenoms: '',
  sexe: '',
  date_naissance: '',
  age:null,
  lieu_naissance: '',
  nationalite: 'Malagasy',
  situation_familiale: '',
  
  // Documents
  numero_cin: '',
  numero_passeport: '',
  numero_securite_sociale: '',
  numero_contribuable: '',
  
  // Adresse
  adresse: '',
  province: '',
  region: '',
  commune: '',
  quartier: '',
  code_postal: '',
  telephone: '',
  email: '',
   // Photo et biométrie
  photo: null,
  empreinte_digitale: null,
  donnees_faciales: null,
  // Profession
  profession: '',
  employeur: '',
  situation_professionnelle: '',
  revenu_annuel: '',
  
  // Éducation
  niveau_education: '',
  diplome: '',
  etablissement: '',
  
  // Santé
  groupe_sanguin: '',
  allergies: '',
  couverture_medicale: false,
  nom_medecin_traitant: '',
  
  // Civique
  bureau_vote: '',
  circonscription_electorale: '',
  situation_militaire: '',
  
  // Parents
  nom_pere: '',
  nom_mere: '',
  profession_pere: '',
  profession_mere: ''
})
// 🧮 Calcul automatique de l’âge quand la date change
watch(() => formData.date_naissance, (newDate) => {
  if (!newDate) {
    formData.age = null
    return
  }
  const today = new Date()
  const birthDate = new Date(newDate)
  let age = today.getFullYear() - birthDate.getFullYear()
  const m = today.getMonth() - birthDate.getMonth()
  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
    age--
  }
  formData.age = age
})
const data = ref([])
const message = ref('')
const success = ref(false)
const photoPreviewUrl = ref('')
const facialData = ref(null)
const isScanning = ref(false)
const isSubmitting = ref(false)

const regions = ref({
  1: [
    'Analamanga',
    'Bongolava',
    'Itasy',
    'Vakinankaratra'
  ],
  2: [
    'Amoron\'i Mania',
    'Atsimo-Atsinanana',
    'Haute Matsiatra',
    'Ihorombe',
    'Vatovavy-Fitovinany'
  ],
  3: [
    'Alaotra-Mangoro',
    'Analanjirofo',
    'Atsinanana'
  ],
  4: [
    'Betsiboka',
    'Boeny',
    'Melaky',
    'Sofia'
  ],
  5: [
    'Androy',
    'Anosy',
    'Atsimo-Andrefana',
    'Menabe'
  ],
  6: [
    'Diana',
    'Sava'
  ]
});

const provinces = ref([])

onMounted(async () => {
  const res = await fetch('http://127.0.0.1:8000/api/provinces/')
  provinces.value = await res.json()
})
function handlePhotoUpload(event) {
  const file = event.target.files[0]
  if (file) {
    // Validation de la taille
    if (file.size > 2 * 1024 * 1024) {
      message.value = 'La photo ne doit pas dépasser 2MB'
      success.value = false
      return
    }

    // Validation du type
    if (!file.type.startsWith('image/')) {
      message.value = 'Veuillez sélectionner une image valide'
      success.value = false
      return
    }

    formData.photo = file
    
    // Prévisualisation
    const reader = new FileReader()
    reader.onload = (e) => {
      photoPreviewUrl.value = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

function removePhoto() {
  formData.photo = null
  photoPreviewUrl.value = ''
}

// Gestion des empreintes digitales
function handleFingerprintUpload(event) {
  const file = event.target.files[0]
  if (file) {
    // Validation de la taille (typiquement < 1KB pour les templates)
    if (file.size > 10 * 1024) {
      message.value = 'Fichier d\'empreinte trop volumineux'
      success.value = false
      return
    }
    
    formData.empreinte_digitale = file
  }
}

// Simulation de scan facial (à adapter avec une vraie API)
function startFacialScan() {
  isScanning.value = true
  message.value = 'Veuillez positionner votre visage devant la caméra...'
  
  // Simulation - remplacer par une vraie capture
  setTimeout(() => {
    facialData.value = {
      template: 'facial_template_data_here',
      features: ['eye_distance', 'nose_shape', 'jaw_line']
    }
    formData.donnees_faciales = facialData.value
    isScanning.value = false
    message.value = 'Scan facial terminé avec succès'
    success.value = true
  }, 3000)
}

function clearFacialData() {
  facialData.value = null
  formData.donnees_faciales = null
}
async function reloadInfo() {
  try {
    const res = await fetch('http://127.0.0.1:8000/api/citoyen/')
    data.value = await res.json()
  } catch (error) {
    console.error('Erreur lors du chargement des données:', error)
  }
}

onMounted(() => {
  reloadInfo()
})

async function submitForm() {
  isSubmitting.value = true
  
  try {
    // Création FormData pour gérer les fichiers
    const formDataToSend = new FormData()
    console.log(formData.province)
    if (formData.age < 18) {
      formData.numero_cin = null; // ou ''
    }

    // Ajout des champs texte
    Object.keys(formData).forEach(key => {
      if (formData[key] !== null && formData[key] !== '' && 
          key !== 'photo' && key !== 'empreinte_digitale' && key !== 'donnees_faciales') {
        formDataToSend.append(key, formData[key])
      }
    })
    
    // Ajout des fichiers
    if (formData.photo) {
      formDataToSend.append('photo', formData.photo)
    }
    
    if (formData.empreinte_digitale) {
      formDataToSend.append('empreinte_digitale', formData.empreinte_digitale)
    }
    
    if (formData.donnees_faciales) {
      formDataToSend.append('donnees_faciales', JSON.stringify(formData.donnees_faciales))
    }

    const res = await fetch('http://127.0.0.1:8000/api/citoyen/', {
      method: 'POST',
      body: formDataToSend
      // Note: Ne pas mettre Content-Type, le navigateur le fera automatiquement avec le bon boundary
    })

    if (res.ok) {
      message.value = 'Citoyen enregistré avec succès!'
      success.value = true
      resetForm()
      reloadInfo()
    } else {
      const errorData = await res.json()
      message.value = `Erreur: ${JSON.stringify(errorData)}`
      success.value = false
    }

  } catch (err) {
    message.value = 'Erreur de connexion au serveur'
    success.value = false
    console.error('Erreur:', err)
  } finally {
    isSubmitting.value = false
  }
}
function resetForm() {
  // Réinitialisation de tous les champs
  Object.keys(formData).forEach(key => {
    if (key === 'nationalite') {
      formData[key] = 'Malagasy'
    } else if (key === 'couverture_medicale') {
      formData[key] = false
    } else {
      formData[key] = null
    }
  })
  photoPreviewUrl.value = ''
  facialData.value = null
}
</script>

<style scoped>
.form-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(0,0,0,0.1);
  background-color: #f9f9f9;
}

fieldset {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  background-color: white;
}
.photo-upload, .fingerprint-upload, .facial-scan {
  margin-bottom: 20px;
}

.upload-label {
  cursor: pointer;
}

.file-input {
  display: none;
}

.upload-area {
  border: 2px dashed #ccc;
  border-radius: 8px;
  padding: 30px;
  text-align: center;
  transition: border-color 0.3s;
  background-color: #fafafa;
}

.upload-area:hover {
  border-color: #4f46e5;
  background-color: #f0f4ff;
}

.photo-preview {
  position: relative;
  display: inline-block;
}

.preview-image {
  width: 150px;
  height: 200px;
  object-fit: cover;
  border-radius: 4px;
  border: 2px solid #4f46e5;
}

.remove-btn {
  position: absolute;
  top: -10px;
  right: -10px;
  background: red;
  color: white;
  border: none;
  border-radius: 50%;
  width: 25px;
  height: 25px;
  cursor: pointer;
  font-size: 12px;
}

.file-name {
  color: green;
  font-weight: bold;
}

.scan-btn, .clear-btn {
  padding: 10px 15px;
  border: 1px solid #ccc;
  border-radius: 6px;
  background: white;
  cursor: pointer;
  margin: 5px;
}

.scan-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.scan-result {
  margin-top: 10px;
  padding: 10px;
  background: #f0fff0;
  border: 1px solid green;
  border-radius: 4px;
}

.help-text {
  font-size: 12px;
  color: #666;
  margin-top: 5px;
}

.biometric-section h4 {
  color: #333;
  margin-bottom: 15px;
  border-bottom: 1px solid #eee;
  padding-bottom: 5px;
}
legend {
  padding: 0 10px;
  font-weight: bold;
  color: #4f46e5;
}

.form-row {
  display: flex;
  gap: 15px;
  margin-bottom: 15px;
}

.form-row > * {
  flex: 1;
}

.full-width {
  width: 100%;
  margin-bottom: 15px;
}

input, select, textarea {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 14px;
}

input:focus, select:focus, textarea:focus {
  outline: none;
  border-color: #4f46e5;
  box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.1);
}

textarea {
  min-height: 80px;
  resize: vertical;
}

.checkbox-label {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 0;
}

.checkbox-label input[type="checkbox"] {
  width: auto;
}

button {
  padding: 12px 30px;
  border: none;
  border-radius: 6px;
  background-color: #4f46e5;
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.2s;
  font-size: 16px;
  width: 100%;
}

button:hover {
  background-color: #3730a3;
}

.success {
  color: green;
  margin-bottom: 15px;
  padding: 10px;
  background-color: #f0fff4;
  border-radius: 6px;
  border: 1px solid green;
}

.error {
  color: red;
  margin-bottom: 15px;
  padding: 10px;
  background-color: #fff5f5;
  border-radius: 6px;
  border: 1px solid red;
}

@media (max-width: 768px) {
  .form-row {
    flex-direction: column;
    gap: 10px;
  }
  
  .form-container {
    margin: 10px;
    padding: 20px;
  }
}
</style>