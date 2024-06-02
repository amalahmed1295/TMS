# TMS
A simple Traffic Management System project which applies some design patterns.
The Traffic Management System (TMS) is a sophisticated software solution designed to enhance traffic control and monitoring within smart city infrastructures. This document provides an overview of the TMS architecture, highlighting the key design patterns employed to ensure efficiency, scalability, and maintainability.

The design patterns used in the project in a way to make its readability and implementation better is as follows:
1. Singleton Pattern
It Ensures that there exists only one instance of the Traffic Management Center (TMC) throughout the system, maintaining a single point of control and coordination.
2. Observer Pattern
Facilitates communication between traffic sensors and the TMC, allowing for real-time data updates and event notifications.
3.Mediator Pattern
Decouples the interaction between sensors and traffic lights, enabling centralized traffic management and coordination.
4.Command Pattern
Encapsulates requests to change traffic light states, promoting modularity and ease of state management.
5.Facade Pattern
Provide a simplified interface for interacting with the complex subsystems of the TMS.

The components of the Traffic Management System can be explained as follows:	
1. Traffic Sensor(ConcreteTrafficSensor class): Represents a sensor deployed at various locations to detect traffic conditions. It updates the TMC with traffic information.
2. Traffic Management Center(TrafficManagementCenter class): Centralized control center responsible for managing traffic flow and handling violations. It Registers sensors, manage traffic lights, and handle traffic events.
3. Traffic Light(TrafficLight class.): Represents a traffic light at an intersection. It changes state based on traffic events.
4. Violation Manager(ViolationManager class): Manages recorded traffic violations. It add and display violations.
