class Car:
    def __init__(self,make,model,year,color):
        self._make = make
        self._model = model
        self._year = year
        self._color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

    def accelerate(self,value):
        if not self.started:
            print("Car is not started yet....")
            return

        if self.speed + value < self.max_speed:
            self.speed += value

        print(f"Accelerating to the {self.speed}km/hrs...")


    def brake(self,value):
        if not self.started:
            print("Car is already stopped...")
            return

        if self.speed + value > 0:
            self.speed -= value

        print(f"Deaccelerating car with: {self.speed} km/hrs.")