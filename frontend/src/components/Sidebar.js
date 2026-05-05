import {
  LayoutDashboard,
  FileText,
  Users,
  Truck,
  Receipt,
  BarChart3,
  Settings,
  Plus,
} from "lucide-react";

export default function Sidebar() {
  return (
    <div className="sidebar">
      <h2 className="logo">✨ AI Procurement</h2>

      <button className="primary-btn">
        <Plus size={16} /> New Requirement
      </button>

      <div className="menu">
        <p>
          <LayoutDashboard size={16} /> Dashboard
        </p>
        <p>
          <FileText size={16} /> RFQs
        </p>
        <p>
          <Users size={16} /> Vendors
        </p>
        <p>
          <Truck size={16} /> Shipments
        </p>
        <p>
          <Receipt size={16} /> Invoices
        </p>
        <p>
          <BarChart3 size={16} /> Reports
        </p>
        <p>
          <Settings size={16} /> Settings
        </p>
      </div>
    </div>
  );
}
