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
transformed_tiles = at.execute_func(artile_img, function=f)
stitched = at.stich_image(transformed_tiles)
```

based off [DeepTile](https://pypi.org/project/DeepTile/)
