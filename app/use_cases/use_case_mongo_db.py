from providers.bdd.mongodb.mongodb_provider import MONGODB_PROVIDER

class GetDescriptionsUseCase:
    def __init__(self, mongodb_provider : MONGODB_PROVIDER):
        self.mongodb_provider = mongodb_provider

    def execute(self):
        self.mongodb_provider.get_descriptions()
class GetImagesUseCase:
    def __init__(self, mongodb_provider : MONGODB_PROVIDER):
        self.mongodb_provider = mongodb_provider

    def execute(self):
        self.mongodb_provider.get_image()