"""Product Service concrete class that handles product-specific operations."""

from interface.service_interface import ServiceInterface

class ProductService(ServiceInterface):
    def handle_request(self, request: dict) -> str:
        
        product_id = request.get("product_id")

        if product_id is None:
            return "[ProductService] Error: product_id not provided"

        
        return f"[ProductService] has been called and your product_id is: {product_id}"