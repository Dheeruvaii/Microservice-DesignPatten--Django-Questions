"""
Orchestrations is a Logical entity handles the business logic
Used to share data and achieve business logic

1.Let's consider a simple e-commerce system with two microservices: Order Service and Payment Service. 
"""
# Order Service
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
Here is no use of message queue and not implementing event-driven-architechture"""