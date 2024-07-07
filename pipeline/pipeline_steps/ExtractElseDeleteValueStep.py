import re
from typing import Dict

from pipeline.pipeline_steps.PipelineStep import PipelineStep


class ExtractElseDeleteValueStep(PipelineStep):
    def __init__(self, input_key, output_key_to_regex_map: Dict[str, str]):
        self.patterns = {key: re.compile(pattern) for key, pattern in output_key_to_regex_map.items()}
        self.input_key = input_key

    def run(self, input_data: Dict[str, str]) -> Dict[str, str]:
        raw_output = input_data.get(self.input_key, "")

        for output_key, pattern in self.patterns.items():
            match = pattern.search(raw_output)

            if match:
                input_data = input_data | {output_key: match.group(1)}
            else:
                if output_key in input_data:
                    del input_data[output_key]

        return input_data

