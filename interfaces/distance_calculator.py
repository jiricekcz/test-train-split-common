from abc import ABC, abstractmethod
from common.interfaces.assest_manager import IAssetManager
from common.interfaces.distance_matrix import IDistanceMatrix
from typing import Callable
class IDistanceCalculator(ABC):
    @abstractmethod
    def calculateDistances(self, distances: IDistanceMatrix, assets: IAssetManager, statusReport: Callable[[int, int, float], None] = (lambda stepsDone, totalSteps, percetage: None)) -> None:
        """
        Calculates the distances between all assets and stores them in the given distance matrix.
        The statusReport function is called when progress changes significantly, and can be used to show a progress bar. Parameters are:
        stepsDone: int - The number of steps done so far.
        totalSteps: int - The total number of steps to be done.
        percentage: float - The percentage of the distance matrix that has been calculated.
        WARN: The function can be called multiple times with the same values.
        """
        pass