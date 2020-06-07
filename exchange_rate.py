import requests
import bs4


def RUB_to_USD():
        url = "https://yandex.ru/"
        html_page = requests.get(url)
        html_soup_page = bs4.BeautifulSoup(html_page.content, "lxml")
        usd = html_soup_page.findAll("span", attrs={"class": "inline-stocks__value_inner"})[0].get_text()
        whole_and_fractional_parts = usd.split(',')
        usd = '.'.join(whole_and_fractional_parts)
        return float(usd)
