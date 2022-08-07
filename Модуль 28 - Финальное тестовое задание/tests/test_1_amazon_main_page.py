#!/usr/bin/python3
# -*- encoding=utf8 -*-


import pytest
from pages.selectors import MainPage


def test_check_main_page_loads(web_browser):
    page = MainPage(web_browser)
    page.wait_page_loaded()
    assert page.get_current_url().find("www.amazon.com") != -1
    assert page.homepage_banner.is_visible()


def test_check_main_page_contains_banner(web_browser):
    page = MainPage(web_browser)

    assert page.homepage_banner.is_visible()
    assert page.homepage_grid_blocks.count() > 1


def test_check_main_page_contains_search(web_browser):
    page = MainPage(web_browser)

    assert page.search.is_visible()
    assert page.search.is_clickable()
    assert page.search_run_button.is_visible()
    assert page.search_run_button.is_clickable()


def test_check_main_page_contains_search(web_browser):
    page = MainPage(web_browser)

    assert page.search.is_visible()
    assert page.search.is_clickable()
    assert page.search_run_button.is_visible()
    assert page.search_run_button.is_clickable()


def test_check_main_page_block_click_redirects_to_search(web_browser):
    page = MainPage(web_browser)

    page.homepage_grid_blocks.wait_to_be_clickable()
    page.homepage_grid_blocks[0].click()

    assert page.results_section_label.is_presented()


def test_check_main_page_contains_todays_deals_link(web_browser):
    page = MainPage(web_browser)

    assert page.homepage_today_deals_link.is_visible()
    assert page.homepage_today_deals_link.is_clickable()


def test_check_main_page_contains_customer_service_link(web_browser):
    page = MainPage(web_browser)

    assert page.homepage_customer_service_link.is_visible()
    assert page.homepage_customer_service_link.is_clickable()


def test_check_main_page_contains_registry_link(web_browser):
    page = MainPage(web_browser)

    assert page.homepage_registry_link.is_visible()
    assert page.homepage_registry_link.is_clickable()


def test_check_main_page_contains_gift_cards_link(web_browser):
    page = MainPage(web_browser)

    assert page.homepage_gift_cards_link.is_visible()
    assert page.homepage_gift_cards_link.is_clickable()


def test_check_main_page_menu_works(web_browser):
    page = MainPage(web_browser)

    page.homepage_menu_link.click()

    assert page.homepage_menu_items.count() > 1