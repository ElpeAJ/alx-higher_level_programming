#!/usr/bin/python3
""" This module defines the Rectangle class """
from .base import Base


class Rectangle(Base):
    """ Represent the rectangle shape """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize an instance of rectangle

        Parameters
        width : integer
        height : integer
        x : integer, optional
        y : interger, optional
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

