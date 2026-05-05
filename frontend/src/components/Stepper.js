import {
  FileText,
  Users,
  DollarSign,
  Mail,
  BarChart,
  Truck,
  CheckCircle,
} from "lucide-react";

export default function Stepper({ currentStep }) {
  const steps = [
    { label: "Parsed Request", icon: <FileText size={16} /> },
    { label: "Vendors", icon: <Users size={16} /> },
    { label: "Price Range", icon: <DollarSign size={16} /> },
    { label: "RFQ", icon: <Mail size={16} /> },
    { label: "Quotes", icon: <BarChart size={16} /> },
    { label: "Shipping", icon: <Truck size={16} /> },
    { label: "Reconciliation", icon: <CheckCircle size={16} /> },
  ];

  return (
    <div className="stepper">
      {steps.map((step, i) => (
        <div
          key={i}
          className={`step ${currentStep === i + 1 ? "active" : ""}`}
        >
          <div className="circle">{step.icon}</div>
          <p>{step.label}</p>
        </div>
      ))}
    </div>
  );
}
