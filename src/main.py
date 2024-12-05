import argparse
import os
from datetime import datetime as dt
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

PARSER = argparse.ArgumentParser()

PARSER.add_argument("-d", "--day", help="Day of the event to get. [01, 25]")
PARSER.add_argument(
    "-y", "--year", help="Year of the event to get. [2015, current-year)"
)


def get_day_input(day: int, year: int) -> str:
    """Get the input for the given problem."""
    req = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        headers={"cookie": f"session={os.getenv('AOC_SESSION_COOKIE')}"},
    )
    return req.text


def main() -> None:
    args = PARSER.parse_args()

    day: int = int(args.day) if args.day else dt.now().day
    year: int = int(args.year) if args.year else dt.now().year

    # Checks
    invalid: bool = False
    if day < 1 or day > 25:
        print(f"Invalid day {day}.")
        invalid = True

    if year < 2015 or year > dt.now().year:
        print(f"Invalid year {year}.")
        invalid = True

    if invalid:
        return

    try:
        # Loading the template
        template: str
        with open("common/python/template.py") as file:
            template = file.read()

        # Creating folder
        path: str = f"./{year}/{str(day).zfill(2)}"
        P: Path = Path(path)

        if not P.exists():
            P.mkdir()
            print(f"Created directory: {path}")

        else:
            print(f"Directory exists: {path}")

        os.chdir(P.absolute())

        # Create solution file
        sol_file: str = f"day{str(day).zfill(2)}.py"
        if not os.path.isfile(sol_file):
            with open(sol_file, "w") as target_file:
                target_file.write(template)

            print(f"Created file: {sol_file}")

        else:
            print(f"{path}/{sol_file} exists")

        # Create the data file
        input_file: str = "input.txt"
        if not os.path.isfile(input_file):
            with open(input_file, "w") as file:
                file.write(get_day_input(day=day, year=year))

            print(f"Created data file: {input_file}")

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
