from selene import by, browser
from selene.support.shared.jquery_style import s
import allure

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open("https://github.com")

@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()

@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()

@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()

@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()