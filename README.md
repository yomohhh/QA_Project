Тесты для сайта [saucedemo.com](https://www.saucedemo.com/) на Python, pytest и Playwright. Отчёты строятся через Allure.

**Отчёт:** https://yomohhh.github.io/QA_Project/

## Что проверяется

Вход: правильный пароль, неправильный пароль, пустые поля

Корзина: добавить товар, открыть корзину, удалить товар

API: получить пост, список пользователей, несуществующий пост, создать пост

## Запуск

Нужны Python 3.12 и pip.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m playwright install chromium
pytest -v
```

## Что происходит при push

Тесты запускаются на GitHub Actions. Потом отчёт публикуется на GitHub Pages, ссылка выше.

## Структура

`pages/` — классы страниц сайта
`tests/` — тесты и фикстуры
`.github/workflows/` — настройка CI

