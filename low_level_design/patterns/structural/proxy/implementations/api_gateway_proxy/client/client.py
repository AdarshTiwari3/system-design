"""client for api gateway proxy"""

def send_request(service, request_data):
    print(service.handle_request(request_data))
