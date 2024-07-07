from abc import ABC, abstractmethod
from typing import Any


class StopCondition(ABC):

    @abstractmethod
    def should_stop(self, output: Any) -> bool:
        pass