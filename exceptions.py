from common.interfaces.assest_manager import IAssetManager, IAsset
class AssetAppendException(Exception):
    """
    Exception raised when an asset cannot be appended to the asset manager.
    """
    asset: IAsset
    assetManager: IAssetManager
    id: int

    def __init__(self, asset: IAsset, assetManager: IAssetManager, id: int, message: str):
        super().__init__(message)
        self.asset = asset
        self.assetManager = assetManager
        self.id = id