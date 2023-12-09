from typing import Any

import cv2
import numpy as np

from src.service.detector import Detector
from src.service.models import Blob, Detections, Image, Detection, Box, Point
from src.utils.openvino_adapter_mixin import OpenVINOAdapterMixin


class OpenVINODetector(Detector, OpenVINOAdapterMixin):
    def __init__(
            self,
            model: str,
            weights: str,
            scale_factor: float,
            score_threshold: float,
            width: int,
            height: int,
    ) -> None:
        super().__init__(model, weights, scale_factor, width, height)
        self._score_threshold = score_threshold

    def _pre_processing(self, image: Image) -> Blob:
        image = cv2.resize(image, (self._width, self._height))
        image = image.transpose((2, 0, 1))  # BHWC to BCHW
        image = np.expand_dims(image, axis=0)
        return image

    def _post_processing(self, output: Any, original_image: Image) -> Any:
        image_height, image_width = original_image.shape[:2]
        output = output[output[:, :, :, 2] > self._score_threshold]
        detections = []

        for _, _, conf, x_min, y_min, x_max, y_max in output:
            detections.append(
                Detection(
                    absolute_box=Box[int](
                        p1=Point(x=int(x_min * image_width), y=int(y_min * image_height)),
                        p2=Point(x=int(x_max * image_width), y=int(y_max * image_height))),
                    relative_box=Box[float](p1=Point(x=x_min, y=y_min), p2=Point(x=x_max, y=y_max)),
                    score=conf,
                    label=0,
                ),
            )

        return detections

    def detect(self, image: Image) -> Detections:
        detections: Detections = self._predict(image=image)
        return detections
