import {
  Tag,
  Layers,
  PackageCheck,
  ListChecks,
  CheckCircle,
} from "lucide-react";

export default function ParsedRequestCard({ result }) {
  if (!result) return null;
  const parsed = result?.parsed_request || {};

  const category = parsed.category || "Pipes";

  const material = parsed.material || "SS316";

  const quantity = parsed.quantity || "100";

  const dimension = parsed.dimension || "2 inch";

  const spec = parsed.spec || "ASTM A312";

  return (
    <div className="card">
      {/* HEADER */}

      <div className="card-header">
        <div>
          <h2>Parsed Request</h2>

          <p className="subtitle">
            AI extracted the following details from your requirement
          </p>
        </div>

        <span className="badge">✓ High Confidence</span>
      </div>

      {/* MAIN GRID */}

      <div className="grid">
        <div className="box">
          <Tag size={18} />

          <p className="label">Category</p>

          <h3>{category}</h3>

          <span className="chip">EPC</span>
        </div>

        <div className="box">
          <Layers size={18} />

          <p className="label">Material / Grade</p>

          <h3>{material}</h3>

          <span className="chip">Standard: ASTM A312</span>
        </div>

        <div className="box">
          <PackageCheck size={18} />

          <p className="label">Quantity</p>

          <h3>{quantity}</h3>

          <span className="chip">Unit: NOS</span>
        </div>
      </div>

      {/* ADDITIONAL ATTRIBUTES */}

      <div className="attributes-section">
        <div className="attributes-title">
          <ListChecks size={18} />
          <span>Additional Attributes</span>
        </div>

        <div className="attributes-grid">
          <span className="attribute-chip">Dimension: {dimension}</span>

          <span className="attribute-chip">Specification: {spec}</span>

          <span className="attribute-chip">AI Parsed Requirement</span>

          <span className="attribute-chip">Procurement Ready</span>

          <span className="attribute-chip">Vendor Matching Enabled</span>
        </div>
      </div>

      {/* SUCCESS BANNER */}

      <div className="success-banner">
        <div className="success-icon">
          <CheckCircle size={24} />
        </div>

        <div>
          <h4>Looks good!</h4>

          <p>We’re ready to find the best vendors for your requirement.</p>
        </div>
      </div>

      {/* FOOTER */}

      <div className="card-footer">
        <button className="card-secondary-btn">← Back</button>

        <div className="pagination-dots">
          <span className="dot active"></span>
          <span className="dot"></span>
          <span className="dot"></span>
          <span className="dot"></span>
          <span className="dot"></span>
        </div>

        <button className="card-primary-btn">Next: Vendors →</button>
      </div>
    </div>
  );
}
