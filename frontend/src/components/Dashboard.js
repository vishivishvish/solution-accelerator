export default function Dashboard({ result }) {
  return (
    <div style={{ padding: "40px" }}>
      <h1>Procurement Manager Dashboard</h1>

      <pre>{JSON.stringify(result, null, 2)}</pre>
    </div>
  );
}
