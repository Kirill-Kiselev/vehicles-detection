import json
from collections import defaultdict
from pathlib import Path

from src.service.saver import Saver


class JSONSaver(Saver):
    def __init__(self, save_path: Path):
        self._save_path = save_path

    def save(self, results: defaultdict) -> None:
        json_data = json.dumps(results)

        with open(self._save_path / 'output_time_intervals.json', 'w') as json_file:
            json_file.write(json_data)
