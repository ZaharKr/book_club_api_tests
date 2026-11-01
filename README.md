# Book Club API tests

Автотесты Book Club API: https://book-club.qa.guru/api/v1/docs/swagger/

## Покрытие

| Файл | Что проверяет |
|------|---------------|
| `tests/test_get_clubs.py` | GET список клубов, поиск, пагинация, JSON Schema |
| `tests/test_register.py` | Регистрация |
| `tests/test_auth.py` | Авторизация (позитив + негативы) |
| `tests/test_club_crud.py` | CRUD клуба |

## Запуск

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```
