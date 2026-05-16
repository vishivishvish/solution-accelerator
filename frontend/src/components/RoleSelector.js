export default function RoleSelector({ setRole }) {
  return (
    <div className="role-screen">
      <h1>AI Procurement Copilot</h1>

      <div className="role-cards">
        <div className="role-card" onClick={() => setRole("Indentor")}>
          <h2>Indentor</h2>
          <p>Create and track procurement requests</p>
        </div>

        <div
          className="role-card"
          onClick={() => setRole("Procurement Manager")}
        >
          <h2>Procurement Manager</h2>
          <p>Analyze vendors, pricing, RFQs, and shipments</p>
        </div>
      </div>
    </div>
  );
}
