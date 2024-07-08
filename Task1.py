from models.GeminiModel import GeminiModel
from pipeline.Pipeline import Pipeline
from pipeline.pipeline_steps.ConditionalLoopPipelineStep import ConditionalLoopPipelineStep
from pipeline.pipeline_steps.ExtractElseDeleteValueStep import ExtractElseDeleteValueStep
from pipeline.pipeline_steps.LLMModelStep import LLMModelStep
from pipeline.pipeline_steps.ReplaceValueStep import ReplaceValueStep
from pipeline.stop_conditions.AtLeastOneKeyExistStopCondition import AtLeastOneKeyExistStopCondition
from tests.PIQATest import PIQATest
from constants.Task1Constants import Task1Constants

if __name__ == "__main__":
    model = GeminiModel(Task1Constants.GEMINI_MODEL_NAME)
    llmModelStep = LLMModelStep(model, Task1Constants.PROMPT_QUESTION_TEMPLATE, Task1Constants.FINAL_ANSWER_KEY)
    replace_value_step = ReplaceValueStep(Task1Constants.ANSWER_TO_LABEL_MAP, Task1Constants.FINAL_ANSWER_KEY)
    extract_value_step = ExtractElseDeleteValueStep(Task1Constants.FINAL_ANSWER_KEY, {Task1Constants.FINAL_ANSWER_KEY: Task1Constants.ANSWER_REGEX})
    key_exist_stop_condition = AtLeastOneKeyExistStopCondition([Task1Constants.FINAL_ANSWER_KEY])
    verification_pipeline = Pipeline([llmModelStep, extract_value_step])
    conditional_loop_step = ConditionalLoopPipelineStep(verification_pipeline, key_exist_stop_condition, max_iterations=5)
    pipeline = Pipeline([conditional_loop_step, replace_value_step])

    piqaTest = PIQATest(Task1Constants.DATA_FILE_PATH, Task1Constants.LABELS_FILE_PATH, 50, pipeline, Task1Constants.FINAL_ANSWER_KEY, Task1Constants.INIT_KEYS)
    success_rate = piqaTest.run(should_log=True)
    print(f"success rate: {success_rate}")
