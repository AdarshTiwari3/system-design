
""" Product Class """
from typing import Dict, Optional
class URL:
    def __init__(self) -> None:
        self.__protocol: Optional[str] = None
        self.__domain: Optional[str] = None
        self.__port: Optional[int] = None
        self.__path: str = ""
        self.__query_param: Dict[str, str] = {}


    def _set_protocol(self, protocol: str):
        self.__protocol=protocol

    def _set_domain(self, domain: str):
        self.__domain=domain
    
    def _set_port(self, port: int):
        self.__port=port

    def _set_path(self, path: str):
        self.__path=path

    def _set_query_param(self, query_param: Dict[str, str]):
        self.__query_param=query_param


    def __str__(self)->str:
        if not self.__protocol or not self.__domain:
            raise ValueError("Protocol and Domain are required to construct the URL")

        url=f"{self.__protocol}://{self.__domain}"

        if self.__port:
            url += f":{self.__port}"
        if self.__path:
            url += f"/{self.__path}"
        if self.__query_param:
            query_parts = []
            for key, value in self.__query_param.items():
                query_parts.append(f"{key}={value}")
            
            query_string = "&".join(query_parts)
            url += f"?{query_string}"


        return url