<script setup>
import { ref } from 'vue'

const data = ref([])
const searchTerm = ref('')

async function searchCitizens() {
  const res = await fetch(`http://127.0.0.1:8000/api/citoyen/?search=${searchTerm.value}`)
  data.value = await res.json()
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
  </style>