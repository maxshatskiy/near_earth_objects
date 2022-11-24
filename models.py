"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str
from typing import Union


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(
            self,
            designation: str,
            name: str = None,
            diameter: float = float('nan'),
            hazardous: bool = False,
            **info):
        """Create a new `NearEarthObject`.
        :param designation: a string. represents primary designation.
        :param name: a string. represents name.
        :param diameter: a flot. represents diameter of the object.
        :param hazardous: a boolean. represents if the object is hazardous to Earth or not.
        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """

        self.designation = designation
        self.name = name
        self.diameter = diameter
        self.hazardous = hazardous
        self.info = info
        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        self.fullname = self.designation + '_' + self.name

        return self.fullname

    def __str__(self):
        """Return `str(self)`."""

        return f"A NearEarthObject named {self.name!s} with a diameter={self.diameter:.3f} moves "\
               f"to {self.designation!s} and is {'hazardous.' if self.hazardous else 'not hazardous.'}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self,
                 time,
                 distance: Union[float,
                                 int] = 0.0,
                 velocity: Union[float,
                                 int] = 0.0,
                 designation: str = None,
                 neo: type(NearEarthObject) = None,
                 **info):
        """Create a new `CloseApproach`.
        :param time: The date and time, in UTC, at which the NEO passes closest to Earth. For example,
                     December 31st, 2020 at noon is: 2020-Dec-31 12:00
        :param distance: The nominal approach distance, in astronomical units, of the NEO to Earth at the closest point.
        :param velocity: The velocity, in kilometers per second, of the NEO relative to Earth at the closest point.
        :param neo: The NearEarthObject that is making a close approach to Earth.
        :param info: A dictionary of excess keyword arguments supplied to the constructor.

        """
        self._designation = designation
        self.time = cd_to_datetime(time)
        self.distance = distance
        self.velocity = velocity
        self.info = info
        self.neo = neo

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return f"A CloseApproach with designation '{self._designation}' approaches Earth at a " \
               f"distance of {self.distance:.2f} au and a velocity " \
               f"of {self.velocity:.2f} km/s at {self.time_str} UTC."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
