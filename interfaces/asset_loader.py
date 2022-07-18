from abc import ABC, abstractmethod
from asset_manager import IAssetManager

class AssetLoader(ABC):
    @abstractmethod
    def loadAssets(self, assetManager: IAssetManager) -> None:
        """
        Loads the assets into the asset manager.
        """
        pass