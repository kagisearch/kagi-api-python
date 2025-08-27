# flake8: noqa

if __import__("typing").TYPE_CHECKING:
    # import apis into api package
    from openapi_client.api.enrichment_api import EnrichmentApi
    from openapi_client.api.fast_gpt_api import FastGPTApi
    from openapi_client.api.search_api import SearchApi
    from openapi_client.api.summarizer_api import SummarizerApi
    from openapi_client.api.translate_api import TranslateApi
    
else:
    from lazy_imports import LazyModule, as_package, load

    load(
        LazyModule(
            *as_package(__file__),
            """# import apis into api package
from openapi_client.api.enrichment_api import EnrichmentApi
from openapi_client.api.fast_gpt_api import FastGPTApi
from openapi_client.api.search_api import SearchApi
from openapi_client.api.summarizer_api import SummarizerApi
from openapi_client.api.translate_api import TranslateApi

""",
            name=__name__,
            doc=__doc__,
        )
    )
