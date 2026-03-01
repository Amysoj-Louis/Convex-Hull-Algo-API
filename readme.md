# Convex Hull Geo-Computation API

A specialized Flask-based REST API designed for high-performance computation of the convex hull for sets of geographical coordinates (Latitude/Longitude).

## 🌍 Project Overview
The **Convex Hull Algo API** provides a precise geometric solution for finding the minimum bounding polygon that encloses a set of GPS points. It utilizes **Andrew's Monotone Chain Algorithm**, delivering an efficient O(n log n) time complexity. This utility is ideal for mapping applications, spatial analysis, and geographical fencing where identifying the outer boundaries of a point cluster is required.

## ✨ Key Features
- **Andrew's Monotone Chain Implementation**: Efficient geometric logic for calculating the convex hull, optimized for accuracy and speed.
- **Geographical Point Processing**: Specifically designed to handle (Lat, Lng) tuples for direct integration with mapping libraries.
- **RESTful POST Endpoint**: A simple, robust `/convexhull` endpoint accepting point sequences via form data.
- **Mapping-Ready Output**: Returns structured JSON data suitable for immediate visualization in Leaflet, Google Maps, or MapLibre GL.
- **Collinear Point Handling**: Built-in logic to exclude redundant collinear points, ensuring a minimal bounding polygon.

## 🛠️ Tech Stack
- **Backend**: Python 3.10, Flask
- **Geometric Logic**: Custom implementation of monotone chain algorithm
- **Data Handling**: JSON, Typing
- **Deployment**: Vercel-ready serverless architecture

*“Defining the boundaries of geographical point clusters with mathematical precision.”*
