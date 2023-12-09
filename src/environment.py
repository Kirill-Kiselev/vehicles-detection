from environs import Env
from pathlib import Path


class Environment:
    env = Env()
    env.read_env()

    base_dir = Path(__file__).resolve().parent.parent

    def __init__(self):
        self.video_path = self.env.path('VIDEO_PATH')
        self.polygon_path = self.env.path('POLYGON_PATH')
        self.time_intervals = self.env.path('TIME_INTERVALS_PATH')
        self.output_path = self.env.path('TIME_INTERVALS_PATH')


env = Environment()
