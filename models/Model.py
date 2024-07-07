from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self, model_path):
        self.model_path = model_path

    @abstractmethod
    def invoke(self, prompt):
        pass
