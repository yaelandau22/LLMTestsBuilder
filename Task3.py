
from models.GeminiModel import GeminiModel
from pipeline.Pipeline import Pipeline
from pipeline.pipeline_steps.ConditionalLoopPipelineStep import ConditionalLoopPipelineStep
from pipeline.pipeline_steps.ExtractElseDeleteValueStep import ExtractElseDeleteValueStep
from pipeline.pipeline_steps.ForkStep import ForkStep
from pipeline.pipeline_steps.GoogleSearchStep import GoogleSearchStep
from pipeline.pipeline_steps.LLMModelStep import LLMModelStep
from pipeline.pipeline_steps.ReplaceValueStep import ReplaceValueStep
from pipeline.stop_conditions.AtLeastOneKeyExistStopCondition import AtLeastOneKeyExistStopCondition
from tests.PIQATest import PIQATest
from constants.Task3Constants import Task3Constants

if __name__ == "__main__":
    model = GeminiModel(Task3Constants.GEMINI_MODEL_NAME)
    model_step = LLMModelStep(model, Task3Constants.PROMPT_QUESTION_TEMPLATE, Task3Constants.FINAL_ANSWER_KEY)
    model_step_with_search_term = LLMModelStep(model, Task3Constants.PROMPT_QUESTION_WITH_GOOGLE_RESULT_TEMPLATE, Task3Constants.FINAL_ANSWER_KEY)
    replace_value_step = ReplaceValueStep(Task3Constants.ANSWER_TO_LABEL_MAP, Task3Constants.FINAL_ANSWER_KEY)
    key_exist_condition_first = AtLeastOneKeyExistStopCondition(Task3Constants.FINAL_ANSWER_KEY)

    extract_answer_value_step = ExtractElseDeleteValueStep(Task3Constants.FINAL_ANSWER_KEY, {Task3Constants.FINAL_ANSWER_KEY: Task3Constants.ANSWER_REGEX})
    extract_answer_or_search_term_value_step = ExtractElseDeleteValueStep(Task3Constants.FINAL_ANSWER_KEY, {Task3Constants.FINAL_ANSWER_KEY: Task3Constants.ANSWER_REGEX, Task3Constants.SEARCH_TERM_KEY: Task3Constants.SEARCH_REGEX})

    answer_or_search_key_exist_stop_condition = AtLeastOneKeyExistStopCondition([Task3Constants.FINAL_ANSWER_KEY, Task3Constants.SEARCH_TERM_KEY])
    model_verification_pipeline = Pipeline([model_step, extract_answer_or_search_term_value_step])
    model_conditional_loop_step = ConditionalLoopPipelineStep(model_verification_pipeline, answer_or_search_key_exist_stop_condition, max_iterations=5)

    answer_key_exist_stop_condition = AtLeastOneKeyExistStopCondition([Task3Constants.FINAL_ANSWER_KEY])
    google_search_step = GoogleSearchStep(Task3Constants.SEARCH_TERM_KEY, Task3Constants.SEARCH_CONTENT_KEY)
    model_with_google_result_verification_pipeline = Pipeline([google_search_step, model_step_with_search_term, extract_answer_value_step])
    model_with_google_result_conditional_loop_step = ConditionalLoopPipelineStep(model_with_google_result_verification_pipeline, answer_key_exist_stop_condition, max_iterations=5)

    fork_step = ForkStep({Task3Constants.FINAL_ANSWER_KEY: None, Task3Constants.SEARCH_TERM_KEY: model_with_google_result_conditional_loop_step})
    pipeline = Pipeline([model_conditional_loop_step, fork_step, replace_value_step])

    piqaTest = PIQATest(Task3Constants.DATA_FILE_PATH, Task3Constants.LABELS_FILE_PATH, 50, pipeline, Task3Constants.FINAL_ANSWER_KEY, Task3Constants.INIT_KEYS, seed=3)
    success_rate = piqaTest.run(should_log=True)
    print(f"success rate: {success_rate}")

