from abc import ABC, abstractmethod

class IAsset(ABC):
    sequence: str
    name: str

class IAssetManager(ABC):
    @abstractmethod
    def getAsset(self, assetIndex: int) -> IAsset:
        """
        Gets the asset with the given id.
        """
        pass
    @abstractmethod
    def getAssetCount(self) -> int:
        """
        Gets the number of assets.
        """
        pass
    @abstractmethod
    def setAsset(self, assetIndex: int, asset: IAsset) -> None:
        """
        Sets the asset with the given id.
        """
        pass