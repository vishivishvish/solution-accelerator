export default function VendorsCard({ result, nextStep, prevStep }) {
  const vendors = result?.ranked_entities || [];

  return (
    <div className="card">
      <h2>Top Vendors</h2>

      <p className="subtitle">
        AI-ranked suppliers based on price, delivery, and reliability
      </p>

      <div className="vendors-list">
        {vendors.map((vendor, index) => (
          <div key={index} className="vendor-item">
            <div>
              <h3>{vendor.name}</h3>

              <p>Score: {vendor.score}</p>
            </div>

            <span className="chip">Recommended</span>
          </div>
        ))}
      </div>

      <div className="card-footer">
        <button className="card-secondary-btn" onClick={prevStep}>
          ← Back
        </button>

        <button className="card-primary-btn" onClick={nextStep}>
          Next: Pricing →
        </button>
      </div>
    </div>
  );
}
