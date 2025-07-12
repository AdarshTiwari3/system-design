"""client """

from builder.create_url_builder import CreateURLBuilder
def run_builder_method():

    builder=CreateURLBuilder()

    url = (
        builder
        .set_protocol("https")
        .set_domain("google.com")
        .set_port(8080)
        .set_path("search")
        .set_query_param({"q": "python"})
        .build()
    )
    print(url)
    # Output: https://google.com:8080/search?q=python
