In this project I try to implement a CQRS pattern and a Event Oriented Architecture through the use of RabbitMQ.

The desired workflow to add functionalities in this system should be:
1. Create a new command or query endpoint in the app
2. Create a new command or query 
3. Add a new command or query handler from a template (TODO) and configure it to run the command or ask for the query.
4. Add a new command or qury handler from a template and write a function that deals with the command or query content.

In the case that secondary effects should be triggered after one of this processes is done, an event bus should be created.
This event bus and its related components should mirror the structure of the command bus and the related components.
