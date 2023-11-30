import requests
import toml
from pathlib import Path


CONFIG = "config.toml"
YEAR = 2022

def get_session():
    try:
        env = toml.load(Path(Path(__file__).parents[1], CONFIG))
        session = env["session"]
    except:
        raise Exception("Error loading session")

    return session


def get_input(day: int):
    input_url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    response = requests.get(input_url, cookies={"session": get_session()}) 
    return response.text


if __name__ == "__main__":
    get_input(1)
