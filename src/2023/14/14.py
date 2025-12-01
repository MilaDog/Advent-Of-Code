from timeit import timeit

from timing import Timing


class Dish:
    def __init__(self, data: str):
        self._data: list[list[str]] = self._parse_data(data)
        self._data_coords: dict[tuple[int, int], str] = self._get_data_coords()

    @classmethod
    def read_input(cls):
        """Read the input for the problem"""
        with open("input.txt", "r") as file:
            data: str = file.read()
        return cls(data)

    def _parse_data(self, data: str) -> list[list[str]]:
        """Parse the problem data into a 2D matrix of strings"""
        return [list(line.strip()) for line in data.strip().splitlines()]

    def _get_data_coords(self) -> dict[tuple[int, int], str]:
        """Get a dictionary of all data coordinates and the value at that position"""
        return {(i, j): c for i, row in enumerate(self._data) for j, c in enumerate(row)}

    def data(self) -> list[list[str]]:
        """Get the dish data"""
        return self._data

    def solve(self):
        """Solve the problem to when the dish is tilted in a given direction"""
        for i in range(len(self._data)):
            for j in range(len(self._data[0])):
                # getting cell to wokr with
                pass


def main() -> None:
    """Entry point for solving the problem"""
    reflector_dish: Dish = Dish.read_input()
    reflector_dish.solve()


if __name__ == "__main__":
    print(Timing(timeit(main, number=1)).microseconds, "microseconds")
