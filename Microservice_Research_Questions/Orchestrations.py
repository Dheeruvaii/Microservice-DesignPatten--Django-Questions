"""
Orchestrations is a Logical entity handles the business logic
Used to share data and achieve business logic
In the orchestration approach, there is a central component called the orchestrator that controls and coordinates the interactions between different microservices
t acts as a conductor, making high-level decisions and directing the microservices to perform the necessary actions.



1.Let's consider a simple e-commerce system with two microservices: Order Service and Payment Service. 
"""
"""Order Service
def place_order(order):
    # Process order placement logic
    order_status = "PLACED"
    # Call Payment Service to process payment
    payment_status = payment_service.process_payment(order)
    if payment_status == "SUCCESS":
        order_status = "COMPLETED"
    else:
        order_status = "PAYMENT_FAILED"
    # Update order status in the database
    update_order_status(order, order_status)

# Payment Service
def process_payment(order):
    # Process payment logic
    payment_status = "SUCCESS"
    # Update payment status in the database
    update_payment_status(order, payment_status)
    return payment_status  
    """

"""
The orchestrator might follow this sequence:

Receive the order request from the user.
Verify the user's payment with the payment processing microservice.
Check the availability of the ordered items with the inventory management microservice.
If the payment is successful and items are available, initiate the shipping process with the shipping microservice.
Notify the user about the order status.


        * Here is no use of orchestrator manages the overall flow of the process, making decisions based on the responses received from each microservice 
        * here  not implementing  message queue and event-driven-architechture 
"""