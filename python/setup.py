import requests
import toml
from pathlib import Path


CONFIG = "config.toml"
YEAR = 2023

def get_session():
    try:
        env = toml.load(Path(Path(__file__).parents[2], CONFIG))
        session = env["session"]
    except:
        raise Exception("Error loading session")

    return session


def get_input(day: int):
    input_url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    response = requests.get(input_url, cookies={"session": get_session()}) 
    return response.text.split("\n")[:-1]


if __name__ == "__main__":
    r = get_input(1)