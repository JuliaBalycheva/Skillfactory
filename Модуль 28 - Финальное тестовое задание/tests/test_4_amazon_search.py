#!/usr/bin/python3
# -*- encoding=utf8 -*-
import time

import pytest
from pages.selectors import MainPage


def test_check_main_search_works(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    assert page.results_section_label.is_visible()
    assert page.moreresults_section_label.is_visible()
    assert page.results_list.count() > 0


def test_check_main_search_returns_correct_results(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    for title in page.results_list_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'keyboard' in title.lower(), msg


def test_check_main_search_results_filtered_by_brand(web_browser):
    page = MainPage(web_browser)

    page.search = 'keyboard'
    page.search_run_button.click()

    page.wait_page_loaded()
    page.results_filter_logitech.click()

    for title in page.results_list_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'keyboard' in title.lower(), msg
        assert 'logitech' in title.lower(), msg





