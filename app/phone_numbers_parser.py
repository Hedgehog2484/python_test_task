import re
import logging
import typing
import requests


class PhoneNumbersParser:
    def __init__(self, custom_headers: dict = None):
        self.headers = custom_headers or {}

    def _get_web_page(self, url: str) -> typing.Optional[str]:
        resp = requests.get(url, headers=self.headers)
        if resp.status_code != 200:
            logging.info(f"Can't get page {url}. Status code: {resp.status_code}")
        return resp.text

    def _parse_numbers(self, source_text: str) -> typing.List[str]:
        found_numbers = []
        for m in re.finditer(r"((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}", source_text):
            potential_num = m.group().strip().replace(" ", "").replace("-", "") \
                             .replace("(", "").replace(")", "")
            if len(potential_num) == 7:
                potential_num = "8495" + potential_num
            if len(potential_num) in [11, 12]:
                found_numbers.append(potential_num.replace("+7", "8"))
        return list(set(found_numbers))

    def get_numbers_list(self, url: str) -> typing.List[str]:
        return self._parse_numbers(self._get_web_page(url))
