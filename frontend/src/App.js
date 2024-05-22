import React, { useState } from 'react';
import axios from 'axios';
import './App.css'; // Importação do arquivo CSS

function App() {
    const [intervaloDe, setIntervaloDe] = useState('');
    const [intervaloAte, setIntervaloAte] = useState('');
    const [resultado, setResultado] = useState(null);
    const [error, setError] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        setError('');
        try {
            const response = await axios.get(`http://127.0.0.1:8000/api/obter-num-div/?intervaloDe=${intervaloDe}&intervaloAte=${intervaloAte}`);
            setResultado(response.data.resultado);
        } catch (err) {
            setError('Erro ao calcular.');
        }
    };

    return (
        <div className="container">
            <div>
                <h1>Calculadora</h1>
                <form onSubmit={handleSubmit}>
                    <div className="input-group">
                        <label>
                            Intervalo de
                            <input type="number" value={intervaloDe} onChange={(e) => setIntervaloDe(e.target.value)} min="1" required /> 
                        </label>
                        <label>
                            Intervalo até
                            <input type="number" value={intervaloAte} onChange={(e) => setIntervaloAte(e.target.value)} min="1" required /> 
                        </label>
                    </div>
                    <div className="button-div">
                        <button className="button-container" type="submit">Calcular</button>
                    </div>
                </form>
                {resultado !== null && (
                    <div className="resultado">
                        <h2>Resultado: {resultado}</h2>
                    </div>
                )}
                {error && (
                    <div>
                        <h2>{error}</h2>
                    </div>
                )}
            </div>
        </div>
    );
}

export default App;
