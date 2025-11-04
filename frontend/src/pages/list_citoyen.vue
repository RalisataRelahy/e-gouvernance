<script setup>
import { ref,onMounted } from 'vue'

const data = ref([])
const searchTerm = ref('')
const searchProvince=ref('')
const provinces = ref([])

onMounted(async () => {
  const res = await fetch('http://127.0.0.1:8000/api/provinces/')
  provinces.value = await res.json()
})


async function searchCitizens() {
  try {
    // Construction dynamique de l’URL selon les filtres
    let url = 'http://127.0.0.1:8000/api/citoyen/?'

    if (searchTerm.value) {
      url += `search=${encodeURIComponent(searchTerm.value)}&`
    }

    if (searchProvince.value) {
      url += `province=${encodeURIComponent(searchProvince.value)}`
    }

    const res = await fetch(url)
    data.value = await res.json()
  } catch (error) {
    console.error('Erreur lors de la recherche :', error)
  }
}
function getSexe(userSex){
    if(userSex==="M") return "eur";
    else if(userSex==="F")return "euse";
    return ''
}
function getNumCIN(cinNum) {
  if (cinNum === null || cinNum === '') return "Min"
  console.log(cinNum);
  return cinNum
}

function getProvinceName(id) {
  if (!id) return ''
  const prov = provinces.value.find(p => p.id === id)
  return prov ? prov.nom : ''
}
function capitalizeFirstLetter(word) {
  if (!word) return '';
  return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
}
searchCitizens()

</script>
<template>
    <div id="header">
        <h1>Liste des citoyens</h1>
        <input 
            v-model="searchTerm" 
            @input="searchCitizens"
            placeholder="🔍 Rechercher un citoyen..." 
            class="search-bar"
        />
        <select 
            v-model="searchProvince" 
            @change="searchCitizens" 
            class="province-select"
        >
            <option value="">Choisir une province</option>
            <option v-for="prov in provinces" :key="prov.id" :value="prov.id">
                {{ prov.nom }}
            </option>
        </select>

    </div>
    
    <p v-if="data.length === 0">Aucun citoyen trouvé...</p>
    <table v-if="data.length!==0">
        <thead>
            <tr>
                <th>Nom</th>
                <th>Prenom</th>
                <th>Date de Naissance</th>
                <th>Lieu de naissance</th>
                <th>Province</th>
                <th>Quartier</th>
                <th>Numéro de CIN</th>
            </tr>
        </thead>
            <tbody>
    <tr 
        v-for="c in data" 
        :key="c.id"
        @click="$router.push(`/info_user/${c.id}`)" 
        style="cursor:pointer"
    >
        <td>{{ c.nom }}</td>
        <td>{{ c.prenoms }}</td>
        <td>{{ c.date_naissance }}</td>
        <td>{{ capitalizeFirstLetter(c.lieu_naissance) }}</td>
        <td>{{ getProvinceName(c.province) }}</td>
        <td>{{ c.quartier }}</td>
        <td>{{ getNumCIN(c.numero_cin)+getSexe(c.sexe) }}</td>
    </tr>

        </tbody>
    </table>
</template>
<style>
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        cursor: pointer;
    }
    
    th, td {
        border: 1px solid #ddd;
        padding: 8px 12px;
        text-align: left;
    }
    
    th {
        background-color: #f2f2f2;
        font-weight: bold;
        font-family: 'Courier New', Courier, monospace;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    .search-bar{
        width: 400px;
        height: 35px;
        margin: 20px;
        border-radius: 10px;
    }
    .province-select{
        text-align: center;
        width: 200px;
        height: 35px;
        margin: 20px;
        border-radius: 10px;
    }
  </style>