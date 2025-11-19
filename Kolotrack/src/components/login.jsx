import '../assets/login.css'
import { useState } from 'react';

function Login({ setPage }) {
    const [login, setLogin] = useState("");
    const [pswd, setPswd] = useState("");
    const [isLoading, setIsLoading] = useState(false); // Nouveau: état de chargement
    const [error, setError] = useState(null); // Nouveau: état d'erreur

    const handleSubmit = async (e) => {
    e.preventDefault();

    // 1. URL JWT standard
  const response = await fetch("http://127.0.0.1:8000/api/token/", { 
   method: "POST",
   headers: { "Content-Type": "application/json" },
   body: JSON.stringify({ 
            // 2. Changer la clé envoyée de 'login' à 'username'
            username: login, 
            password: pswd 
        }),
   });

   const data = await response.json();
   if (response.ok) {
     localStorage.setItem("access_token", data.access); // Clé 'access'
        localStorage.setItem("refresh_token", data.refresh); // Clé 'refresh'
        
     alert("Connexion réussie !");
     window.location.href = "/dashboard";
   } else {
     alert(data.detail || "Identifiants incorrects"); 
   }
   };

    return (
        <div className="login-container">
            <div className="login-card">
                <h2>Connexion</h2>
                {/* 🚨 Affichage des messages d'erreur */}
                {error && <p className="error-message" style={{ color: 'red' }}>{error}</p>}

                <form onSubmit={handleSubmit}>
                    {/* ... (Champs login et mot de passe, pas de changement ici) */}
                    <div className="form-group">
                        <label htmlFor="login">ID / Numéro / E-mail :</label>
                        <input
                            type="text"
                            id="login"
                            name="login"
                            placeholder="Entrez votre identifiant" 
                            value={login}
                            onChange={(e) => setLogin(e.target.value)}
                            required
                        />
                    </div>
                    <div className="form-group">
                        <label htmlFor="pswd">Mot de passe :</label>
                        <input
                            type="password"
                            id="pswd"
                            name="pswd"
                            placeholder="••••••••" 
                            value={pswd}
                            onChange={(e) => setPswd(e.target.value)}
                            required
                        />
                    </div>

                    <button type="submit" className="login-btn" disabled={isLoading}>
                        {isLoading ? 'Connexion en cours...' : 'Se connecter'}
                    </button>
                </form>
                 <p className="register-link">
                  Pas encore de compte ? 
                <a onClick={() => setPage('register')}> Créer un compte</a>
              </p>
            </div>
        </div>
    );
}

export default Login;