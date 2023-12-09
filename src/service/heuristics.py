from abc import ABC, abstractmethod
from typing import List
from src.service.models import Detections


class Heuristics(ABC):

    @abstractmethod
    def get_page_order_status(self, detections: Detections) -> str:
        raise NotImplementedError('Subclasses should implement this')

    @abstractmethod
    def stamp_sign_heuristic(
            self,
            reg_sign_stamp_det: Detections,
            error_list: List[str],
            image_width: int
    ) -> List[str]:
        raise NotImplementedError('Subclasses should implement this')
