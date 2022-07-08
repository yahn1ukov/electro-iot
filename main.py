import sys
import time

import requests

from Car import Car


class IoT:
    @staticmethod
    def get_current_car_info():
        return Car("3VWLL7AJ9BM053541", 50000, 50.12345, 110.12345, "J-123", "Nissan", "Leaf", 51)

    @staticmethod
    def add_car():
        print("\n==== Checking for the presence of an electric vehicle in the system... ====")
        time.sleep(2)
        car = requests.get("http://localhost:8080/api/v1/cars/vin-codes/" + IoT.get_current_car_info().get_vin_code())
        if car.status_code == 200:
            print("==== The electric car has been found. Updating data... ====")
            time.sleep(2)
            requests.patch(
                "http://localhost:8080/api/v1/cars/vin-codes/" + IoT.get_current_car_info().get_vin_code() + "/update",
                json={
                    "latitude": IoT.get_current_car_info().get_latitude(),
                    "longitude": IoT.get_current_car_info().get_longitude(),
                    "percentageOfCharge": IoT.get_current_car_info().get_percentage_of_charge()
                }
            )
            print("==== Data updated ====\n")
        else:
            print("==== Electric vehicle not found. Added to the system... ====")
            time.sleep(2)
            requests.post(
                "http://localhost:8080/api/v1/cars/create",
                json={
                    "name": IoT.get_current_car_info().get_name(),
                    "model": IoT.get_current_car_info().get_model(),
                    "vinCode": IoT.get_current_car_info().get_vin_code(),
                    "mileage": IoT.get_current_car_info().get_mileage(),
                    "typeConnector": IoT.get_current_car_info().get_type_connector(),
                    "percentageOfCharge": IoT.get_current_car_info().get_percentage_of_charge(),
                    "latitude": IoT.get_current_car_info().get_latitude(),
                    "longitude": IoT.get_current_car_info().get_longitude()
                }
            )
            print("==== Electric vehicle added ====\n")

    @staticmethod
    def update_car():
        print("\n==== Updating data... ====")
        time.sleep(2)
        requests.patch(
            "http://localhost:8080/api/v1/cars/vin-codes/" + IoT.get_current_car_info().get_vin_code() + "/update",
            json={
                "percentageOfCharge": IoT.get_current_car_info().get_percentage_of_charge(),
                "latitude": IoT.get_current_car_info().get_latitude(),
                "longitude": IoT.get_current_car_info().get_longitude()
            }
        )
        print("==== Data updated ====\n")

    @staticmethod
    def get_charger_stations():
        if IoT.get_current_car_info().get_percentage_of_charge() > 50:
            return
        charger_stations = requests.get(
            "http://localhost:8080/api/v1/cars/vin-codes/" + IoT.get_current_car_info().get_vin_code() + "/chargers") \
            .json()
        print(charger_stations)

    @staticmethod
    def get_service_stations():
        service_stations = requests.get(
            "http://localhost:8080/api/v1/cars/vin-codes/" + IoT.get_current_car_info().get_vin_code() + "/stations") \
            .json()
        print(service_stations)

    @staticmethod
    def print_menu():
        print("========================\n"
              "Select an option:\n"
              "1. Add car to database\n"
              "2. Update data about car\n"
              "3. Get the nearest charging stations\n"
              "4. Get the nearest service stations\n"
              "5. Exit\n"
              "========================")

    @staticmethod
    def menu():
        while True:
            IoT.print_menu()
            option = input("Please make a choice >> ")

            if option == "1":
                IoT.add_car()
            elif option == "2":
                IoT.update_car()
            elif option == "3":
                IoT.get_charger_stations()
            elif option == "4":
                IoT.get_service_stations()
            elif option == "5":
                sys.exit()
            else:
                print("\n==== Wrong number ====\n")


def main():
    IoT.menu()


if __name__ == '__main__':
    main()
