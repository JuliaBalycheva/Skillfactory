#!/usr/bin/python3
# -*- encoding=utf8 -*-
import time

import pytest
from pages.selectors import MainPage


def test_check_detail_page_opens(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    assert page.detail_add_to_card_button.is_visible()
    assert page.detail_add_to_card_button.is_clickable()


def test_check_product_can_be_added_to_cart(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    page.detail_add_to_card_button.click()

    assert page.detail_card_count.get_text() == '1'


def test_detail_page_contains_buy_button(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    assert page.detail_buy_now_button.is_visible()
    assert page.detail_buy_now_button.is_clickable()


def test_detail_page_buy_button_click_redirects_to_signin(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    page.detail_buy_now_button.click()
    page.wait_page_loaded()

    assert page.get_current_url().find("signin") != -1


def test_detail_page_contains_similar_items(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    assert page.detail_similar_item.count() > 1


def test_detail_page_contains_related_items(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    assert page.detail_related_products.count() > 1


def test_detail_page_contains_customer_questions_section(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    assert page.detail_customer_questions.get_text().contains('Customer questions & answers')


def test_detail_page_contains_different_buy_options(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.results_list_titles[0].click()

    assert page.detail_buy_variants.count() > 1

