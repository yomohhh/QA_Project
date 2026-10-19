\# SauceDemo UI Tests



!\[Tests](https://github.com/yomohhh/QA\_Project/actions/workflows/run\_tests.yml/badge.svg)



UI test suite for \[saucedemo.com](https://www.saucedemo.com/) built with

Python, pytest, Playwright and Allure.



\*\*Live report:\*\* https://yomohhh.github.io/QA\_Project/



\## What is tested



\- \*\*Authentication:\*\* login with valid credentials, wrong password, empty username and empty password

\- \*\*Cart:\*\* add a product to the cart and open the cart

\- \*\*Cart:\*\* remove a product from the cart



\## Tech stack



\- Python 3.12

\- pytest and pytest-playwright

\- Playwright (Chromium)

\- Allure for test reports

\- GitHub Actions for continuous integration

\- GitHub Pages for publishing the report



\## Run locally



```bash

python -m venv .venv

.venv\\Scripts\\activate          # Windows

pip install -r requirements.txt

python -m playwright install chromium

pytest -v

```



After the run, raw Allure results are written to `allure-results/`.



To open the report on your machine (requires the Allure CLI):



```bash

allure serve allure-results

```



\## CI and reports



Every push to `master` runs the tests on GitHub Actions. The workflow then:



1\. Runs all tests and writes results to `allure-results/`.

2\. Generates an HTML report with the Allure CLI.

3\. Publishes the report to the `gh-pages` branch, which GitHub Pages serves at the link above.



Pull requests run the tests but do not publish the report.



\## Project structure



```

pages/              Page Object classes for SauceDemo pages

tests/

&#x20; conftest.py       fixtures (logged\_in\_page) and failure screenshots

&#x20; test\_auth.py      login and cart tests

pytest.ini          pytest settings (Allure output, Python path)

requirements.txt    pinned dependencies

.github/workflows/  CI configuration

```



\## License



MIT

