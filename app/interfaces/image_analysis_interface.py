from abc import ABC, abstractmethod

class ImageUseCase(ABC):
    @abstractmethod
    def analyze_image(self, image_path: str) -> str:
        pass
    