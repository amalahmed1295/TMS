import time
import random
from abc import ABC, ABCMeta, abstractmethod
import tkinter as tk
from tkinter import messagebox

# Unique Singleton Meta Implementation
class UniqueSingletonMeta(type):
    _unique_instances = {}  # Ensure this is a dictionary
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._unique_instances:
            cls._unique_instances[cls] = super().__call__(*args, **kwargs)
        return cls._unique_instances[cls]

# Combine UniqueSingletonMeta with ABCMeta
class UniqueSingletonABCMeta(UniqueSingletonMeta, ABCMeta):
    pass

# Observer Pattern Implementation (abstract class)
class TrafficSensor(ABC):
    # Abstract method for receiving updates
    @abstractmethod
    def receive_update(self, traffic_info):
        pass

# Concrete Class
class ConcreteTrafficSensor(TrafficSensor):
    def __init__(self, location):
        # Location of the sensor
        self.location = location
        # Placeholder for traffic data
        self.traffic_info = None

    # Update traffic data
    def receive_update(self, traffic_info):
        self.traffic_info = traffic_info
        print(f"Sensor at {self.location} updated with data: {self.traffic_info}")

# Mediator Pattern Implementation
class TrafficMediator(ABC):
    # Abstract method for notifying about events
    @abstractmethod
    def notify(self, sender, event):
        pass

class TrafficManagementCenter(TrafficMediator):
    def __init__(self):
        # List to hold sensors
        self.sensor_units = list()
        # List to hold traffic lights
        self.lights = list()
        # Initialize the violation manager
        self.violation_manager = ViolationManager()
    
    def register_sensor(self, sensor):
        # Add sensor to list
        self.sensor_units.append(sensor)
    
    def add_light(self, light):
        # Add light to list
        self.lights.append(light)

    # Notify all traffic signals about the occurrence
    def notify(self, sender, event):
        if isinstance(sender, TrafficSensor):
            print(f"Sensor at {sender.location} detected event: {event}")
            # Process event and notify relevant lights
            for light in self.lights:
                light.handle_event(event)

# Traffic Violation Manager
class ViolationManager:
    def __init__(self):
        self.violations = []

    def add_violation(self, vehicle, violation_type):
        violation = TrafficViolation(vehicle, violation_type)
        self.violations.append(violation)
        print(f"Violation recorded: Vehicle {vehicle} committed {violation_type}")

    def display_violations(self):
        if self.violations:
            print("\n-- Recorded Violations --")
            for i, violation in enumerate(self.violations, start=1):
                print(f"{i}. Vehicle {violation.vehicle} committed {violation.violation_type}")
        else:
            print("\nNo violations recorded.")

class TrafficLight:
    def __init__(self, location):
        # Location of the light
        self.location = location
        # Initial state of the light
        self.state = "RED"
    
    # Change the state of the light
    def update_state(self, new_state):
        self.state = new_state
        print(f"Traffic light at {self.location} changed to {self.state}")

    # Change light state based on traffic occurrence
    def handle_event(self, event):
        # Example handling based on event
        if event == "Heavy Traffic":
            self.update_state("RED")
        elif event == "Moderate Traffic":
            self.update_state("YELLOW")
        else:
            self.update_state("GREEN")

class TrafficViolation:
    def __init__(self, vehicle, violation_type):
        self.vehicle = vehicle
        self.violation_type = violation_type

# Command Pattern Implementation
class UpdateLightCommand:
    def __init__(self, light, new_state):
        # Traffic light to be controlled
        self.light = light
        # Desired new state
        self.new_state = new_state
    
    # Execute command to change state
    def execute(self):
        self.light.update_state(self.new_state)

# Facade Pattern Implementation
class TrafficSystemFacade:
    def __init__(self):
        # Singleton Traffic management Center
        self.tms = SingletonTrafficManagementCenter()

    # Create new sensor and add it to the system
    def register_sensor(self, location):
        # Create a new sensor
        sensor = ConcreteTrafficSensor(location)
        # Register the sensor
        self.tms.register_sensor(sensor)
        return sensor

    # Create new traffic lights and register it to the system
    def add_traffic_light(self, location):
        # Create a new traffic light
        light = TrafficLight(location)
        # Register the light
        self.tms.add_light(light)
        return light

    # Method to update the traffic information
    def update_traffic_info(self, sensor, data):
        # Update sensor with new traffic info
        sensor.receive_update(data)
        # Notify the control center
        self.tms.notify(sensor, data)
    
    # Method to report a traffic violation
    def report_violation(self, vehicle, violation_type):
        self.tms.violation_manager.add_violation(vehicle, violation_type)

# Singleton Pattern Implementation with Combined Metaclass
class SingletonTrafficManagementCenter(TrafficManagementCenter, metaclass=UniqueSingletonABCMeta):
    pass

# Simulation function for the tms system
def simulate_traffic_system():
    # Using the Interface to interact with the system
    traffic_system = TrafficSystemFacade()
    # Register sensors
    sensor1 = traffic_system.register_sensor("Main Street")
    sensor2 = traffic_system.register_sensor("Second Avenue")
    
    # Register traffic lights
    light1 = traffic_system.add_traffic_light("Main St & First Ave")
    light2 = traffic_system.add_traffic_light("Main St & Second Ave")

    # Simulating traffic updates
    traffic_events = ["Heavy Traffic", "Moderate Traffic", "Light Traffic"]
    violation_types = ["Speeding", "Running Red Light", "Illegal Turn"]
    
    # Simulate 10 traffic updates
    for _ in range(10):
        event1 = random.choice(traffic_events)
        event2 = random.choice(traffic_events)
        
        # Update information of the tms (updating sensors)
        traffic_system.update_traffic_info(sensor1, event1)
        traffic_system.update_traffic_info(sensor2, event2)
        
        # Randomly generate and report a traffic violation
        if random.random() > 0.7:  # 30% chance of a violation
            vehicle_id = f"Vehicle_{random.randint(100, 999)}"
            violation_type = random.choice(violation_types)
            traffic_system.report_violation(vehicle_id, violation_type)
        
        time.sleep(1)  # Wait 1 second between updates
    
    # Change traffic light state directly
    notify_light_command = UpdateLightCommand(light1, "GREEN")  # Create command to change light state
    notify_light_command.execute()  # Execute the command
    
    # Ensure singleton Traffic management Center
    singleton_tms1 = SingletonTrafficManagementCenter()  # first instance of the singleton
    singleton_tms2 = SingletonTrafficManagementCenter()  # Second instance of the singleton
    print(singleton_tms1 is singleton_tms2)  # Should print True, confirming singleton behavior

    # Display recorded violations
    singleton_tms1.violation_manager.display_violations()

# Run simulation
simulate_traffic_system()
