import pyperclip
import requests
import toml
from os.path import exists
from pathlib import Path


CONFIG = "config.toml"
YEAR = 2023


class Base:
    def __init__(self):
        self.day = 0

    def get_input(self):
        cache = Path(Path(__file__).parents[2], "inputs", f"input{self.day}.txt")
        if exists(cache):
            f = open(cache)
            return f.read().strip()

        input_url = f"https://adventofcode.com/{YEAR}/day/{self.day}/input"
        response = requests.get(input_url, cookies={"session": get_session()})
        if response.status_code == 404:
            exit()

        text = response.text.strip()

        with open(cache, "w+") as f:
            print("caching input...")
            f.write(text)

        return text

    def get_test_input(self):
        f = open(Path(Path(__file__).parents[2], "tests", f"test{self.day}.txt"))
        return f.read().strip()

    def run(self):
        p1 = self.part_1(self.parse_input())
        print(p1)

        p2 = self.part_2(self.parse_input())

        if not p2:
            pyperclip.copy(p1)
        else:
            pyperclip.copy(p2)
            print(p2)


def get_session():
    try:
        env = toml.load(Path(Path(__file__).parents[2], CONFIG))
        session = env["session"]
    except:
        raise Exception("Error loading session")

    return session
