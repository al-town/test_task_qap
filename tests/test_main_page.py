from pages.main_page import MainPage


def test_search(web_browser):
    """check search field (presence, suggest table output and correctness of the search result)"""
    page = MainPage(web_browser)

    assert page.search.is_presented(), 'Search field in not presented'

    page.search = 'Тензор'

    assert page.search_suggest.are_visible(), 'Search suggest is not visible'

    page.search.send_keys('\ue007')

    assert page.search_results.are_visible(), 'Error with press "Enter" in search field'

    for i in range(5):
        res = page.search_results[i]
        assert 'https://tensor.ru/' in res.get_attribute('href'), \
            f'The first five results do not contain a link to tensor.ru. Error in {i+1} search result'


def test_pictures_section(web_browser):
    """check picture section (presence, correctness of the links and buttons)"""
    page = MainPage(web_browser)

    assert page.pictures.is_presented(), 'Link on picture section is not presented'

    page.pictures.click()
    page.switch_to_window()

    assert 'https://yandex.ru/images/' in page.get_current_url(), 'Error in link on picture section'

    img_ctg_text = page.img_category.get_text()
    page.img_category.click()

    assert img_ctg_text == page.img_search_request.get_attribute('value'), \
        'Wrong text in search by first popular request from picture section'

    search_res_url = page.get_current_url()
    page.img_first_in_search.click()
    page.wait_page_loaded()
    first_img_url = page.get_current_url()
    first_img_src = page.img_page.get_attribute('src')

    assert search_res_url != first_img_url, 'Error with opening the first image in the search request'

    page.img_next_button[-1].click()
    page.wait_page_loaded()

    assert first_img_url != page.get_current_url(), 'Error with opening next image from first image page'

    page.img_next_button[0].click()

    assert first_img_src == page.img_page.get_attribute('src'), \
        'Error with opening previous image from current image page'
