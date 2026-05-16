import Sidebar from "./Sidebar";
import Topbar from "./Topbar";
import Stepper from "./Stepper";
import ParsedRequestCard from "./ParsedRequestCard";

export default function Dashboard({ result }) {
  return (
    <div className="layout">
      <Sidebar />

      <div className="main">
        <Topbar />

        <div className="content">
          <Stepper currentStep={1} />

          <ParsedRequestCard />
        </div>
      </div>
    </div>
  );
}
