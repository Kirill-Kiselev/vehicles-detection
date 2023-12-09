from pathlib import Path
from typing import Iterator, Optional

from src.service.loader import Loader


class FolderLoader(Loader):
    def __init__(self, folder_path: Path):
        self._folder_path = folder_path

    def load(self) -> Iterator[Optional[str]]:
        for path in sorted(self._folder_path.glob('*.mp4')):
            yield str(path)
