from pipeline.stop_conditions.StopCondition import StopCondition

from typing import Dict, List


class AtLeastOneKeyExistStopCondition(StopCondition):
    def __init__(self, keys: List[str]):
        self.keys = keys

    def should_stop(self, output: Dict[str, str]) -> bool:
        return any(key in output for key in self.keys)
