from selene.support import by
from selene.support.conditions import be
from selene import browser
import allure
from allure_commons.types import Severity
from utils.function_steps import open_main_page, open_issue_tab, search_for_repository, go_to_repository, \
    should_see_issue_with_number


@allure.tag('Github')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'eroshenkoam')
@allure.feature("Tasks in repository")
@allure.story('Checking issue № 76')
@allure.link('https://github.com', name='Testing')
def test_dynamic_steps():
    with allure.step("Open main page"):
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        browser.open('https://github.com')

    with allure.step('Finding repository'):
        browser.element(".header-search-button").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step('Go to repo link'):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Open tab issues'):
        browser.element("#issues-tab").click()

    with allure.step('Checking issue 76'):
        browser.element(by.partial_text("#76")).should(be.visible)


@allure.tag('Github')
@allure.severity(Severity.MINOR)
@allure.label('Owner_2', 'eroshenkoam')
@allure.feature("Tasks in repository second variant")
@allure.story('Checking issue № 76')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")