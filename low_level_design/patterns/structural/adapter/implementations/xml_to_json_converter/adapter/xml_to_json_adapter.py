"""Adapter implementation of XML to JSON converter"""
from adapter.adapter_interface import JSONDataProvider
from adaptee.adaptee_interface import XMLDataProvider
import json

import xml.etree.ElementTree as ET #ElementTree module provides a simple and efficient way to parse, manipulate, and generate XML (eXtensible Markup Language) data in Python.
class XMLToJSONAdapter(JSONDataProvider):
    def __init__(self,xmlprovider: XMLDataProvider):
        self._xmlprovider=xmlprovider #for internal use only means like private

    def get_data(self) -> str:
        xml_string=self._xmlprovider.get_data()
        root=ET.fromstring(xml_string)
        #xml to json converter for nested xml
        """logic credit: internet"""
        def element_to_dict(element):
            result = {}
            for attr_key, attr_val in element.attrib.items():
                result[f"{attr_key}"] = attr_val

            children = list(element)
            # print("children=",children)
            if children:
                for child in children:
                    result[child.tag] = element_to_dict(child)
            else:
                text = element.text.strip() if element.text else ''
                return text if text else result

            return result

        data = {root.tag: element_to_dict(root)}
        return json.dumps(data, indent=4)