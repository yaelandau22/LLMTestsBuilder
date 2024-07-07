from typing import Dict

from pipeline.pipeline_steps.PipelineStep import PipelineStep


class ReplaceValueStep(PipelineStep):
    def __init__(self, replace_map: Dict[str, str], key_to_replace):
        self.replace_map = replace_map
        self.key_to_replace = key_to_replace

    def run(self, input_data: Dict[str, str]) -> Dict[str, str]:
        input_data[self.key_to_replace] = self.replace_map[input_data[self.key_to_replace]]
        return input_data
