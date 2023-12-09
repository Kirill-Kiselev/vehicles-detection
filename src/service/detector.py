from abc import ABC, abstractmethod

from src.service.models import Detections, Region


class Detector(ABC):

    @abstractmethod
    def detect(self, region: Region) -> Detections:
        raise NotImplementedError('Subclasses should implement this')
