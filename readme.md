# Convex Hull API

This repository provides a Flask-based API that calculates the convex hull for a given set of geographical coordinates (latitude and longitude). The convex hull represents the smallest polygon that can enclose all the points in the set, excluding collinear points.

## Overview

The API implements Andrew's monotone chain algorithm to compute the convex hull of a given set of points.

## Features

- **Fast and Efficient**: Utilizes Andrew's monotone chain algorithm for optimal performance.
- **REST API**: Easy-to-use API endpoint to integrate into your applications.
- **JSON Response**: Returns the convex hull coordinates in JSON format.

## Requirements

- **Python 3.7+**
- **Flask**

## API Usage

### Endpoint

**POST /convexhull**

### Request Parameters

- `latlng`: A sequence of latitude and longitude pairs. This should be provided in the form data of the POST request.

### Example Request

```bash
curl -X POST -F "latlng=34.05,-118.25 36.16,-115.15 37.77,-122.42 34.05,-118.25" http://127.0.0.1:5000/convexhull
```

### Example Response

```json
{
  "data": [
    [34.05, -118.25],
    [36.16, -115.15],
    [37.77, -122.42]
  ]
}
```

### Explanation

- The input is a list of geographical coordinates (latitude, longitude) that you wish to compute the convex hull for.
- The output is a list of coordinates that represent the convex hull, forming the smallest polygon enclosing all input points.

## Algorithm Details

The convex hull algorithm employed in this API is Andrew's monotone chain algorithm. It sorts the points by x-coordinates (and by y-coordinates if x-coordinates are identical) and then constructs the upper and lower hulls of the convex hull. The algorithm efficiently removes collinear points, ensuring that the output polygon is minimal. The algorithm used was developed by [Project Nayuki](https://www.nayuki.io/page/convex-hull-algorithm).

## Limitations
- The input format expects coordinates as a single string in the request form data, which needs to be parsed correctly on the client-side.
