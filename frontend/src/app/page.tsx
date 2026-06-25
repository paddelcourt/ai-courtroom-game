import { CaseList } from "@/components/case-list";

export default function Home() {
  return (
    <main className="shell">
      <section className="hero">
        <p className="eyebrow">AI Courtroom Game</p>
        <h1>Trial desk</h1>
        <p className="lede">Start with cases and evidence, then wire in courtroom gameplay.</p>
      </section>
      <CaseList />
    </main>
  );
}
