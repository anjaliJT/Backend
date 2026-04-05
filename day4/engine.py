from abc import ABC , abstractmethod

class Engine(ABC):
    @abstractmethod
    def move_forward(self):
        pass
    @abstractmethod   
    def stop(self):
        pass


class Electric_engine(Engine):
    def move_forward(self):
        print("Electric engine moved forward")

    def stop(self):
        print("Electric Engine Stoped")
    

class Petrol_engine(Engine):
    def move_forward(self):
        print("Petrol engine moved forward")
    
    def stop(self):
        print("Petrol Engine Stoped")

class Diesel_engine(Engine):
    def move_forward(self):
        print("Diesel engine moved forward")
    
    def stop(self):
        print("Diesel Engine Stoped")

class Engine_handler:
    def move_forward(engine:Engine):
        engine.move_forward()
    
    def stop(engine:Engine):
        engine.stop()

electric_engine = Electric_engine()
petrol_engine = Petrol_engine()
diesel_engine = Diesel_engine()

engine_handler = Engine_handler
engine_handler.move_forward(electric_engine)
engine_handler.stop(electric_engine)
engine_handler.move_forward(petrol_engine)
engine_handler.stop(petrol_engine)
engine_handler.move_forward(diesel_engine)
engine_handler.stop(diesel_engine)




