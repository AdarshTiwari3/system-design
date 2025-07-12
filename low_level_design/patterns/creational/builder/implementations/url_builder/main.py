""" main runner of url builder design pattern"""
from builder.create_url_builder import CreateURLBuilder
from client.client import run_builder_method
from director.director import CreateDirector
def url_generator():
    run_builder_method()
    builder=CreateURLBuilder()
    url = builder.set_protocol("http").set_domain("myweb.com").build()
    print(url)
    #build url using director
    build=CreateDirector(builder)
    url=build.get_url("https","www.lld.com")
    print(url)
    
if __name__== "__main__":
    """ uml diagram will be similar as house builder so we are not going to make it"""
    print("\nBuilder Design Pattern of URL:")
    
    url_generator()