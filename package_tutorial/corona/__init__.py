import requests
import sys

from .Subcorona import Subcorona as Subcorona


def get(country: str) -> str:
    url = f"https://corona-stats.online/{country}?minimal=true"
    response = requests.get(url, headers={"user-agent": "curl"})
    return response.text


def main() -> None:
    country = sys.argv[1] if len(sys.argv) > 1 else ""
    print(get(country))


# class Subcorona:
#     def __init__(self) -> None:
#         pass

#     def print_test(self):
#         print("aaa")
