import requests
import toml
from pathlib import Path


CONFIG = "config.toml"
YEAR = 2023


class Base:
    def __init__(self):
        self.day = 0

    def get_input(self):
        input_url = f"https://adventofcode.com/{YEAR}/day/{self.day}/input"
        response = requests.get(input_url, cookies={"session": get_session()})

        return response.text.strip()
    
    def get_test_input(self):
        f = open(Path(Path(__file__).parents[1], "tests", f"test{self.day}.txt"))
        return f.read().strip()

    def run(self):
        print(self.part_1(self.parse_input()))
        print(self.part_2(self.parse_input()))


def get_session():
    try:
        env = toml.load(Path(Path(__file__).parents[2], CONFIG))
        session = env["session"]
    except:
        raise Exception("Error loading session")

    return session
