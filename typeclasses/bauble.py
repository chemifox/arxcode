"""

Placeholder class. Currently identical to regular
objects.
"""
from typeclasses.objects import Object as DefaultObject
from .mixins import ObjectMixins


class Bauble(DefaultObject):
    """
    Essentially a placeolder in case we wanna do anything with it
    later.
    """

    def at_object_creation(self):
        """
        Run at Bauble creation.
        """
        self.db.bauble = True
    pass
