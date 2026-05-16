export default function IndentorWizard({
  indentorStep,
  setIndentorStep,
  formData,
  setFormData,
  submitRequirement,
}) {
  return (
    <div className="card">
      {indentorStep === 1 && (
        <>
          <h2>Select Category</h2>

          <select
            value={formData.category}
            onChange={(e) =>
              setFormData({
                ...formData,
                category: e.target.value,
              })
            }
          >
            <option>Pipes</option>
            <option>Pumps</option>
            <option>Valves</option>
            <option>Cables</option>
          </select>

          <button onClick={() => setIndentorStep(2)}>Next →</button>
        </>
      )}

      {indentorStep === 2 && (
        <>
          <h2>Enter Quantity</h2>

          <input
            type="number"
            value={formData.quantity}
            onChange={(e) =>
              setFormData({
                ...formData,
                quantity: e.target.value,
              })
            }
          />

          <button onClick={() => setIndentorStep(1)}>← Back</button>

          <button onClick={() => setIndentorStep(3)}>Next →</button>
        </>
      )}

      {/* Repeat same pattern for remaining steps */}

      {indentorStep === 6 && (
        <>
          <h2>Review Requirement</h2>

          <pre>{JSON.stringify(formData, null, 2)}</pre>

          <button onClick={submitRequirement}>Submit Requirement</button>
        </>
      )}
    </div>
  );
}
