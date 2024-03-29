from dataclasses import dataclass
from nptyping import NDArray, UInt8
from typing import Any, Generic, List, Tuple, TypeVar


# any color image has 3 channels: red, green, blue
# these constants show order of channels
BGR = RGB = 3

Image = NDArray[(Any, Any, BGR), UInt8]  # [height, width, channels]
Blob = NDArray[(1, BGR, Any, Any), UInt8]  # [batch, channels, height, width]


Coordinate = TypeVar('Coordinate', int, float)


@dataclass
class Point(Generic[Coordinate]):
    x: Coordinate
    y: Coordinate

    @property
    def as_tuple(self) -> Tuple[Coordinate, Coordinate]:
        return self.x, self.y

    @property
    def as_list(self) -> List[Coordinate]:
        return [self.x, self.y]


Points = List[Point]


@dataclass
class Box(Generic[Coordinate]):
    p1: Point[Coordinate]  # top left
    p2: Point[Coordinate]  # bottom right

    @property
    def as_tuple(self) -> Tuple[Coordinate, Coordinate, Coordinate, Coordinate]:
        return *self.p1.as_tuple, *self.p2.as_tuple

    @property
    def as_list(self) -> List[Coordinate]:
        return [*self.p1.as_list, *self.p2.as_list]

    @property
    def height(self) -> Coordinate:
        return max(type(self.p1.y)(0), self.p2.y - self.p1.y)

    @property
    def width(self) -> Coordinate:
        return max(type(self.p1.x)(0), self.p2.x - self.p1.x)


Boxes = List[Box]


@dataclass
class Detection:
    absolute_box: Box[int]
    relative_box: Box[float]
    label: int
    score: float


Detections = List[Detection]
