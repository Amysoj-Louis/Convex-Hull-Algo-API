from typing import List, Sequence, Tuple
from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/convexhull', methods=['POST'])
def index():
    args = request.form
    data = args['latlng']
    # Returns a new list of points representing the convex hull of
    # the given set of points. The convex hull excludes collinear points.
    # This algorithm runs in O(n log n) time.

    def make_hull(points: Sequence[Tuple[float, float]]) -> List[Tuple[float, float]]:
        return make_hull_presorted(sorted(points))

    # Returns the convex hull, assuming that each points[i] <= points[i + 1]. Runs in O(n) time.

    def make_hull_presorted(points: Sequence[Tuple[float, float]]) -> List[Tuple[float, float]]:
        if len(points) <= 1:
            return list(points)

        # Andrew's monotone chain algorithm. Positive y coordinates correspond to "up"
        # as per the mathematical convention, instead of "down" as per the computer
        # graphics convention. This doesn't affect the correctness of the result.
        upperhull: List[Tuple[float, float]] = []
        lowerhull: List[Tuple[float, float]] = []
        for hull in (upperhull, lowerhull):
            for p in (points if (hull is upperhull) else reversed(points)):
                while len(hull) >= 2:
                    qx, qy = hull[-1]
                    rx, ry = hull[-2]
                    if (qx - rx) * (p[1] - ry) >= (qy - ry) * (p[0] - rx):
                        del hull[-1]
                    else:
                        break
                hull.append(p)
            del hull[-1]

        if not (len(upperhull) == 1 and upperhull == lowerhull):
            upperhull.extend(lowerhull)
        return upperhull
    final_points = make_hull(points=[data])
    output = {"data": final_points[0]}
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)
