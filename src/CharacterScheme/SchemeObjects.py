# Object representing a name, containing its representation used in DTW
class Representation:
    def __init__(self, name, representation):
        self.name = name
        self.representation = representation
        self.pic = None


class Character:
    def __init__(self, orth, type):
        self.orth = orth                # str - orthography
        self.properties = set()         # set {property_tag} - used for defining classes etc. for the char
        self.type = type
