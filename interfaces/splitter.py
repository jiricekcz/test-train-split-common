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
    @abstractmethod
    def minimalDistanceBetweenSplits(self) -> float:
        pass

    def __repr__(self):
        splits = self.splits()
        s = sum(map(len, splits))
        return f"Split<distribution = [{', '.join(map(lambda x: '{0:.3f}'.format(len(x) / s), splits))}], minDistance = {'{0:.3g}'.format(self.minimalDistanceBetweenSplits())}>"
    
    def __str__(self):
        return self.__repr__()
"""
This class is an abstract class for splitting assets into chunks by IDs and distances from the distance matrix.
"""
class ISplitter(ABC):
    @abstractmethod
    def calculateSplit(self, distances: IDistanceMatrix, distribution: "list[int]") -> Iterable[ISplit]:
        pass

