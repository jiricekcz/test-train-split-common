from abc import ABC, abstractmethod
from typing import Iterable

from common.interfaces.distance_matrix import IDistanceMatrix

"""
This class is an abstract class for holding asset ids split into chunks.
"""
class ISplit(ABC):
    @abstractmethod
    def splits(self) -> Iterable[Iterable[int]]:
        pass

"""
This class is an abstract class for splitting assets into chunks by IDs and distances from the distance matrix.
"""
class ISplitter(ABC):
    @abstractmethod
    def calculateSplit(self, distances: IDistanceMatrix, distribution: "list[int]") -> Iterable[ISplit]:
        pass

