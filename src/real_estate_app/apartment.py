from src.real_estate_app.property import Property


class Apartment(Property):
    valid_laundries = ("coin","ensuite","none")
    valid_balconies = ("yes","no","solarium")

    def __init__(self,balcony='',laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()

        laundry = get_valid_input("what laundry? ",Apartment.valid_laundries)
        balcony = get_valid_input("what balcony? ",Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init


def get_valid_input(message_string,valid_options):
    message_string += "  ({})  ".format(", ".join(valid_options))
    response = input(message_string)
    while response not in valid_options:
        response = input(message_string)
    return response
