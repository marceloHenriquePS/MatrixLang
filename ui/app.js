const { useState } = React;

function App(){
  const [code, setCode] = useState('CREATE([[1, 2], [3, 4]]);');
  const [output, setOutput] = useState('');
  const [running, setRunning] = useState(false);

  async function run(){
    setRunning(true);
    setOutput('Running...');
    try{
      // Try calling a backend API if present
      const resp = await fetch('/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code })
      });
      if(!resp.ok){
        const txt = await resp.text();
        setOutput('Server error: ' + txt);
      } else {
        const data = await resp.json();
        setOutput(JSON.stringify(data, null, 2));
      }
    } catch(e){
      // No backend available — show a helpful message and fallback
      setOutput('No backend detected. To run code locally, either start the Python runner (see README) or implement a /run endpoint.\n\nYour code:\n' + code);
    } finally {
      setRunning(false);
    }
  }

  function openHelp(){
    // open README in new tab if hosted; otherwise try local file
    window.open('../README.md', '_blank');
  }

  return (
    <div className="ide">
      <header>
        <h1>MatrixLang — Mini IDE</h1>
        <div className="actions">
          <button onClick={run} disabled={running}>Run</button>
          <button onClick={openHelp}>Help</button>
        </div>
      </header>

      <main>
        <section className="editor">
          <label>Input</label>
          <textarea value={code} onChange={e=>setCode(e.target.value)} spellCheck={false} />
        </section>

        <section className="output">
          <label>Output</label>
          <pre>{output}</pre>
        </section>
      </main>

      <footer>
        <small>Static demo — Run expects a POST /run that accepts JSON { code: string } and returns JSON result.</small>
      </footer>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />);
