from abc import ABC, abstractmethod
from typing import List

from src.service.models import TranscribedPage


class Saver(ABC):
    @abstractmethod
    def update_data(
        self, transcribed: TranscribedPage, error_lst: List[str]
    ) -> None:
        raise NotImplementedError('Subclasses should implement this')

    @abstractmethod
    def save(self) -> None:
        raise NotImplementedError('Subclasses should implement this')
