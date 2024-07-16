import secrets
from typing import List, Optional

PLOT_X = 8
PLOT_Y = 8

SCALE_X = 8
SCALE_Y = 4

RENDER_CHARACTER = "⏺"

# Array 0 -> y, Array 1 -> x
Point = int
Cordinate = List[Point]
PlotTable = List[Cordinate]


def render_x_axis(coordinates: Optional[Cordinate] = None, is_base: bool = False) -> None:
    # Plot x axis

    x_point = coordinates[1] if coordinates is not None else -1
    y_point = coordinates[0] if coordinates is not None else -1

    rendered_point = f"{RENDER_CHARACTER}({x_point},{y_point})"
    total_rendered_characters = len(rendered_point) - 1

    for i in range(PLOT_X):
        # Lets scale according to the x axis
        is_rendered_on_base_line: bool = i == x_point and y_point == 0
        for j in range(SCALE_X):
            if j != 0:
                if is_base:
                    if not is_rendered_on_base_line:
                        print("-", end="")
                    else:
                        # TODO: Factor for character rendering when deciding replacements
                        # for the fill character
                        should_render = j > total_rendered_characters

                        if should_render:
                            print("-", end="")
                else:
                    print(" ", end="")
                continue

            if i == x_point:
                print(rendered_point, end="")

            else:
                if is_base:
                    print(i, end="")
                else:
                    print(" ", end="")


def render_y_axis(coordinates: Cordinate) -> None:

    y_point = coordinates[0]

    for item in range(SCALE_Y):
        if (item != 0):
            print("|")
            continue

        print(y_point, end="")
        if y_point == 0:
            print(",", end="")
        render_x_axis(coordinates, is_base=y_point == 0)
        print("", end="\n")


def render_plotable_points(plot_table: PlotTable) -> None:
    # Plot y axis

    for point in range(PLOT_Y, 0, -1):

        coordinates = plot_table[point - 1]

        render_y_axis(coordinates)


def safe_plotable_point(max: int) -> int:
    return secrets.randbelow(max)


def generate_plotable_points() -> PlotTable:
    plot_table: PlotTable = []

    for i in range(PLOT_Y):
        has_plot = False
        for j in range(PLOT_X):
            should_plot = secrets.randbelow(2)
            if should_plot:
                cordinates = safe_plotable_point(PLOT_X)
                item = [i, cordinates]
                plot_table.append(item)

                has_plot = True
                break

            if j == PLOT_X - 1 and not has_plot:
                # If there is no plot in the row, add a plot
                cordinates = safe_plotable_point(PLOT_X)
                item = [i, cordinates]
                plot_table.append(item)

        has_plot = False

    return plot_table


def main() -> None:
    cordinates = generate_plotable_points()
    render_plotable_points(cordinates)


if __name__ == "__main__":
    main()
