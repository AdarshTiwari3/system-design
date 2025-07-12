from typing import Optional, Dict
from builder.url_build import URLBuilder
from typing_extensions import Self
from product.product import URL

class CreateURLBuilder(URLBuilder):
    def __init__(self):
        self._protocol: Optional[str] = None
        self._domain: Optional[str] = None
        self._port: Optional[int] = None
        self._path: str = ""  # optional
        self._query_param: Dict[str, str] = {}  # optional

    def set_protocol(self, protocol: str = "") -> Self:
        self._protocol=protocol
        return self
    
    def set_domain(self, domain: str = "") -> Self:
        self._domain=domain
        return self
    
    def set_port(self, port: int = 0) -> Self:
        self._port=port
        return self
    
    def set_path(self, path: str = "") -> Self:
        self._path=path
        return self
    
    def set_query_param(self, query_param: Dict[str, str] = {}) -> Self:
        self._query_param=query_param
        return self
    
    def build(self) -> URL:
        url=URL()
        if not self._protocol or not self._domain:
            raise ValueError("Protocol and Domain are required to construct the URL")

        url._set_protocol(self._protocol)
        url._set_domain(self._domain)
        url._set_port(self._port) # type: ignore
        url._set_path(self._path)
        url._set_query_param(self._query_param)

        return url