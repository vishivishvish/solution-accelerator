import { Tag, Layers, PackageCheck } from "lucide-react";

export default function ParsedRequestCard() {
  return (
    <div className="card">
      <div className="card-header">
        <div>
          <h2>Parsed Request</h2>
          <p className="subtitle">
            AI extracted the following details from your requirement
          </p>
        </div>

        <span className="badge">✓ High Confidence</span>
      </div>

      <div className="grid">
        <div className="box">
          <Tag size={18} />
          <p className="label">Category</p>
          <h3>Pipes</h3>
        </div>

        <div className="box">
          <Layers size={18} />
          <p className="label">Material / Grade</p>
          <h3>Stainless Steel 316</h3>
        </div>

        <div className="box">
          <PackageCheck size={18} />
          <p className="label">Quantity</p>
          <h3>100</h3>
        </div>
      </div>
    </div>
  );
}
