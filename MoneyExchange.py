import requests as r
from bs4 import BeautifulSoup

curr = {
    'dollar': ('USD', '$'),
    'euro': ('EUR', '€'),
    'zloty': ('PLN', 'zł'),
    'pound': ('GBP', '£'),
    'hryvna': ('UAH', '₴'),
    'dinar' : ('TND', 'DT')
}


def get_currency(currency1, currency2):
    try:
        if currency1 == currency2:
            return curr[currency2][1]
        if type(currency1[0]) is not str or type(currency2[0]) is not str:
            raise TypeError("Zly typ danych!")
        else:
            url = f'https://www.google.com/finance/quote/{curr[currency1][0]}-{curr[currency2][0]}'
            page = r.get(url)
            soup = BeautifulSoup(page.text, 'html.parser')
            res = soup.find_all('div', attrs={'class': 'YMlKec fxKbKc'})
            res = float([x.text for x in res][0])
            return res, currency2[1]
    except ValueError:
        raise ValueError("Wystapil blad!")
