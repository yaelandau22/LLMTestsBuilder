class Task1Constants:
    PROMPT_QUESTION_TEMPLATE = """
        SYSTEM: I will give you a question or sentence to complete and two possible answers. Please answer either A or B, depending on which answer is better. You may write down your reasoning but please write your final answer (either A or B) between the <answer> and </answer> tags.
        QUESTION: {question_input}           
        OPTION A: {sol_1}
        OPTION B: {sol_2}
        ANSWER:
        """
    GEMINI_MODEL_NAME = "gemini-pro"
    ANSWER_REGEX = r"<answer>(.*?)</answer>"
    FINAL_ANSWER_KEY = "output_key"
    INIT_KEYS = ["question_input", "sol_1", "sol_2"]
    DATA_FILE_PATH = 'data/train.jsonl'
    LABELS_FILE_PATH = 'data/train-labels.lst'
    ANSWER_TO_LABEL_MAP = {'A': '0', 'B': '1'}