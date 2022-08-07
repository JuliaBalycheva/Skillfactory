#!/usr/bin/python3
# -*- encoding=utf8 -*-

import os

from pages.base import WebPage
from pages.web_element import WebElement
from pages.web_element import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://www.amazon.com/'

        super().__init__(web_driver, url)

    homepage_banner = WebElement(id='desktop-banner')
    homepage_grid_blocks = ManyWebElements(xpath="//div[contains(@class, 'quadrant-container')]")
    homepage_signin_button = WebElement(xpath="(//span[text()='Sign in'])[last()]")
    homepage_today_deals_link = WebElement(xpath="//span[text()='Today''s Deals']")
    homepage_customer_service_link = WebElement(xpath="//span[text()='Customer Service']")
    homepage_registry_link = WebElement(xpath="//span[text()='Registry']")
    homepage_gift_cards_link = WebElement(xpath="//span[text()='Gift Cards']")
    homepage_sell_link = WebElement(xpath="//span[text()='Sell']")
    homepage_menu_link = WebElement(id='nav-hamburger-menu')
    homepage_menu_items = ManyWebElements(xpath="//*[contains(@class, 'hmenu-item')]")

    signin_email_field = WebElement(id='ap_email')
    signin_continue_button = WebElement(id='continue')
    signin_create_account_button = WebElement(id='createAccountSubmit')
    signin_error_text = WebElement(xpath="//*[contains(@class, 'a-alert-heading')]")

    signup_name_field = WebElement(id='ap_customer_name')
    signup_email_field = WebElement(id='ap_email')
    signup_password_field = WebElement(id='ap_password')
    signup_continue_button = WebElement(id='continue')
    signup_name_missing_alert = WebElement(xpath="//div[contains(@id, 'auth-customerName-missing-alert')]//div[contains(@class,'a-alert-content')]")
    signup_email_missing_alert = WebElement(xpath="//div[contains(@id, 'auth-email-missing-alert')]//div[contains(@class,'a-alert-content')]")
    signup_password_missing_alert = WebElement(xpath="//div[contains(@id, 'auth-password-missing-alert')]//div[contains(@class,'a-alert-content')]")

    search = WebElement(id='twotabsearchtextbox')
    search_run_button = WebElement(id='nav-search-submit-button')

    results_list = ManyWebElements(xpath="//*[@id='search']//div[contains(@class,'s-result-item')]")
    results_list_titles = ManyWebElements(xpath="//*[@id='search']//div[contains(@class,'s-result-item')]//div[contains(@class,'s-card-container')]//span[contains(@class,'a-size-medium')]")
    results_filter_logitech = ManyWebElements(xpath="//li[@aria-label='Logitech']")

    detail_add_to_card_button = WebElement(id='add-to-cart-button')
    detail_similar_item = ManyWebElements(xpath="//th[contains(@class,'comparison_image_title_cell')]")
    detail_related_products = ManyWebElements(xpath="//div[@id='sp_detail']//li[contains(@class,'a-carousel-card')]")
    detail_customer_questions = WebElement(xpath="//h2[contains(@class,'askWidgetHeader')]")
    detail_buy_variants = ManyWebElements(xpath="//div[contains(@id,'variation_style_name')]//li")

    detail_card_count = WebElement(id='nav-cart-count')
    detail_buy_now_button = WebElement(id='buy-now-button')

    results_section_label = WebElement(xpath="//*[@id='search']//span[text()='RESULTS']")
    highlyrated_section_label = WebElement(xpath="//*[@id='search']//span[text()='HIGHLY RATED']")
    moreresults_section_label = WebElement(xpath="//*[@id='search']//span[text()='MORE RESULTS']")
    todaysdeal_section_label = WebElement(xpath="//*[@id='search']//span[text()='Today''s deals']")