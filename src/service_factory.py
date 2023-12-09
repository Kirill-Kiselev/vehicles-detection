from src.detectors import OpenVINODetector
from src.loders import FolderLoader
# from src.heuristics import HeuristicsV1
# from src.preprocessor.preprocessor_v1.preprocessor_v1 import PreprocessorV1
# from src.savers import JSONSaver
from src.environment import Environment
from src.service.detector import Detector
from src.service.loader import Loader
from src.service.heuristics import Heuristics
from src.service.preprocessor import Preprocessor
from src.service.saver import Saver
from src.service.service import Service
from src.service.visualizer import Visualizer
# from src.visualizers import visualizer_factory


class ServiceFactory:
    @staticmethod
    def create(env: Environment) -> Service:
        loader: Loader = FolderLoader(env.video_path)
        # preprocessor: Preprocessor = PreprocessorV1(env.min_h, env.min_w, env.format)

        # region_detector: Detector = detector_factory.create(key=env.region_detector_model)
        # heuristics: Heuristics = HeuristicsV1()
        # region_filter: RegionFilter = YOLODetectorRegionFilter()
        print(env.base_dir)
        detector: Detector = OpenVINODetector(
            model=env.base_dir / 'assets/models/FP32/vehicle-detection-0202.xml',
            weights=env.base_dir / 'assets/models/FP32/vehicle-detection-0202.bin',
            scale_factor=1.0,
            score_threshold=0.5,
            width=512,
            height=512
        )
        # recognizer: Recognizer = recognizer_factory.create(key=env.recognition_model)
        # visualizer: Visualizer = visualizer_factory.create(key=env.visualizer)
        # saver: Saver = JSONSaver()

        return Service(
            loader=loader,
            # preprocessor=preprocessor,
            # blur_detector=blur_detector,
            # barcode_detector=barcode_detector,
            # region_detector=region_detector,
            # heuristics=heuristics,
            # region_filter=region_filter,
            detector=detector,
            # recognizer=recognizer,
            # visualizer=visualizer,
            # saver=saver
        )
