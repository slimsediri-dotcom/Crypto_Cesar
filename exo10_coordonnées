coord_a = { 
    "x": 45,
    "y": 32
 }

coord_b = { 
    "x": 54,
    "y": 28
 }


# def get_highest(coords: list[dict]) -> dict:
#     highest = {
#         "x": 0,
#         "y": 0,
#     }

#     for coord in coords:
#         if coord["y"] > highest["y"]:
#             highest = coord
    
#     return highest

def get_highest(coord_a: dict, coord_b: dict) -> dict:
    if coord_a["y"] > coord_b["y"]:
        return coord_a

    return coord_b


def get_farthest(coord_a: dict, coord_b: dict) -> dict:
    if coord_a["x"] > coord_b["x"]:
        return coord_a

    return coord_b

def get_mid(coord_a: dict, coord_b: dict) -> dict:
    return {
        "x": (coord_a["x"] + coord_b["x"]) / 2,
        "y": (coord_a["y"] + coord_b["y"]) / 2
    }

print(get_mid(coord_a, coord_b))