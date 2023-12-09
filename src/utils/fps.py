from collections import deque
from statistics import mean
from time import perf_counter


# https://book.pythontips.com/en/latest/context_managers.html#implementing-a-context-manager-as-a-class
class FPS:
    def __init__(self):
        self._times = deque(maxlen=100)

    def __enter__(self):
        self._start = perf_counter()

    def __exit__(self, type, value, traceback):
        self._times.append(perf_counter() - self._start)

    @property
    def fps(self) -> float:
        return 1.0 / mean(self._times)

    def __str__(self):
        return f'{self.fps:.2f}'
