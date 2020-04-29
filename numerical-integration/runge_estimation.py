def partition(points):
    partitioned_points = []
    for i in range(1, len(points)):
        mid = (points[i] + points[i - 1]) / 2

        partitioned_points.extend([points[i - 1], mid, points[i]])

    return partitioned_points


def calculate_grid(integral, points, a, b, eps):
    result_grid = []

    for i in range(1, len(points)):
        h = points[i] - points[i - 1]
        borders = [points[i - 1], points[i]]

        partitioned = borders
        partitioned_estimation = partition(borders)

        integrated_segment = integral(borders)

        while True:
            integrated_partition = integral(partitioned_estimation)

            if abs(integrated_segment - integrated_partition) <= (eps * h) / (b - a):
                break
            else:
                partitioned = partitioned_estimation
                partitioned_estimation = partition(partitioned_estimation)

                integrated_segment = integrated_partition

        if len(result_grid) > 0:
            partitioned = partitioned[1:]

        result_grid.extend(partitioned)

    return result_grid


