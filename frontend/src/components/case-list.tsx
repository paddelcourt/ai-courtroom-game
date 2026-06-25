import { getCases } from "@/lib/api";

export async function CaseList() {
  const cases = await getCases();

  return (
    <section className="panel" aria-label="Cases">
      <div className="panel-header">
        <h2>Cases</h2>
        <span className="status">{cases.length} active</span>
      </div>
      {cases.length === 0 ? (
        <div className="case-row">
          <p className="empty-state">No cases yet.</p>
        </div>
      ) : (
        cases.map((caseFile) => (
          <article className="case-row" key={caseFile.id}>
            <div>
              <p className="case-title">{caseFile.title}</p>
              <p className="case-description">{caseFile.description ?? "No description"}</p>
            </div>
            <span className="status">{caseFile.status}</span>
          </article>
        ))
      )}
    </section>
  );
}
