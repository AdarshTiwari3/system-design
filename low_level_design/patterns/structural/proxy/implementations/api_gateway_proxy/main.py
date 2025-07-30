"""main code runner"""

from proxy.api_gateway import APIGatewayProxy
from client.client import send_request
from services.product_service import ProductService
from services.user_service import UserService

def run_api_gateway_proxy():
    print("\nRunning API Gateway Proxy...")
    user_service=APIGatewayProxy(UserService())
    product_service=APIGatewayProxy(ProductService())
    valid_token="secret-token-123"
    print("\n--- Valid Request to UserService ---")
    send_request(user_service, {"user_token": valid_token, "user_id": 42})

    print("\n--- Valid Request to ProductService ---")
    send_request(product_service, {"user_token": valid_token, "product_id": 42})

    
    print("\n--- Invalid Request to ProductService ---")
    send_request(product_service, {"user_token": "invalid-token", "product_id": 99})

    

if __name__ == "__main__":
    print("\nProxy design pattern")
    run_api_gateway_proxy()