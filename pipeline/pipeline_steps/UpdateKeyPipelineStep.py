from typing import Dict, Any

from pipeline.pipeline_steps.PipelineStep import PipelineStep


class UpdateKeyPipelineStep(PipelineStep):

    def __init__(self, old_key: str, new_key: str):
        self.old_key = old_key
        self.new_key = new_key

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        if self.old_key in input_data:
            input_data[self.new_key] = input_data.pop(self.old_key)
        return input_data
