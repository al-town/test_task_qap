# test_task_qap
Test task for the position of a developer in testing

------------

This repository contains autotest for yandex.ru using PageObject
pattern with Selenium and Python (PyTest + Selenium).

Files
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases and make screenshot
of the page when any test case will fail.

[pages/base_page.py](pages/base_page.py) contains PageObject pattern implementation for Python.

[pages/elements.py](pages/elements.py) contains helper class to define web elements on web pages.

[pages/main_page.py](pages/main_page.py) contains locators for relevant site pages

[tests/test_main_page.py](tests/test_main_page.py) contains some tests for different pages of Yandex (https://www.yandex.ru)


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r path_to_file\requirements.txt
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    python3 -m pytest -v --driver Chrome --driver-path path_to_WebDriver_file path_to_file_with_tests
    ```
