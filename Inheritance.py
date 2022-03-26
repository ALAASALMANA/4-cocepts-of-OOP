#inheritance

class Brands:  # parent_class
    brand_name_1 = "Gucci"
    brand_name_2 = "Cartier"
    brand_name_3 = "Nike"


class Products(Brands):  # child_class
    prod_1 = "Italian luxury brand of fashion, "
    prod_2 = "French luxury goods conglomerate that designs, manufactures, distributes, and sells jewelry and watches, "
    prod_3 = "American multinational corporation engaged in designing, manufacturing, and marketing footwear, "



class Popularity(Products):  # grand_child_class
    prod_1_popularity = "1 of the "
    prod_2_popularity = "27 of the "
    prod_3_popularity = "3 of the "


obj_1 = Popularity()  # Object_creation
print(obj_1.brand_name_1 + " is an " + obj_1.prod_1 + str(obj_1.prod_1_popularity) + " BEST Fashion from 30 Brands In 2022 ")
print(obj_1.brand_name_2 + " is a " + obj_1.prod_2 + str(obj_1.prod_2_popularity) + " BEST Fashion from 30 Brands In 2022 ")
print(obj_1.brand_name_3 + " is an " + obj_1.prod_3 + str(obj_1.prod_3_popularity)+ " BEST Fashion from 30 Brands In 2022 ")