"""
INTERSERVICE COMMUNICATIONS:
                            Inter-service communication refers to the exchange of information or messages between different services in a microservices architecture.
                            it enables services to collaborate, share data, and coordinate their actions.
"""


"""
EVENT DRIVEN ARCHITECHTURE:
                        Event-driven architecture (EDA) is an architectural pattern that emphasizes the production, detection, and consumption of events to enable communication and coordination between services.
                        In an event-driven architecture, services communicate by publishing and subscribing to events.

                        PROCESS:
                                1.When an event is published, it is typically broadcast to the interested subscribers, which can be other services or components. 
 
                                2.Subscribers react to the event by performing their own actions or triggering further processes.
                                3.The decoupled nature of event-driven architecture allows services to communicate asynchronously and ensures loose coupling between them.
BENIFITS:

        1.Loose coupling: Services are decoupled from each other, allowing them to evolve independently without impacting other services.
        2.Scalability: Services can scale independently since they communicate through events, enabling horizontal scaling and handling varying workloads.
        3.Extensibility: New services can be added easily by subscribing to relevant events, allowing for easier system evolution and modular design.
        4.Asynchronous communication: Event-driven architecture promotes asynchronous communication, allowing services to operate independently without waiting for immediate responses.
        5.Fault tolerance: If a service is temporarily unavailable, events can be stored and processed later, ensuring fault tolerance and resilience.
"""

