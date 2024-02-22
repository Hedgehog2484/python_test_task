from phone_numbers_parser import PhoneNumbersParser


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
    }
    parser = PhoneNumbersParser(headers)
    print(parser.get_numbers_list("https://hands.ru/company/about"))
    print(parser.get_numbers_list("https://repetitors.info"))
