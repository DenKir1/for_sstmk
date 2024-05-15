import re
import requests
from bs4 import BeautifulSoup


url = 'https://sstmk.ru/'


def get_phone(urls):
    response = requests.get(urls)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Наверное можно проще (в один поиск), но я мало работал с супом
    phone_class = soup.find(class_='phone_lang')
    # В вашем телефоне есть пробелы, а в условии по этому поводу - ничего
    phone = phone_class.find('a', class_='f-white').text.replace(' ', '')

    # Код страны либо + и число до 3 знаков, либо число от 0 до 3 знаков (то есть может отсутствовать)
    # Далее в скобках код города (число без ограничений, нужны границы для реальности)
    # Далее первые числа номера, опять без ограничений, для реальных нужны границы
    # И, наконец, последние 4 числа номера по 2 через дефис
    # Предложил бы ограничить \d{1,5} код города и \d{1,3} для первых чисел номера
    match = re.match(r'^(?:\+\d{1,3}?|\d{0,3})\(\d+\)\d+-\d{2}-\d{2}$', phone)
    return match[0] if match else 'Not found'


if __name__ == "__main__":
    print("Your phone is: ", get_phone(url))
