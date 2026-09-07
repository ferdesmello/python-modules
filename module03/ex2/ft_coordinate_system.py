import math

def get_player_pos() -> tuple[float, float, float]:

    coord_str: list[str] = []
    coord_float: list[float] = []
    while not coord_float:
        input_str: str = input("Enter new coordinates as floats "
                               "in format 'x,y,z': ")
        coord_str = input_str.split(",")
        try:
           coord_str = input_str.split(",")
           if calc_size(coord_str) != 3:
               raise IndexError
           for coordinate in coord_str:
               coord_float.append(float(coordinate))
           return (coord_float[0], coord_float[1], coord_float[2])

        except IndexError:
            print(f"Invalid syntax")
            coord_str.clear()
            coord_float.clear()

        except ValueError:
            print(f"Error on parameter "
                  f"'{coord_str[calc_size(coord_float)]}': "
                  f"could not convert string to float: "
                  f"'{coord_str[calc_size(coord_float)]}'")
            coord_str.clear()
            coord_float.clear()


def calc_size(coord_list: list[float]) -> float:
    size = 0
    for _ in coord_list:
        size +=1;
    return size


def calc_distance(x1: float, 
                  y1: float, 
                  z1: float, 
                  x2: float,
                  y2: float,
                  z2: float) -> float:
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    x1, y1, z1 = get_player_pos()
    print(f"Got a first tuple: {(x1, y1, z1)}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance = calc_distance(0, 0, 0, x1, y1, z1)
    print(f"Distance to center: {round(distance, 4)}\n")

    print("Get a second set of coordinates")
    x2, y2, z2 = get_player_pos()
    print(f"Got a second tuple: {(x2, y2, z2)}")
    print(f"It includes: X={x2}, Y={y2}, Z={z2}")
    distance = calc_distance(x1, y1, z1, x2, y2, z2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(distance, 4)}")


if __name__ == "__main__":
    main()
