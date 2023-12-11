from detectors import OpenVINODetector
from loders import FolderLoader
from heuristics import HeuristicsV1
from savers import JSONSaver
from environment import Environment
from service.detector import Detector
from service.loader import Loader
from service.heuristics import Heuristics
from service.saver import Saver
from src.service.service import Service


class ServiceFactory:
    @staticmethod
    def create(env: Environment) -> Service:
        loader: Loader = FolderLoader(env.video_path)
        detector: Detector = OpenVINODetector(
            model=env.base_dir / 'assets/models/FP32/vehicle-detection-0202.xml',
            weights=env.base_dir / 'assets/models/FP32/vehicle-detection-0202.bin',
            scale_factor=1.0,
            score_threshold=0.5,
            width=512,
            height=512
        )
        heuristics: Heuristics = HeuristicsV1()
        saver: Saver = JSONSaver(save_path=env.output_path)

        return Service(
            loader=loader,
            heuristics=heuristics,
            detector=detector,
            saver=saver
        )
