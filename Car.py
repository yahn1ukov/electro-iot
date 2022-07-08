class Car:
    __vin_code = ""
    __mileage = 0
    __latitude = 0
    __longitude = 0
    __type_connector = ""
    __name = ""
    __model = ""
    __percentage_of_charge = 0

    def __init__(self, vin_code, mileage, latitude, longitude, type_connector, name, model, percentage_of_charge):
        self.__vin_code = vin_code
        self.__mileage = mileage
        self.__latitude = latitude
        self.__longitude = longitude
        self.__type_connector = type_connector
        self.__name = name
        self.__model = model
        self.__percentage_of_charge = percentage_of_charge

    def get_vin_code(self):
        return self.__vin_code

    def set_vin_code(self, value):
        self.__vin_code = value

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, value):
        self.__mileage = value

    def get_latitude(self):
        return self.__latitude

    def set_latitude(self, value):
        self.__latitude = value

    def get_longitude(self):
        return self.__longitude

    def set_longitude(self, value):
        self.__longitude = value

    def get_type_connector(self):
        return self.__type_connector

    def set_type_connector(self, value):
        self.__type_connector = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_model(self):
        return self.__model

    def set_model(self, value):
        self.__model = value

    def get_percentage_of_charge(self):
        return self.__percentage_of_charge

    def set_percentage_of_charge(self, value):
        self.__percentage_of_charge = value

    def __str__(self):
        return 'Car(' \
               'vin_code=' + str(self.get_vin_code()) + \
               ', mileage=' + str(self.get_mileage()) + \
               ', latitude=' + str(self.get_latitude()) + \
               ', longitude=' + str(self.get_longitude()) + \
               ', type_connector=' + self.get_type_connector() + \
               ', name=' + self.get_name() + \
               ', model=' + self.get_model() + \
               ', percentage_of_charge=' + str(self.get_percentage_of_charge()) + \
               ')'
