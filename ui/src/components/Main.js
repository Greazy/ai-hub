import { useState } from "react";


const Main = () => {
    const [message, setMessage] = useState("");
    const [response, setResponse] = useState(null);

    const sendMessage = async () => {
    const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
        "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
    });
    const data = await res.json();
    
    console.log(data);

    setResponse(data);

  };

    return ( 
        <>
        <div>
            
        {response && <pre>{JSON.stringify(response, null, 2)}</pre>}
        
        <input
            type="text"
            placeholder="Enter message"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
        />
        <button onClick={sendMessage}>Send</button>
        
        </div>
        </>
    )
}

export default Main;