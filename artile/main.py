from artile.core.data import Tiled


def execute_func(tiles: Tiled, function: callable) -> Tiled:
    for t in tiles:
        t = function(t)
    return tiles
