from typing import Dict

from pipeline.Pipeline import Pipeline
from pipeline.pipeline_steps.PipelineStep import PipelineStep
from pipeline.stop_conditions.StopCondition import StopCondition


class ConditionalLoopPipelineStep(PipelineStep):

    def __init__(self, pipeline: Pipeline, stop_condition: StopCondition, max_iterations: int):
        self.pipeline = pipeline
        self.max_iterations = max_iterations
        self.stop_condition = stop_condition

    def run(self, input_data: Dict[str, str]) -> Dict[str, str]:
        for i in range(self.max_iterations):
            if self.stop_condition.should_stop(input_data):
                return input_data
            input_data = self.pipeline.run(input_data)

        raise Exception(f"Max iterations ({self.max_iterations}) reached without satisfying the stop condition.")
