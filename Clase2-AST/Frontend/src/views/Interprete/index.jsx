
import { Console } from '../../components/Console';
import { Button } from 'react-bootstrap';
import { useState } from 'react';

import './index.css';

const initialCode = `ejecutar(2 * 3 + 4 -23  * 2 / (5 - 4));`

export const Interprete = () => {
  const [code, setCode] = useState(initialCode);
  const [consoleText, setConsoleText] = useState('');

  const ejecutarHandler = () => {

    fetch('http://127.0.0.1:5000/api/interpretar', {
      method: 'POST',
      body: JSON.stringify({instrucciones:code}),
      headers: {
        'Content-Type':'application/json'
      }
    })
      .then(resp => resp.json())
      .then(data => {
        setConsoleText(data.resultado)
      })
      .catch(console.error);
  }

  const clearHandler = () => {
    setConsoleText('');
  }

  return (
    <div className="d-flex fill flex-column justify-content-start">
      <h2 className='text-white mb-4'>Interprete</h2>
      <div className='row flex-grow-1'>
        <Console code={code} setCode={setCode}>
          <Button
            className='mt-3'
            variant="primary"
            onClick={ejecutarHandler}
          >Ejecutar</Button>{' '}
        </ Console>
        <Console readOnly code={consoleText} setCode={setConsoleText}>
          <Button
            className='mt-3'
            variant="primary"
            onClick={clearHandler}
          >Clear</Button>{' '}
        </Console>
      </div>
    </div>
  )
}
