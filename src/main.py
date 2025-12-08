import argparse
import datetime
import subprocess
from pathlib import Path
from typing import Any

PARSER = argparse.ArgumentParser()

PARSER.add_argument("-y", "--year", help="Year of the event to get. [2015, current-year)")
PARSER.add_argument("-l", "--language", help="Language being used.")


def main() -> None:
    """Run all the problems for the given year."""
    args = PARSER.parse_args()

    year: int = int(args.year) if args.year else datetime.datetime.now().year
    language: str = args.language if args.language else "python"

    directory: Path = Path(__file__).absolute().parent / f"{language.lower()}/{year}"

    if not directory.exists():
        print(f"Target directory does not exist: `{directory}`")
        exit(1)

    print("=" * 28)
    print(f"Running solutions for {year}")
    print("=" * 28)
    print()

    for day in range(25):
        target_directory: Path = directory / f"{str(day + 1).zfill(2)}"
        target_file: Any = target_directory.glob("*.py")

        for file in target_file:
            res = subprocess.run(["py", str(file)], capture_output=True, text=True)

            print("=" * 6)
            print(f"Day {str(day + 1).zfill(2)}")
            print("=" * 6)
            print(res.stdout)

            if res.stderr:
                print(f"Error: {res.stderr}")


if __name__ == "__main__":
    main()
