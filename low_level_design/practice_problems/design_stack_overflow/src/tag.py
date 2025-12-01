"""Tag- implementation : this will contain type of tag on stackoverflow"""

class Tag:
    def __init__(self, tag_name: str):
        self.tag_name=tag_name

    def get_tag_name(self)-> str:
        return self.tag_name