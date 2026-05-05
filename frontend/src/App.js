import Sidebar from "./components/Sidebar";
import Topbar from "./components/Topbar";
import Stepper from "./components/Stepper";
import ParsedRequestCard from "./components/ParsedRequestCard";

import "./styles/app.css";

function App() {
  return (
    <div className="app-container">
      <Sidebar />

      <div className="main-content">
        <Topbar />
        <Stepper currentStep={1} />
        <ParsedRequestCard />
      </div>
    </div>
  );
}

export default App;
