import numpy as np

from abc import ABC, abstractmethod
from service.models import Detections


class Heuristics(ABC):

    @abstractmethod
    def calc_intersections(
            self,
            detections: Detections,
            polygon: np.array
    ) -> bool:
        raise NotImplementedError('Subclasses should implement this')
