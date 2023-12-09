import json
from typing import List
import cv2
import numpy as np

from tqdm import tqdm
# from src.service.barcode_detector import BarcodeDetector
# from src.service.blur_detector import BlurDetector
# from src.service.preprocessor import Preprocessor
# from src.service.region_filter import RegionFilter
from src.service.detector import Detector
# from src.service.heuristics import Heuristics
from src.environment import env
from src.service.loader import Loader
from src.service.models import Detections
# from src.service.recognizer import Recognizer
# from src.service.saver import Saver
# from src.service.visualizer import Visualizer
from src.utils.fps import FPS


class Service:
    """ Service of any business logic"""
    def __init__(
            self,
            loader: Loader,
            # preprocessor: Preprocessor,
            # region_detector: Detector,
            detector: Detector,
            # heuristics: Heuristics,
            # visualizer: Visualizer,
            # saver: Saver
    ):
        self._loader = loader
        # self._preprocessor = preprocessor
        # self._region_detector = region_detector
        # self._heuristics = heuristics
        self._detector = detector
        # self._visualizer = visualizer
        # self._saver = saver

    def process(self):
        all_FPS = FPS()
        with open(env.polygon_path, '+r') as f:
            f = json.load(f)
        for video_path in self._loader.load():
            polygon = np.array(f[video_path.split('/')[-1]])

            with all_FPS:
                cap = cv2.VideoCapture(video_path)
                if not cap.isOpened():
                    print('Video file opening error')
                    exit()

                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break
                    detections: Detections = self._detector.detect(frame)

                    for detection in detections:
                        cv2.rectangle(
                            frame,
                            detection.absolute_box.p1.as_tuple,
                            detection.absolute_box.p2.as_tuple,
                            (255, 0, 0), 5, )

                    cv2.polylines(
                        frame,
                        [polygon],
                        isClosed=True,
                        color=(255, 255, 255),
                        thickness=2
                    )

                    cv2.imshow('Video', frame)
                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break

                cap.release()
                cv2.destroyAllWindows()


        # self._saver.save()
        print(f'All FPS: {all_FPS}')
