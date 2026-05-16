import RoleSelector from "./components/RoleSelector";
import IndentorWizard from "./components/IndentorWizard";
import Dashboard from "./components/Dashboard";
import { useState } from "react";
import "./styles/app.css";

function App() {
  // -----------------------------
  // STATE
  // -----------------------------

  const [role, setRole] = useState(null);

  const [indentorStep, setIndentorStep] = useState(1);

  const [formData, setFormData] = useState({
    category: "",
    quantity: "",
    dimension: "",
    material: "",
    spec: "",
  });

  const [pipelineResult, setPipelineResult] = useState(null);

  // -----------------------------
  // BACKEND FUNCTION
  // -----------------------------

  const submitRequirement = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/run", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      setPipelineResult(data);

      setRole("Procurement Manager");
    } catch (err) {
      console.error(err);
    }
  };

  // -----------------------------
  // RETURN UI
  // -----------------------------

  if (!role) {
    return <RoleSelector setRole={setRole} />;
  }

  if (role === "Indentor") {
    return (
      <IndentorWizard
        indentorStep={indentorStep}
        setIndentorStep={setIndentorStep}
        formData={formData}
        setFormData={setFormData}
        submitRequirement={submitRequirement}
      />
    );
  }

  if (role === "Procurement Manager") {
    return <Dashboard result={pipelineResult} />;
  }
}

export default App;
