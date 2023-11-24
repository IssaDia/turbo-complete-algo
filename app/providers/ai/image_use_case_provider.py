from interfaces.image_analysis_interface import ImageUseCase
from use_cases.image_analysis.tensorflow.use_case_tensorflow_image_analysis import TensorFlowImageUseCase
from use_cases.image_analysis.transformers.use_case_transformers_image_analysis import TransformersImageUseCase  # Import the missing class

def get_image_use_case(use_tensorflow: bool = True, use_transformers: bool = False) -> ImageUseCase:
    return TensorFlowImageUseCase() if use_tensorflow else (TransformersImageUseCase() if use_transformers else None)
