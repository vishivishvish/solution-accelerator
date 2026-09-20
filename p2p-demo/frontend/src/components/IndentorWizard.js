import { useState } from "react";

export default function IndentorWizard({
  indentorStep,
  setIndentorStep,
  formData,
  setFormData,
  submitRequirement,
}) {
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);

    setTimeout(async () => {
      await submitRequirement();

      setLoading(false);
    }, 2200);
  };

  // =====================================
  // LOADING SCREEN
  // =====================================

  if (loading) {
    return (
      <div className="wizard-screen">
        <div className="wizard-card loading-card">
          <div className="spinner"></div>

          <h2>Generating Procurement Intelligence...</h2>

          <p>Evaluating vendors, pricing, RFQs, and logistics</p>
        </div>
      </div>
    );
  }

  // =====================================
  // MAIN WIZARD
  // =====================================

  return (
    <div className="wizard-screen">
      <div className="wizard-card">
        {/* STEP HEADER */}

        <div className="wizard-header">
          <h1>Procurement Requirement Builder</h1>

          <p>Guided AI-assisted requirement creation</p>
        </div>

        {/* STEP INDICATOR */}

        <div className="wizard-progress">Step {indentorStep} of 6</div>

        {/* =====================================
            STEP 1
        ===================================== */}

        {indentorStep === 1 && (
          <>
            <h2>Select Product Category</h2>

            <div className="wizard-options">
              {["Pipes", "Pumps", "Valves", "Cables"].map((item) => (
                <div
                  key={item}
                  className={`option-card ${
                    formData.category === item ? "selected" : ""
                  }`}
                  onClick={() =>
                    setFormData({
                      ...formData,
                      category: item,
                    })
                  }
                >
                  <h3>{item}</h3>
                </div>
              ))}
            </div>

            <div className="wizard-footer">
              <button
                className="card-primary-btn"
                onClick={() => setIndentorStep(2)}
              >
                Next →
              </button>
            </div>
          </>
        )}

        {/* =====================================
            STEP 2
        ===================================== */}

        {indentorStep === 2 && (
          <>
            <h2>Enter Quantity</h2>

            <input
              className="wizard-input"
              type="number"
              placeholder="Enter quantity"
              value={formData.quantity}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  quantity: e.target.value,
                })
              }
            />

            <div className="wizard-footer">
              <button
                className="card-secondary-btn"
                onClick={() => setIndentorStep(1)}
              >
                ← Back
              </button>

              <button
                className="card-primary-btn"
                onClick={() => setIndentorStep(3)}
              >
                Next →
              </button>
            </div>
          </>
        )}

        {/* =====================================
            STEP 3
        ===================================== */}

        {indentorStep === 3 && (
          <>
            <h2>Select Dimension</h2>

            <div className="wizard-options">
              {["1 inch", "2 inch", "4 inch", "6 inch"].map((item) => (
                <div
                  key={item}
                  className={`option-card ${
                    formData.dimension === item ? "selected" : ""
                  }`}
                  onClick={() =>
                    setFormData({
                      ...formData,
                      dimension: item,
                    })
                  }
                >
                  <h3>{item}</h3>
                </div>
              ))}
            </div>

            <div className="wizard-footer">
              <button
                className="card-secondary-btn"
                onClick={() => setIndentorStep(2)}
              >
                ← Back
              </button>

              <button
                className="card-primary-btn"
                onClick={() => setIndentorStep(4)}
              >
                Next →
              </button>
            </div>
          </>
        )}

        {/* =====================================
            STEP 4
        ===================================== */}

        {indentorStep === 4 && (
          <>
            <h2>Select Material</h2>

            <div className="wizard-options">
              {["SS316", "Carbon Steel", "Alloy Steel"].map((item) => (
                <div
                  key={item}
                  className={`option-card ${
                    formData.material === item ? "selected" : ""
                  }`}
                  onClick={() =>
                    setFormData({
                      ...formData,
                      material: item,
                    })
                  }
                >
                  <h3>{item}</h3>
                </div>
              ))}
            </div>

            <div className="wizard-footer">
              <button
                className="card-secondary-btn"
                onClick={() => setIndentorStep(3)}
              >
                ← Back
              </button>

              <button
                className="card-primary-btn"
                onClick={() => setIndentorStep(5)}
              >
                Next →
              </button>
            </div>
          </>
        )}

        {/* =====================================
            STEP 5
        ===================================== */}

        {indentorStep === 5 && (
          <>
            <h2>Select Specification</h2>

            <select
              className="wizard-select"
              value={formData.spec}
              onChange={(e) =>
                setFormData({
                  ...formData,
                  spec: e.target.value,
                })
              }
            >
              <option>ASTM A312</option>
              <option>ASTM A106</option>
              <option>API 5L</option>
            </select>

            <div className="wizard-footer">
              <button
                className="card-secondary-btn"
                onClick={() => setIndentorStep(4)}
              >
                ← Back
              </button>

              <button
                className="card-primary-btn"
                onClick={() => setIndentorStep(6)}
              >
                Review →
              </button>
            </div>
          </>
        )}

        {/* =====================================
            STEP 6
        ===================================== */}

        {indentorStep === 6 && (
          <>
            <h2>Review Requirement</h2>

            <div className="review-card">
              <p>
                <strong>Category:</strong> {formData.category}
              </p>

              <p>
                <strong>Quantity:</strong> {formData.quantity}
              </p>

              <p>
                <strong>Dimension:</strong> {formData.dimension}
              </p>

              <p>
                <strong>Material:</strong> {formData.material}
              </p>

              <p>
                <strong>Specification:</strong> {formData.spec}
              </p>
            </div>

            <div className="wizard-footer">
              <button
                className="card-secondary-btn"
                onClick={() => setIndentorStep(5)}
              >
                ← Back
              </button>

              <button className="card-primary-btn" onClick={handleSubmit}>
                Generate Intelligence →
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}
