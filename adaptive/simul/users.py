
from adaptive.interface.constants.user_attributes.constants import Gender

class User:
    """
    User

    attributes:
        uid                 int
        gender_private      int
        gender_public       int
        age_private         int
        age_public          int
    """
    def __init__(self):
        self.name = ""
        self.uid = None

        self.gender_private = Gender.UNKNOWN
        self.gender_public = Gender.UNKNOWN

        self.age_private = 0
        self.age_public = 0
