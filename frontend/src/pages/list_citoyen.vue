<script setup>
import { ref } from 'vue'

const data = ref([])
const searchTerm = ref('')
const searchProvince=ref('')

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
            <option value="">Toutes les provinces</option>
            <option value="Mahajanga">Mahajanga</option>
            <option value="Antananarivo">Antananarivo</option>
            <option value="Fianarantsoa">Fianarantsoa</option>
            <option value="Toliara">Toliara</option>
            <option value="Toamasina">Toamasina</option>
            <option value="Antsiranana">Antsiranana</option>
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
        <td>{{ c.lieu_naissance }}</td>
        <td>{{ c.province }}</td>
        <td>{{ c.quartier }}</td>
        <td>{{ c.numero_cin }}</td>
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