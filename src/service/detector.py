from abc import ABC, abstractmethod

from service.models import Detections, Image


class Detector(ABC):

    @abstractmethod
    def detect(self, image: Image) -> Detections:
        raise NotImplementedError('Subclasses should implement this')
