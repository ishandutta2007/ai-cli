from typing import Any, Dict, List, Optional
from abc import ABC, abstractmethod

class Model(ABC):
    """Base class every AI model plugin should subclass or follow"""

    def __init__(self, model_id: str, **kwargs):
        self.model_id = model_id
        self.kwargs = kwargs

    @abstractmethod
    def run(self, prompt: str, **kwargs) -> Dict[str, Any]:
        """Unified run method — returns {'text': ..., 'image_url': ..., etc.}"""
        pass

    def supports(self, capability: str) -> bool:
        """'text', 'image_gen', 'video_gen', 'tts', 'stt', etc."""
        return False

registered_models: Dict[str, type[Model]] = {}

def register_models(register_fn):
    """Plugin hook: register_models(register)"""
    register_fn(registered_models)

def get_model(model_name: str) -> Model:
    if model_name not in registered_models:
        raise ValueError(f"Unknown model: {model_name}")
    return registered_models[model_name](model_name)