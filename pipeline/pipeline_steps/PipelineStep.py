from abc import ABC, abstractmethod
from typing import Dict


class PipelineStep(ABC):
    @abstractmethod
    def run(self, input_data: Dict[str, str]) -> Dict[str, str]:
        pass
