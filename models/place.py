#!/usr/bin/python3
"""Module for Place class."""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class representing a Place."""
    city_id = ""
    user_id = ""
    name = ""
