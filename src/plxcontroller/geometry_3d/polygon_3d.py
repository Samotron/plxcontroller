from __future__ import annotations

from copy import copy
from typing import List, Tuple

from skspatial.objects import Points as ScikitSpatialPoints

from plxcontroller.geometry_3d.point_3d import Point3D


class Polygon3D:
    """
    A class with information about a polygon in the 3D space.
    """

    def __init__(self, coordinates: List[Tuple[float, float, float]]):
        """Initializes a Polygon3D instance.

        Parameters
        ----------
        coordinates : List[Tuple[float, float, float]]
            a list of the coordinates of the polygon.

        Raises
        ------
        TypeError
            if coordinates of its (sub)items are not of the expected type.
        ValueError
            - if length of coordinates is not >= 3.
            - if length of any tuple is not exactly 3.
            - if the given coordinates are not coplanar.
        """
        # Validate input
        # coordinates
        if not isinstance(coordinates, list):
            raise TypeError(
                f"Unexpected type for coordinates. Expected list, but got: {type(coordinates)}"
            )
        # coordinate items and subtimes
        for i, coord in enumerate(coordinates):
            if not isinstance(coord, tuple):
                raise TypeError(
                    f"Unexpected type for item of coordinates at index {i}. Expected tuple, but got: {type(coord)}"
                )
            if not len(coord) == 3:
                raise ValueError(
                    f"Unexpected tuple length for item of coordinates at index {i}. Expected tuple length = 3, but got: {len(coord)}"
                )
            if not all(isinstance(a, (float, int)) for a in coord):
                raise TypeError(
                    f"Unexpected type for tuple items of coordinate at index {i}. Expected float, but got: {tuple(isinstance(a, float) for a in coord)}"
                )

        # Validate length of list
        if not len(coordinates) >= 3:
            raise ValueError(
                f"Unexpected length of coordinates. Expected length >= 3, but got: {len(coordinates)}"
            )

        # Validate points are coplanar
        skspatial_points = ScikitSpatialPoints(coordinates)
        if not skspatial_points.are_coplanar():
            raise ValueError(
                "Cannot create Polygon3D, because the given coordinates are not coplanar."
            )

        # Store the coordinates
        self._coordinates = coordinates

    @property
    def coordinates(self) -> List[Tuple[float, float, float]]:
        """Return the coordinates of the polygon a list of (x,y,z) tuples."""
        return copy(self._coordinates)

    @property
    def points(self) -> List[Point3D]:
        """Return the coordinates of the polygon a list of Point3D."""
        return [Point3D(*a) for a in self._coordinates]

    @property
    def scikit_spatial_points(self) -> ScikitSpatialPoints:
        """Return the coordinates of the polygon a skspatial.objects.Points object."""
        return ScikitSpatialPoints(self._coordinates)
