from __future__ import annotations


class Point3D:
    """
    A class with information about a point in the 3D space.
    """

    def __init__(self, x: float, y: float, z: float) -> None:
        """Initializes a Point3D instance.

        Parameters
        ----------
        x : float
            the x coordinate of the point.
        y : float
            the y coordinate of the point.
        z : float
            the z coordinate of the point.

        Raises
        ------
        TypeError
            if any parameter is not of the expected type.
        """
        # Validate types
        if not isinstance(x, (float, int)):
            raise TypeError(
                f"Unexpected type found for x. Expected float, but got {type(x)}"
            )
        if not isinstance(y, (float, int)):
            raise TypeError(
                f"Unexpected type found for y. Expected float, but got {type(y)}"
            )
        if not isinstance(z, (float, int)):
            raise TypeError(
                f"Unexpected type found for z. Expected float, but got {type(z)}"
            )

        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self) -> float:
        """Returns the x coordinate of the point."""
        return self._x

    @property
    def y(self) -> float:
        """Returns the y coordinate of the point."""
        return self._y

    @property
    def z(self) -> float:
        """Returns the z coordinate of the point."""
        return self._z
