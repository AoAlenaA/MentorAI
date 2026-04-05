# MentorAI

# открываешь pg Admin -> создаешь новую бд(database -> create) -> нажимаешь на бд и выбираешь restore (тип данных plain, тип файл sql) -> если таблицы не обновились (schemas-> tables), то выбираешь бд и кликаешь refresh, все обновится

Стартовый шаблон для двух экранов:

- экран логина;
- экран после входа с левым меню и пустой рабочей областью.

## Стек

- Frontend: React + TypeScript + Vite
- Backend: FastAPI

## Как запустить frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend поднимется на `http://localhost:5173`.

## Как запустить backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Backend поднимется на `http://localhost:8000`.

## Тестовый пользователь

- e-mail: `aoanuchina@hse.edu.ru`
- пароль: `password123`

## Что уже есть

- стилизованный экран логина под ваши референсы;
- авторизация через backend;
- переход на `/app` после логина;
- второй экран только с левым меню.

## Что можно делать дальше

1. Подключить реальную базу пользователей.
2. Добавить защищённые роуты.
3. Разбить sidebar по ролям.
4. Наполнить главный экран виджетами.
5. Добавить docker-compose для frontend и backend.
