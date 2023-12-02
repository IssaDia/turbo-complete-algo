
from external.replicate.replicate_ai import ReplicateAPI

class DescriptionUseCase:
    def __init__(self, replicate_api : ReplicateAPI):
        self._replicate_api = replicate_api

    def execute(self, description_text, keyword):
        return self._replicate_api.generate_description(description_text, keyword)
