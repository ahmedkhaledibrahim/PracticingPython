from gc import garbage

from src.real_estate_app.apartment import get_valid_input
from src.real_estate_app.property import Property


class House(Property):
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self,num_stories='',garage='',fenced_yard='',**kwargs):
        super().__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced_yard = fenced_yard

    def display(self):
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced_yard))

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()
        garage = get_valid_input("what garage? ",House.valid_garage)
        fenced = get_valid_input("what fance?",House.valid_fenced)
        num_stories = input("How many stories? ")
        parent_init.update({
            "garage" : garage,
            "fenced" : fenced,
            "num_stories" : num_stories
        })
        return parent_init


house = House.prompt_init()



