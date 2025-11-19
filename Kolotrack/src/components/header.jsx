import logoMada from '../assets/logo_mada-Photoroom.png';
import '../assets/header.css';

function Header({title}){
    return (<header>
        <div id="container">
            <h1><span id="white">KO</span><span id="green">LO</span><span id="red">TRACK</span></h1>
            <img src={logoMada} alt="logo mada" />
        </div>
        
    </header>)
}
export default Header