import { useState } from "react";

import Sidebar from "./Sidebar";
import Topbar from "./Topbar";
import Stepper from "./Stepper";
import ParsedRequestCard from "./ParsedRequestCard";
import VendorsCard from "./VendorsCard";

export default function Dashboard({ result }) {
  // PM DASHBOARD STEP STATE

  const [pmStep, setPmStep] = useState(1);

  return (
    <div className="layout">
      <Sidebar />

      <div className="main">
        <Topbar />

        <div className="content">
          {/* STEPPER */}

          <Stepper currentStep={pmStep} />

          {/* =====================================
              STEP 1 → PARSED REQUEST
          ===================================== */}

          {pmStep === 1 && (
            <ParsedRequestCard result={result} nextStep={() => setPmStep(2)} />
          )}

          {/* =====================================
              STEP 2 → VENDORS
          ===================================== */}

          {pmStep === 2 && (
            <VendorsCard
              result={result}
              nextStep={() => setPmStep(3)}
              prevStep={() => setPmStep(1)}
            />
          )}
        </div>
      </div>
    </div>
  );
}
