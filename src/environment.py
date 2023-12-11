import argparse

from environs import Env
from pathlib import Path


class Environment:
    # env = Env()
    # env.read_env()

    base_dir = Path(__file__).resolve().parent.parent

    parser = argparse.ArgumentParser(description='Airport vehicle detector')

    parser.add_argument('-v', '--video_path', type=Path, help='Path to video')
    parser.add_argument('-p', '--polygon_path', type=Path, help='Path to polygon')
    parser.add_argument('-o', '--output_path', type=Path, help='Output file path')
    parser.add_argument(
        '-m',
        '--pipeline_mode',
        type=str,
        help='Calc metrics or save intervals',
        default='save'
    )
    parser.add_argument(
        '-t',
        '--time_intervals_path',
        type=Path,
        help='Path to time intervals',
        default=Path(__file__).resolve().parent.parent
    )

    args = parser.parse_args()
    video_path = args.video_path
    polygon_path = args.polygon_path
    output_path = args.output_path


    # def __init__(self):
        # self.video_path = self.env.path('VIDEO_PATH')
        # self.polygon_path = self.env.path('POLYGON_PATH')
        # self.time_intervals = self.env.path('TIME_INTERVALS_PATH')
        # self.output_path = self.env.path('OUTPUT_PATH')


env = Environment()
