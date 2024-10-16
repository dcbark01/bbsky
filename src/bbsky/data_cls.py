import yarl
from cattrs import Converter

URL = yarl.URL

converter = Converter()
structure = converter.structure
unstructure = converter.unstructure


@converter.register_structure_hook
def url_from_str(instance: str, cl: URL) -> URL:
    return URL(instance)


@converter.register_unstructure_hook
def url_to_str(instance: URL) -> str:
    return str(instance)
