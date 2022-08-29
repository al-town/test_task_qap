import os
from pages.base_page import WebPage
from pages.elements import WebElement, ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://yandex.ru/'

        super().__init__(web_driver, url)

    # Main search field
    search = WebElement(id='text')

    # List table with search suggest
    search_suggest = ManyWebElements(css_selector='.mini-suggest__item.mini-suggest__item_type_fulltext.mini'
                                                  '-suggest__item_arrow_yes.mini-suggest__item_with-button')

    # Search results
    search_results = ManyWebElements(xpath='//a[@class="Link Link_theme_normal OrganicTitle-Link organic__url link"]')

    # Link to the picture section
    pictures = WebElement(xpath='//a[@data-id="images"]')

    # First popular request in picture section
    img_category = WebElement(css_selector='.PopularRequestList-SearchText')

    # Search field after request in picture section
    img_search_request = WebElement(css_selector='.input__control.mini-suggest__input')

    # First image in search request
    img_first_in_search = WebElement(css_selector='.serp-item__thumb.justifier__thumb')

    # Image page in search request
    img_page = WebElement(css_selector='.MMImage-Origin')

    # Previous/next picture buttons
    img_next_button = ManyWebElements(css_selector='.CircleButton-Icon')
