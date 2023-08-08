from pathlib import Path

from dask.array import Array
from numpy import ndarray

from artile import tile


def load(image, dask=True, link_data=True):
    """Load image into a ArTile object.

    Parameters
    ----------
        image
            An object or path of an image.
        dask : bool, optional, default True
            Whether to use Dask for lazy loading and processing.
        link_data : bool, optional, default True
            Whether to link input and output data to the profile and job objects. Set to ``False`` to reduce memory
            usage.

    Returns
    -------
        at : ArTile
            ArTile object.

    Raises
    ------
        ValueError
            If ``image`` has an unsupported file type.
        ValueError
            If ``image`` is invalid.
    """

    if isinstance(image, Array):
        dask = True
        at = from_array(image, dask)
    elif isinstance(image, ndarray):
        at = from_array(image, dask)
    elif Path(image).is_file():
        if image.endswith((".tif", ".tiff")):
            at = from_tiff(image, dask)
        elif image.endswith(".nd2"):
            at = from_nd2(image)
        else:
            raise ValueError("unsupported file type.")
    else:
        raise ValueError("invalid image.")

    at.dask = dask
    at.link_data = link_data

    return at


def from_array(image, dask):
    """Create a ArTileArray object from an array.

    Parameters
    ----------
        image : array_like
            An array-like object of an image.
        dask : bool, optional, default True
            Whether to use Dask for lazy loading and processing.

    Returns
    -------
        at : ArTileArray
            ArTileArray object.
    """

    from artile.sources import array

    image = array.read(image, dask)
    at = tile.ArTileArray(image)

    return at


def from_large_image(image):
    """Create a ArTileLargeImage object from a large_image tile source.

    Parameters
    ----------
        image : large_image tile source
            A large_image tile source.

    Returns
    -------
        at : ArTileLargeImage
            ArTileLargeImage object.
    """

    at = tile.ArTileLargeImage(image)

    return at


def from_nd2(image):
    """Create a ArTileND2 object from an ND2 file.

    Parameters
    ----------
        image : str
            Path to an ND2 file.

    Returns
    -------
        at : ArTileND2
            ArTileND2 object.
    """

    from artile.sources import nd2

    image_sizes, axes_order = nd2.read(image)
    at = tile.ArTileND2(image)
    at.axis_sizes = image_sizes
    at.axis_order = axes_order

    return at


def from_tiff(image, dask):
    """Create a ArTileArray object from a TIFF file.

    Parameters
    ----------
        image : str
            Path to a TIFF file.
        dask : bool, optional, default True
            Whether to use Dask for lazy loading and processing.

    Returns
    -------
        at : ArTileArray
            ArTileArray object.
    """

    from artile.sources import tiff

    image = tiff.read(image, dask)
    at = tile.ArTileArray(image)

    return at
