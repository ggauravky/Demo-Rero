from abc import ABC, abstractmethod

# Abstract Class
class SmartDevice(ABC):
    def __init__(self, name):
        self._name = name
        self.__is_on = False  # Private attribute

    @abstractmethod
    def operate(self):
        pass

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def show_status(self):
        status = "ON" if self.__is_on else "OFF"
        print(f"{self._name} is {status}")

    # Encapsulated Getter for is_on
    def is_device_on(self):
        return self.__is_on


# SmartLight Class
class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__brightness = 70  # Default brightness level

    def operate(self):
        self.turn_on()
        print(f"{self._name} light turned ON with brightness at {self.__brightness}%.")

    # Encapsulated Getters/Setters
    def get_brightness(self):
        return self.__brightness

    def set_brightness(self, brightness):
        if 0 <= brightness <= 100:
            self.__brightness = brightness
        else:
            print("Invalid brightness level.")


# SmartFan Class
class SmartFan(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__speed = "Medium"

    def operate(self):
        self.turn_on()
        print(f"{self._name} fan turned ON at {self.__speed} speed.")

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        if speed in ["Low", "Medium", "High"]:
            self.__speed = speed
        else:
            print("Invalid speed option.")


# SmartAC Class
class SmartAC(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__temperature = 24

    def operate(self):
        self.turn_on()
        print(f"{self._name} AC turned ON at {self.__temperature}°C.")

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, temp):
        if 16 <= temp <= 30:
            self.__temperature = temp
        else:
            print("Invalid temperature setting.")


# Demonstration
if __name__ == "__main__":
    # Create objects
    light = SmartLight("Living Room")
    fan = SmartFan("Bedroom")
    ac = SmartAC("Office")

    # Call operate and show_status
    light.operate()
    light.show_status()

    fan.operate()
    fan.show_status()

    ac.operate()
    ac.show_status()

    print("\nAttempting direct access to private attribute:")
    try:
        print(light.__brightness)  # Should raise an AttributeError
    except AttributeError:
        print("Cannot access private attribute directly!")

    # Modify using setters
    print("\nUpdating settings using setters:")
    light.set_brightness(85)
    print("Updated Brightness:", light.get_brightness())

    fan.set_speed("High")
    print("Updated Speed:", fan.get_speed())

    ac.set_temperature(22)
    print("Updated Temperature:", ac.get_temperature())
