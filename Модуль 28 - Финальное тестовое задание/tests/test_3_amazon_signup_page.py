#!/usr/bin/python3
# -*- encoding=utf8 -*-


import pytest
from pages.selectors import MainPage


def test_check_signin_page_contains_signup_feature(web_browser):
    page = MainPage(web_browser)
    page.homepage_signin_button.wait_to_be_clickable()
    page.homepage_signin_button.click()
    page.wait_page_loaded()

    assert page.signin_create_account_button.is_visible()
    assert page.signin_create_account_button.is_clickable()


def test_check_create_account_button_redirects_to_signup_page(web_browser):
    page = MainPage(web_browser)
    page.homepage_signin_button.wait_to_be_clickable()
    page.homepage_signin_button.click()
    page.wait_page_loaded()
    page.signin_create_account_button.click()
    page.wait_page_loaded()

    assert page.get_current_url().find("register") != -1


def test_check_signup_page_contains_elements(web_browser):
    page = MainPage(web_browser)
    page.homepage_signin_button.wait_to_be_clickable()
    page.homepage_signin_button.click()
    page.wait_page_loaded()
    page.signin_create_account_button.click()
    page.wait_page_loaded()

    assert page.signup_name_field.is_visible()
    assert page.signup_email_field.is_visible()
    assert page.signup_password_field.is_visible()
    assert page.signup_continue_button.is_visible()


def test_check_signup_is_impossible_with_empty_values(web_browser):
    page = MainPage(web_browser)
    page.homepage_signin_button.wait_to_be_clickable()
    page.homepage_signin_button.click()
    page.wait_page_loaded()
    page.signin_create_account_button.click()
    page.wait_page_loaded()

    page.signup_continue_button.wait_to_be_clickable()
    page.signup_continue_button.click()

    assert page.signup_name_missing_alert.is_visible()
    assert page.signup_name_missing_alert.get_text().find("Enter your name") != -1
    assert page.signup_email_missing_alert.is_visible()
    assert page.signup_email_missing_alert.get_text().find("Enter your email or mobile phone number") != -1
    assert page.signup_password_missing_alert.is_visible()
    assert page.signup_password_missing_alert.get_text().find("Minimum 6 characters required") != -1

