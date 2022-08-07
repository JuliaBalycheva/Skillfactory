#!/usr/bin/python3
# -*- encoding=utf8 -*-


import pytest
from pages.selectors import MainPage


def test_check_main_page_contains_signin_feature(web_browser):
    page = MainPage(web_browser)
    page.wait_page_loaded()

    assert page.homepage_signin_button.is_visible()


def test_check_signin_button_redirects_to_signin_page(web_browser):
    page = MainPage(web_browser)
    page.homepage_signin_button.wait_to_be_clickable()
    page.homepage_signin_button.click()
    page.wait_page_loaded()
    assert page.get_current_url().find("signin") != -1


def test_check_signin_page_contains_elements(web_browser):
    page = MainPage(web_browser)

    page.homepage_signin_button.wait_to_be_clickable()
    page.homepage_signin_button.click()

    page.wait_page_loaded()

    assert page.signin_email_field.is_visible()
    assert page.signin_continue_button.is_visible()
    assert page.signin_create_account_button.is_visible()


def test_check_signin_button_enter_wrong_email_results_in_error_message(web_browser):
    page = MainPage(web_browser)
    page.homepage_signin_button.wait_to_be_clickable()
    page.homepage_signin_button.click()
    page.wait_page_loaded()

    page.signin_email_field = 'absolutelywrongemail@test.com'
    page.signin_continue_button.click()

    assert page.signin_error_text.is_visible()
    assert page.signin_error_text.get_text() == 'There was a problem'
