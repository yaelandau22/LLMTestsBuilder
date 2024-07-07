
from typing import Dict, Any

from pipeline.pipeline_steps.PipelineStep import PipelineStep


class RemoveKeyPipelineStep(PipelineStep):

    def __init__(self, key_to_remove: str):
        self.key_to_remove = key_to_remove

    def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        input_data.pop(self.key_to_remove, None)
        return input_data
