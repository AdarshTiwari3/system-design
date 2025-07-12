# director class but this is optional
from builder.url_build import URLBuilder
from product.product import URL

class CreateDirector:
    def __init__(self, builder: URLBuilder):
        self._builder = builder

    def get_url(self,protocol="", domain="", path="", port=0, query={}) -> URL:
        """Build URL by chaining method calls."""
        return (
            self._builder
            .set_protocol(protocol)
            .set_domain(domain)
            .set_path(path)
            .set_port(port)
            .set_query_param(query)
            .build()
        )
