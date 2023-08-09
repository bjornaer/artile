# artile

tiling and re-tiling library for image processing and transformation

## Installation

```shell
pip install artile
```

## Usage

```python
import artile as at
def f(img):
    print("do something")

artile_img = at.load("path/to/image")
tile_size = (300, 300)
overlap = (0.1, 0.1)
tiles = dt.get_tiles(tile_size, overlap)
tiles = tiles.pad()
transformed_tiles = at.execute_func(tiles, function=f)
stitched = at.stich_image(transformed_tiles)
```

based off [DeepTile](https://pypi.org/project/DeepTile/)
