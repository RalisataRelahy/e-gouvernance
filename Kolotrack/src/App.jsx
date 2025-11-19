import { useState } from 'react';
import Header from './components/header';
import Login from './components/login';
import Register from './components/inscription';
import './assets/Contain.css'
function App() {
  const [page, setPage] = useState('login');

  const renderContent = () => {
    switch (page) {
      case 'login': return <Login setPage={setPage} />;
      case 'register': return <Register setPage={setPage} />;
      default: return <Login setPage={setPage} />;
    }
  }

  return (
    <div>
      <Header title="KOLOTRACK" /> {/* header fixe */}
      <div className="container">
        {renderContent()} {/* contenu dynamique */}
      </div>
    </div>
  );
}

export default App;
