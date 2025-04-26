import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function ImageGenerator() {
  const [msg, setMsg] = useState("");
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  const handleRequest = async () => {
    try {
      const res = await fetch("http://localhost:8000/generate-image", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt: msg }),
      });
  
      if (!res.ok) {
        const errorData = await res.json();
        throw new Error(errorData.detail || "Failed to generate image");
      }
  
      const blob = await res.blob();
      const imageUrl = URL.createObjectURL(blob);
  
      const imgElement = document.createElement("img");
      imgElement.src = imageUrl;
      imgElement.alt = "Generated image";
      imgElement.style.maxWidth = "100%";
      document.body.appendChild(imgElement);
  
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <h2>Hello, user</h2>
      <input type="msg" placeholder="Msg" value={msg}
        onChange={(e) => setMsg(e.target.value)} />

      <button onClick={handleRequest}>Start</button>
      {error && <p style={{ color: "red" }}>{error}</p>}
    </div>
  );
}