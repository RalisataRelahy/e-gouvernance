import React, { useState } from 'react';

function Register({ setPage }) {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [password2, setPassword2] = useState("");
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);

        if (password !== password2) {
            setError("Les mots de passe ne correspondent pas.");
            return;
        }

        const urlAPI = "http://127.0.0.1:8000/api/register/"; 

        try {
            const response = await fetch(urlAPI, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, email, password, password2 }),
            });

            const data = await response.json();

            if (response.ok) {
                alert(`Compte ${data.username} créé avec succès ! Veuillez vous connecter.`);
                window.location.href = "/login"; 
            } else {
                const errorMsg = data.username ? `Nom d'utilisateur : ${data.username[0]}` : 
                                 data.email ? `Email : ${data.email[0]}` : 
                                 data.password ? `Mot de passe : ${data.password[0]}` :
                                 data.detail || "Erreur lors de l'inscription.";
                setError(errorMsg);
            }
        } catch (err) {
            console.error("Erreur réseau :", err);
            setError("Impossible de se connecter au serveur.");
        }
    };

    return (
        <div style={{
            minHeight: '100vh',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            position: 'relative',
            overflow: 'hidden',
            fontFamily: 'Arial, sans-serif'
        }} className="container">

            {/* Registration Form */}
            <div style={{
                background: 'rgba(30, 30, 30, 0.8)',
                backdropFilter: 'blur(1px)',
                padding: '40px 50px',
                borderRadius: '12px',
                boxShadow: '0 8px 32px rgba(0, 0, 0, 0.4)',
                width: '100%',
                maxWidth: '450px',
                zIndex: 5
            }}>
                <h2 style={{
                    color: 'white',
                    textAlign: 'center',
                    marginBottom: '30px',
                    fontSize: '28px',
                    fontFamily:'',
                    fontWeight: '500'
                }}>
                    Inscription
                </h2>

                <form onSubmit={handleSubmit}>
                    {error && (
                        <div style={{
                            color: '#ef4444',
                            backgroundColor: 'rgba(239, 68, 68, 0.1)',
                            padding: '12px',
                            borderRadius: '6px',
                            marginBottom: '20px',
                            fontSize: '14px',
                            border: '1px solid rgba(239, 68, 68, 0.3)'
                        }}>
                            {error}
                        </div>
                    )}

                    <div style={{ marginBottom: '20px' }}>
                        <label style={{
                            display: 'block',
                            color: 'white',
                            marginBottom: '8px',
                            fontSize: '14px',
                            fontWeight: '500'
                        }}>
                            Nom d'utilisateur :
                        </label>
                        <input
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            placeholder="Entrez votre nom d'utilisateur"
                            required
                            style={{
                                width: '100%',
                                padding: '12px 16px',
                                borderRadius: '6px',
                                border: 'none',
                                background: 'rgba(255, 255, 255, 0.1)',
                                color: 'white',
                                fontSize: '15px',
                                outline: 'none',
                                transition: 'all 0.3s',
                                boxSizing: 'border-box'
                            }}
                            onFocus={(e) => e.target.style.background = 'rgba(255, 255, 255, 0.15)'}
                            onBlur={(e) => e.target.style.background = 'rgba(255, 255, 255, 0.1)'}
                        />
                    </div>

                    <div style={{ marginBottom: '20px' }}>
                        <label style={{
                            display: 'block',
                            color: 'white',
                            marginBottom: '8px',
                            fontSize: '14px',
                            fontWeight: '500'
                        }}>
                            E-mail :
                        </label>
                        <input
                            type="email"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            placeholder="Entrez votre e-mail"
                            required
                            style={{
                                width: '100%',
                                padding: '12px 16px',
                                borderRadius: '6px',
                                border: 'none',
                                background: 'rgba(255, 255, 255, 0.1)',
                                color: 'white',
                                fontSize: '15px',
                                outline: 'none',
                                transition: 'all 0.3s',
                                boxSizing: 'border-box'
                            }}
                            onFocus={(e) => e.target.style.background = 'rgba(255, 255, 255, 0.15)'}
                            onBlur={(e) => e.target.style.background = 'rgba(255, 255, 255, 0.1)'}
                        />
                    </div>

                    <div style={{ marginBottom: '20px' }}>
                        <label style={{
                            display: 'block',
                            color: 'white',
                            marginBottom: '8px',
                            fontSize: '14px',
                            fontWeight: '500'
                        }}>
                            Mot de passe :
                        </label>
                        <input
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="Entrez votre mot de passe"
                            required
                            style={{
                                width: '100%',
                                padding: '12px 16px',
                                borderRadius: '6px',
                                border: 'none',
                                background: 'rgba(255, 255, 255, 0.1)',
                                color: 'white',
                                fontSize: '15px',
                                outline: 'none',
                                transition: 'all 0.3s',
                                boxSizing: 'border-box'
                            }}
                            onFocus={(e) => e.target.style.background = 'rgba(255, 255, 255, 0.15)'}
                            onBlur={(e) => e.target.style.background = 'rgba(255, 255, 255, 0.1)'}
                        />
                    </div>

                    <div style={{ marginBottom: '25px' }}>
                        <label style={{
                            display: 'block',
                            color: 'white',
                            marginBottom: '8px',
                            fontSize: '14px',
                            fontWeight: '500'
                        }}>
                            Confirmer le mot de passe :
                        </label>
                        <input
                            type="password"
                            value={password2}
                            onChange={(e) => setPassword2(e.target.value)}
                            placeholder="Confirmez votre mot de passe"
                            required
                            style={{
                                width: '100%',
                                padding: '12px 16px',
                                borderRadius: '6px',
                                border: 'none',
                                background: 'rgba(255, 255, 255, 0.1)',
                                color: 'white',
                                fontSize: '15px',
                                outline: 'none',
                                transition: 'all 0.3s',
                                boxSizing: 'border-box'
                            }}
                            onFocus={(e) => e.target.style.background = 'rgba(255, 255, 255, 0.15)'}
                            onBlur={(e) => e.target.style.background = 'rgba(255, 255, 255, 0.1)'}
                        />
                    </div>

                    <button
                        type="submit"
                        style={{
                            width: '100%',
                            padding: '14px',
                            backgroundColor: '#10b981',
                            color: 'black',
                            border: 'none',
                            borderRadius: '6px',
                            fontSize: '16px',
                            fontWeight: '600',
                            cursor: 'pointer',
                            transition: 'all 0.3s',
                            marginBottom: '20px'
                        }}
                        onMouseOver={(e) => e.target.style.backgroundColor = '#059669'}
                        onMouseOut={(e) => e.target.style.backgroundColor = '#10b981'}
                    >
                        S'inscrire
                    </button>

                    <p style={{
                        textAlign: 'center',
                        color: 'rgba(255, 255, 255, 0.7)',
                        fontSize: '14px',
                        margin: 0
                    }}>
                        Déjà un compte ?{' '}
                        <a
                            onClick={() => setPage('login')}
                            style={{
                                cursor:'pointer',
                                color: '#10b981',
                                textDecoration: 'none',
                                fontWeight: '500'
                            }}
                            onMouseOver={(e) => e.target.style.textDecoration = 'underline'}
                            onMouseOut={(e) => e.target.style.textDecoration = 'none'}
                        >
                            Se connecter
                        </a>
                    </p>
                </form>
            </div>
        </div>
    );
}

export default Register;