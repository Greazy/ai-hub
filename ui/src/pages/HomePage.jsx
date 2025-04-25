import { useState } from "react";

export default function HomePage() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;
    console.log({content: input})
    const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: input }),
    }); 
    const data = await res.json();
    console.log('data is here')
    console.log(data)
    setMessages((prev) => [...prev, { role: "user", content: input }, { role: "ai", content: data.message }]);
    setInput("");
  };

  return (
    <div style={{ maxWidth: 600, margin: "auto", padding: 20 }}>
      <h2>AI Chat</h2>
      <div
        style={{
          maxHeight: "60vh",
          overflowY: "auto",
          border: "1px solid #ccc",
          padding: 10,
          marginBottom: 10,
        }}
      >
        {messages.map((msg, i) => (
          <div key={i} style={{ textAlign: msg.sender === "user" ? "right" : "left" }}>
            <p><strong>{msg.sender}</strong>: {msg.content}</p>
          </div>
        ))}
      </div>
      <input
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Type a message..."
        style={{ width: "80%", padding: 8 }}
      />
      <button onClick={sendMessage} style={{ width: "18%", padding: 8, marginLeft: 4 }}>
        Send
      </button>
    </div>
  );
}