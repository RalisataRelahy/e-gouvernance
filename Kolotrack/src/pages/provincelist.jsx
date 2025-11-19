import axios from "axios";
import { useEffect, useState } from "react";

function ProvincesList() {
  const [provinces, setProvinces] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/provinces/")
      .then(res => setProvinces(res.data))
      .catch(err => console.error("Erreur API :", err));
  }, []);

  return (
    <ul>
      {provinces.map((p, i) => (
        <li key={i}>{p.nom}</li>
      ))}
    </ul>
  );
}

export default ProvincesList;
