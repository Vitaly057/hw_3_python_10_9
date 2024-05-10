from selene import browser, by, be
from selene.support.shared.jquery_style import s
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

        browser.open("/")

    with allure.step('Finding repository'):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step('Go to repo link'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Open tab issues'):
        s("#issues-tab").click()

    with allure.step('Checking issue 76'):
        s(by.partial_text("#76")).should(be.visible)


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