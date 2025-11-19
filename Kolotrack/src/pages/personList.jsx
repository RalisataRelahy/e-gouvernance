import axios from "axios";
import { useEffect, useState } from "react";

function CitoyenList() {
  const [citoyens, setCitoyen] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/citoyen/")
      .then(res => setCitoyen(res.data))
      .catch(err => console.error("Erreur API :", err));
  }, []);

  return (
    <ul>
      {citoyens.map((p, i) => (
        <li key={i}>{p.nom}-{p.prenoms}</li>
      ))}
    </ul>
  );
}

export default CitoyenList;
