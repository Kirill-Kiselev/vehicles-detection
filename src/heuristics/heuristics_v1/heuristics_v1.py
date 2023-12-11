import numpy as np
from shapely import Polygon, box

from src.service.models import Detections
from src.service.heuristics import Heuristics


class HeuristicsV1(Heuristics):
    def calc_intersections(self, detections: Detections, polygon: np.array) -> bool:
        poly = Polygon(polygon)
        for detection in detections:
            bbox = box(
                *detection.absolute_box.p1.as_tuple,
                *detection.absolute_box.p2.as_tuple
            )
            if bbox.intersects(poly):
                return True

        return False
