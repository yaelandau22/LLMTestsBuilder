from models.GeminiModel import GeminiModel
from pipeline.Pipeline import Pipeline
from pipeline.pipeline_steps.ConditionalLoopPipelineStep import ConditionalLoopPipelineStep
from pipeline.pipeline_steps.ExtractElseDeleteValueStep import ExtractElseDeleteValueStep
from pipeline.pipeline_steps.LLMModelStep import LLMModelStep
from pipeline.pipeline_steps.RemoveKeyPipelineStep import RemoveKeyPipelineStep
from pipeline.pipeline_steps.ReplaceValueStep import ReplaceValueStep
from pipeline.pipeline_steps.UpdateKeyPipelineStep import UpdateKeyPipelineStep
from pipeline.stop_conditions.EqualValuesStopCondition import EqualValuesStopCondition
from pipeline.stop_conditions.AtLeastOneKeyExistStopCondition import AtLeastOneKeyExistStopCondition
from tests.PIQATest import PIQATest
from constants.Task2Constants import Task2Constants

if __name__ == "__main__":

    model = GeminiModel(Task2Constants.GEMINI_MODEL_NAME)

    model_step = LLMModelStep(model, Task2Constants.PROMPT_QUESTION_TEMPLATE, Task2Constants.FINAL_ANSWER_KEY)
    second_model_for_verification_step = LLMModelStep(model, Task2Constants.PROMPT_VERIFICATION_TEMPLATE, Task2Constants.VERIFICATION_ANSWER_KEY)
    remove_key_step = RemoveKeyPipelineStep(Task2Constants.FINAL_ANSWER_KEY)
    update_key_step = UpdateKeyPipelineStep(Task2Constants.VERIFICATION_ANSWER_KEY, Task2Constants.FINAL_ANSWER_KEY)
    extract_else_delete_value_step_first = ExtractElseDeleteValueStep(Task2Constants.FINAL_ANSWER_KEY, {Task2Constants.FINAL_ANSWER_KEY: Task2Constants.ANSWER_REGEX})
    extract_else_delete_value_step_second = ExtractElseDeleteValueStep(Task2Constants.VERIFICATION_ANSWER_KEY, {Task2Constants.VERIFICATION_ANSWER_KEY: Task2Constants.ANSWER_REGEX})
    replace_value_step = ReplaceValueStep(Task2Constants.ANSWER_TO_LABEL_MAP, Task2Constants.FINAL_ANSWER_KEY)

    equal_values_condition = EqualValuesStopCondition(Task2Constants.ANSWER_REGEX, Task2Constants.FINAL_ANSWER_KEY, Task2Constants.VERIFICATION_ANSWER_KEY)
    key_exist_condition_first = AtLeastOneKeyExistStopCondition([Task2Constants.FINAL_ANSWER_KEY])
    key_exist_condition_second = AtLeastOneKeyExistStopCondition([Task2Constants.VERIFICATION_ANSWER_KEY])

    model_with_validation_pipeline = Pipeline([model_step, extract_else_delete_value_step_first])
    simple_model_with_validation_loop_step = ConditionalLoopPipelineStep(model_with_validation_pipeline, key_exist_condition_first, max_iterations=5)

    second_model_with_validation_pipeline = Pipeline([second_model_for_verification_step, extract_else_delete_value_step_second])
    second_model_with_validation_loop_step = ConditionalLoopPipelineStep(second_model_with_validation_pipeline, key_exist_condition_second, max_iterations=5)

    verification_pipeline = Pipeline([remove_key_step, update_key_step, second_model_with_validation_loop_step])
    conditional_loop_step = ConditionalLoopPipelineStep(verification_pipeline, equal_values_condition, max_iterations=5)

    final_pipeline = Pipeline([simple_model_with_validation_loop_step,
                               second_model_with_validation_loop_step,
                               conditional_loop_step,
                               replace_value_step])

    piqaTest = PIQATest(Task2Constants.DATA_FILE_PATH, Task2Constants.LABELS_FILE_PATH, 50, final_pipeline, Task2Constants.FINAL_ANSWER_KEY, Task2Constants.INIT_KEYS, seed=3)
    success_rate = piqaTest.run(should_log=True)
    print(f"success rate: {success_rate}")
