"""
CQRS stands for Command Queue Responsiblity Segarations
It is a design pattern commonly used in microservices architectures to separate the read and write operations, providing different models for handling each type of operation
CQRS emphasizes the idea that the read and write concerns of an application have different characteristics and should be treated differently

 Q3: In CQRS, the application is divided into two main parts:
                                        1.Command side (Write side):
                                                It includes functionality such as creating, updating, or deleting data.
                                                eg: 
                                        # write_service/views.py
                                            from django.http import JsonResponse

                                            def create_product(request):
                                                # Extract product details from the request
                                                
                                                # Perform necessary validations and business logic for creating a product
                                                
                                                # Save the product to the write database
                                                # ...
                                                
                                                return JsonResponse({'message': 'Product created successfully'})
                                        2.Query side (Read side):
                                                It provides read-only access to the application's data and focuses on delivering optimal performance for querying and retrieving information
                                         read_service/views.py

                                            from django.http import JsonResponse

                                            def get_product(request, product_id):
                                                # Retrieve the product from the read database based on the product_id
                                                
                                                # Perform any necessary data transformations or formatting
                                                
                                                # Return the product details as a JSON response
                                                return JsonResponse(product_details)
  

                                                
By separating the read and write concerns, CQRS allows for more scalable and efficient architectures
"""
"""WorkFlow
    1.The write_service handles write operations, such as creating a product, performing validations and business logic, and saving the product to the write database.
    2.The read_service handles read operations, retrieving product details from the read database based on the product_id and returning them as a JSON response.
    3.By separating write and read operations into different services, you can optimize each side independently, scale them separately, use different databases, and apply caching or indexing strategies for improved read performance.
"""
