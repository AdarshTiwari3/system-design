from adaptee.adaptee_interface import XMLDataProvider
class XMLFromString(XMLDataProvider):
    def __init__(self, xml_input: str):
        self._xml_input = xml_input
    def get_data(self) -> str:  
        return self._xml_input