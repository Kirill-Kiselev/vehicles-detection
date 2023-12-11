from abc import ABC, abstractmethod
from collections import defaultdict
from src.service.models import TranscribedPage


class Saver(ABC):

    @abstractmethod
    def save(self, results: defaultdict) -> None:
        raise NotImplementedError('Subclasses should implement this')
