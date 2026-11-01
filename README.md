# Book Club API tests (GET clubs)

Автотесты на `GET /api/v1/clubs/` для [Book Club API](https://book-club.qa.guru/api/v1/docs/swagger/#/clubs/clubsList).

Стек: Python, Pytest, Requests, JSON Schema.

## Установка и запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Покрытие

1. Список клубов возвращает 200 и непустой `results`
2. Ответ соответствует JSON Schema
3. У первого клуба есть title/authors/members
4. Поиск по существующему `bookTitle` находит клуб
5. Пагинация `page_size=2` возвращает 2 элемента
