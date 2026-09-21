# Проект автоматизации тестирования [TOOLSHOP](https://practicesoftwaretesting.com/).

## Содержание:

- Технологии и инструменты используемые для тестирования данного проекта.
- Реализованные проверки:
    - Тесты пользовательского интерфейса (WEB).
- Способы запуска авто-тестов:
    - Локальный запуск;
    - Удаленный запуск;
    - Параметры для запуска тестов в Jenkins.
- Визуализация.

## Технологии и инструменты используемые для тестирования данного проекта.

<p style="text-align: left;">
<a href="https://www.python.org/"> <img src="resources/images/python.png" height="70" width="70" alt="Python logo."/></a>
<a href="https://docs.pytest.org/en/stable/"> <img src="resources/images/pytest.png" height="70" width="70" alt="Pytest logo."/></a>
<a href="https://www.jetbrains.com/pycharm/"> <img src="resources/images/pycharm.png" height="70" width="70" alt="Pycharm logo."/></a>
<a href="https://www.selenium.dev/"> <img src="resources/images/selenium.png" height="70" width="70" alt="Selenium logo."/></a>
<a href="https://www.jenkins.io/"> <img src="resources/images/jenkins.png" height="70" width="50" alt="Jenkins logo."/></a>
<a href="https://aerokube.com/selenoid/"> <img src="resources/images/selenoid.svg" height="70" width="70" alt="Selenoid logo."/></a>
<a href="https://telegram.org/"> <img src="resources/images/telegram.png" height="70" width="70" alt="Telegram logo."/></a>
</p>

Для предоставления отчетности о выполнении тестов использован инструмент — `Allure-Report`.
Отчет состоит из следующих элементов:

- Шаги;
- Снимок экрана для последнего шага теста;
- Видео выполнения;
- Исходный код страницы;
- Логи консоли браузера.

Дополнительным инструментом уведомления о прохождении тестов выступает ```telegram bot``` отправляющий отчет в
специально созданный для этого канал.

Указанные выше инструменты позволяют не только предоставить отчетность менеджерам, но и в случае проблем быстрее
позволит
разобраться в причине падений тестов.

Удаленный запуск WEB тестов осуществляется с помощью `Selenoid`, который представляет собой ферму браузеров, а системой
CI/CD
выступает — `Jenkins`.

## Реализация тестов.

#### Тесты WEB:

Есть негативные тесты для аутентификации проверяющие различные случаи (неправильные почта/пароль, пустые поле и т. п.).

## Запуск авто-тестов.

<details>
<summary>Нажмите, чтобы раскрыть/скрыть.</summary>

Все команды необходимо выполнять в эмуляторе терминала (консоль).

#### Локальный запуск авто-тестов.

```bash
pytest -sv tests
```

#### Удаленный запуск авто-тестов.

```bash
pytest tests -s --base-url=$BASE_URL --selenoid-url=$SELENOID_URL --environment=$ENVIRONMENT --browser=$BROWSER --browser-version=$BROWSER_VERSION --headless=$HEADLESS --screen-resolution=$SCREEN_RESOLUTION
```

> `--base-url` — Адрес стенда для UI тестов.
>
> `--selenoid-url` — Адрес на котором развернут Selenoid (для удаленного выполнения UI тестов).
>
> `--browser` — Браузер в котором будут выполняться тесты.
>
> `--browser-version` — Версия браузера.
>
> `--screen-resolution` — Размер окна браузера.
>
> `--headless` — Параметр отвечающий за запуск тестов без отображения графического интерфейса.
>
> `--environment` — Конфиг для какого окружения должен использоваться для запуска тестов.

#### Запуск тестов из Jenkins:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest tests -s --base-url=$BASE_URL --selenoid-url=$SELENOID_URL --environment=$ENVIRONMENT --browser=$BROWSER --browser-version=$BROWSER_VERSION --headless=$HEADLESS --screen-resolution=$SCREEN_RESOLUTION
```

</details>

## Визуализация.

### Запуск тестов в <a href="https://jenkins.qa.guru/job/aslan_rb_python_27_thread_toolshop_diploma_project/"> Jenkins: </a>

<div style="text-align: left;">
    <img src="resources/images/jenkins_run_tests.png" alt="Run a freestyle pipeline in Jenkins.">
</div>

### Отчеты в <a href="https://jenkins.qa.guru/job/aslan_rb_python_27_thread_toolshop_diploma_project/6/allure/"> Allure Report: </a>

#### Главная страница отчета:

<div style="text-align: left;">
    <img src="resources/images/allure_general.png" alt="Allure report.">
</div>

#### Страница набора тестов.

<div style="text-align: left;">
    <img src="resources/images/allure_suites.png" alt="Allure report.">
</div>

#### Пример отправляемого отчета в telegram:

<div style="text-align: left;">
    <img src="resources/images/telegram_notification.png" alt="Telegram notifications.">
</div>

#### Видео выполнения теста в Selenoid (Для наглядности был добавлен sleep):

<div style="text-align: left;">
    <img src="resources/videos/video_test_exec.gif" alt="A video of a test that is being executed on Selenoid.">
</div>