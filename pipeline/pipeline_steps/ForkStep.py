
from typing import Dict

from pipeline.pipeline_steps.PipelineStep import PipelineStep


class ForkStep(PipelineStep):

    def __init__(self, key_to_step_map: Dict[str, PipelineStep]):
        self.key_to_step_map = key_to_step_map

    def run(self, input_data: Dict[str, str]) -> Dict[str, str]:
        next_step = None
        for key in self.key_to_step_map:
            if key in input_data:
                next_step = self.key_to_step_map[key]
                break

        if next_step:
            return next_step.run(input_data)

        return input_data
