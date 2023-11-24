
from external.replicate.replicate_ai import ReplicateAPI

class DescriptionUseCase:
    def __init__(self, replicate_api : ReplicateAPI):
        self._replicate_api = replicate_api

    def execute(self, prompt_input):
        return self._replicate_api.generate_description(prompt_input)
