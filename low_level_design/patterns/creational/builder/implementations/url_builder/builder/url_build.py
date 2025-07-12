"""URL builder interface"""
from abc import ABC, abstractmethod
from typing import Dict
from product.product import URL
from typing_extensions import Self
class URLBuilder(ABC):
    @abstractmethod
    def set_protocol(self, protocol: str) -> Self:
        pass

    @abstractmethod
    def set_domain(self, domain: str) -> Self:
        pass

    @abstractmethod
    def set_port(self, port: int) -> Self:
        pass

    @abstractmethod
    def set_path(self, path: str) -> Self:
        pass

    @abstractmethod
    def set_query_param(self, query_param: Dict[str,str]) -> Self:
        pass

    @abstractmethod
    def build(self) -> URL:
        pass