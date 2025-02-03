import { useState } from "react";
import { generateImage } from "./api";
import { applyGlitchEffect } from "./effects";

function App() {
    const [prompt, setPrompt] = useState("");
    const [image, setImage] = useState(null);

    const handleGenerate = async () => {
        applyGlitchEffect();
        const generatedImage = await generateImage(prompt);
        setImage(`data:image/png;base64,${generatedImage}`);
    };

    return (
        <div className="app">
            <h1 className="title">👽 Alien Image Generator</h1>
            <input type="text" value={prompt} onChange={(e) => setPrompt(e.target.value)} />
            <button onClick={handleGenerate}>Générer</button>
            {image && <img src={image} alt="Generated" />}
        </div>
    );
}

export default App;
