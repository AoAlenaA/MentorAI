const menuItems = [
  'Диалоговый тренажёр',
  'Аналитика',
  'Курсы',
  'Тесты',
  'Руководство пользователя'
];

export function Sidebar() {
  return (
    <aside className="sidebar">
      <div>
        <div className="brand brand--sidebar">
          <span className="brand__mentor">Mentor</span>
          <span className="brand__ai">AI</span>
        </div>

        <nav className="sidebar-nav" aria-label="Основное меню">
          {menuItems.map((item) => (
            <button key={item} className="sidebar-link" type="button">
              <span className="sidebar-link__icon" />
              <span>{item}</span>
            </button>
          ))}
        </nav>
      </div>

      <button type="button" className="sidebar-chatbot">
        <span className="sidebar-link__icon" />
        <span>Чат-бот</span>
      </button>
    </aside>
  );
}
