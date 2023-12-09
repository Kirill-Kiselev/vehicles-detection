from abc import ABC, abstractmethod

from src.service.models import Image, TranscribedPage, Detections


class Visualizer(ABC):

    @abstractmethod
    def visualize(
        self, image: Image, transcribed_page: TranscribedPage, detections: Detections
    ) -> None:
        raise NotImplementedError('Subclasses should implement this')
