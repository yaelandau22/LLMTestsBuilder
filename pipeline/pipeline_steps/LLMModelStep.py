from typing import Dict

from models.Model import Model
from pipeline.pipeline_steps.PipelineStep import PipelineStep


class LLMModelStep(PipelineStep):
    def __init__(self, model: Model, prompt_template, output_key):
        self.model = model
        self.prompt_template = prompt_template
        self.output_key = output_key

    def run(self, input_data: Dict[str, str]) -> Dict[str, str]:
        full_prompt = self.prompt_template.format(**input_data)
        response = self.model.invoke(full_prompt)
        return input_data | {self.output_key: response}
