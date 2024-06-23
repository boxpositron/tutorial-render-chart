import secrets
from typing import List, Optional


PLOT_X = 8
PLOT_Y = 8

SCALE_X = 8
SCALE_Y = 3


# Array 0 -> y, Array 1 -> x
Point = List[int]
PlotTable = List[Point]


def render_x_axis(point: Optional[Point] = None) -> None:
    # Plot x axis

    normalized_plot_x = (PLOT_X + 1) * SCALE_X
    if point is None:

        for i in range(normalized_plot_x):
            if i % SCALE_X == 0:
                index = i // SCALE_X
                print(index, end="")
            else:
                print("-", end="")

        return

    for i in range(PLOT_X):
        # Lets scale according to the x axis
        for j in range(SCALE_X):
            if j != 0:
                print(" ", end="")
                continue

            if i == point[1]:
                print(f"⏺ ({point[0]},{point[1]})", end="")
            else:
                print(" ", end="")


def render_y_axis(point: Point, index: int) -> None:

    for item in range(SCALE_Y):
        if (item != 0):
            print("|")
            continue

        print(index, end="")
        for point in point:
            render_x_axis(point)
        print("")

    if index == 1:
        render_x_axis()


def render_plotable_points(plot_table: PlotTable) -> None:
    # Plot y axis

    for i in range(PLOT_Y, 0, -1):

        selected_row = list(filter(lambda x: x[0] == i, plot_table))

        render_y_axis(selected_row, i)


def safe_plotable_point(max: int) -> int:
    return secrets.randbelow(max)


def generate_plotable_points() -> PlotTable:
    plot_table: PlotTable = []

    for i in range(PLOT_Y):
        has_plot = False
        for j in range(PLOT_X):
            should_plot = secrets.randbelow(2)
            if should_plot:
                point = safe_plotable_point(PLOT_X)
                item = [i, point]
                plot_table.append(item)

                has_plot = True
                break

            if j == PLOT_X - 1 and not has_plot:
                # If there is no plot in the row, add a plot
                point = safe_plotable_point(PLOT_X)
                item = [i, point]
                plot_table.append(item)

        has_plot = False

    return plot_table


def main() -> None:
    point = generate_plotable_points()
    render_plotable_points(point)
