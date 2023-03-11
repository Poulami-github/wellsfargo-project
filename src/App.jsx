import { useState } from 'react'
import './App.scss';
import FileUpload from './FileUpload/FileUpload';

function App() {
  const [files, setFiles] = useState([])

  const removeFile = (filename) => {
    setFiles(files.filter(file => file.name !== filename))
  }

  return (
    <div className="App">
      <div className="title">Upload file</div>
      <FileUpload files={files} setFiles={setFiles}
        removeFile={removeFile} />
    </div>
  );
}

export default App;
