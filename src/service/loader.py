from abc import ABC, abstractmethod
from typing import Iterator, Optional


class Loader(ABC):

    @abstractmethod
    def load(self) -> Iterator[Optional[str]]:
        raise NotImplementedError('Subclasses should implement this')
