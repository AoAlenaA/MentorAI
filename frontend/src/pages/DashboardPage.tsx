import { Sidebar } from '../components/Sidebar';

export function DashboardPage() {
  return (
    <main className="dashboard-layout">
      <Sidebar />
      <section className="dashboard-empty" aria-label="Рабочая область" />
    </main>
  );
}
