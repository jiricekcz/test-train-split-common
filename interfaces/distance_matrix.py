from abc import ABC, abstractmethod
from typing import Callable, Iterable, Tuple


class IDistanceMatrix(ABC):

    @abstractmethod
    def getRawDistance(self, x: int, y: int) -> int:
        """
        Gets the raw distance between two objects in the matrix represented by an integer.
        """
        pass

    @abstractmethod
    def setRawDistance(self, x: int, y: int, value: int) -> None:
        """
        Sets the raw distance between two objects in the matrix represented by an integer.
        """
        pass

    @abstractmethod
    def getMinMaxRawDistance(self) -> Tuple[int, int]:
        """
        Gets the minimum and maximum raw distance in the matrix.  
        This information is used to translate the raw distance to a distance in the range [0, 1].
        """
        pass

    @abstractmethod
    def getMatrixSize(self) -> int:
        """
        Gets the size of the matrix.
        """
        pass

    @abstractmethod
    def getRawMatrix(self) -> Iterable[Iterable[int]]:
        """
        Returns the raw matrix as a list of lists.
        NOTE: This can be a very expensive operation for large matrices. May cause memory crashes, if matrix can't fit into memory.
        """
        pass

    def getDistance(self, x: int, y: int) -> float:
        """
        Gets the distance between two objects in the matrix represented by a float in the range [0, 1].
        """
        rawD = self.getRawDistance(x, y)
        minD, maxD = self.getMinMaxRawDistance()
        return (rawD - minD) / (maxD - minD)

    def setDistance(self, x: int, y: int, value: float) -> None:
        """
        Sets the distance between two objects in the matrix represented by a float in the range [0, 1].
        """
        minD, maxD = self.getMinMaxRawDistance()
        self.setRawDistance(x, y, int(value * (maxD - minD) + minD))

    def elements(
            self) -> Iterable[Tuple[int, int, int, Callable[[float], None]]]:
        """
        Returns an iterator over the elements in the matrix.
        """
        t = 0
        for i in range(self.getMatrixSize()):
            for j in range(self.getMatrixSize()):
                yield t, i, j, lambda d: self.setDistance(i, j, d)
                t += 1