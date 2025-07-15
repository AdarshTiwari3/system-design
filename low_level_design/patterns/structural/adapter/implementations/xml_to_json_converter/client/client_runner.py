"""client code"""
from adaptee.xml_from_string import XMLFromString
from adapter.xml_to_json_adapter import XMLToJSONAdapter
def run_client():
    xml_string = """
        <user id="123">
        <name>John</name>
        <contact>
            <email>john@example.com</email>
        </contact>
        </user>
        """
    xml_source=XMLFromString(xml_string)
    adapter=XMLToJSONAdapter(xml_source)
    json_data=adapter.get_data()
    print(json_data)

