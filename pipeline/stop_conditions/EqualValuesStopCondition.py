from pipeline.stop_conditions.StopCondition import StopCondition

import re
from typing import Dict


class EqualValuesStopCondition(StopCondition):
    def __init__(self, regex_pattern: str, key1: str, key2: str):
        self.pattern = re.compile(regex_pattern)
        self.key1 = key1
        self.key2 = key2

    def should_stop(self, output: Dict[str, str]) -> bool:
        value1 = output.get(self.key1, "")
        value2 = output.get(self.key2, "")
        return value1 == value2
