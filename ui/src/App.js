import "./App.css";

import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import HomePage from "./pages/HomePage";
import ImageGenerator from "./pages/ImageGenerator";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/image" element={<ImageGenerator />} />
      </Routes>
    </Router>
  );
}

export default App;