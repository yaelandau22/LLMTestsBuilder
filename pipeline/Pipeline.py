from typing import List, Dict

from pipeline.pipeline_steps.PipelineStep import PipelineStep


class Pipeline:
    def __init__(self, steps: List[PipelineStep]):
        self.steps = steps

    def run(self, input_data: Dict[str, str]) -> Dict[str, str]:
        result = input_data
        for step in self.steps:
            result = step.run(result)
        return result
