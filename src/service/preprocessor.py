from abc import ABC, abstractmethod
from typing import List

from src.service.models import Image


class Preprocessor(ABC):

    @abstractmethod
    def preprocess(self, img: Image, error_lst: List[str]) -> Image:
        raise NotImplementedError('Subclasses should implement this')
