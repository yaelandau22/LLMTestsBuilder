
class Task2Constants:
    PROMPT_QUESTION_TEMPLATE = """
        SYSTEM: I will give you a question or sentence to complete and two possible answers. Please answer either A or B, depending on which answer is better. You may write down your reasoning but please write your final answer (either A or B) between the <answer> and </answer> tags”
        QUESTION: {question_input}           
        OPTION A: {sol_1}
        OPTION B: {sol_2}
        ANSWER:
        """

    PROMPT_VERIFICATION_TEMPLATE = """
        SYSTEM: I will give you a task:
        1. I will provide you a question or sentence to complete and two possible answers: A or B. 
        2. I need to know which option is better (A or B). 
        3. I already received a possible answer from another model which I provided under "THE OTHER MODEL ANSWER" section below.
        4. I want you to verify this answer. If you decide his answer is correct then write the answer (A or B) between the <answer> and </answer>. But if you think the answer in incorrect, then right your own answer. You may write down your reasoning but please write your final answer (either A or B) between the <answer> and </answer> tags.
        QUESTION: {question_input}           
        OPTION A: {sol_1}
        OPTION B: {sol_2}
        THE OTHER MODEL ANSWER: {first_answer} 
        YOUR ANSWER:
        """

    ANSWER_REGEX = r"<answer>(.*?)</answer>"
    FINAL_ANSWER_KEY = "first_answer"
    VERIFICATION_ANSWER_KEY = "second_answer"
    GEMINI_MODEL_NAME = "gemini-pro"
    INIT_KEYS = ["question_input", "sol_1", "sol_2"]
    DATA_FILE_PATH = 'data/train.jsonl'
    LABELS_FILE_PATH = 'data/train-labels.lst'
    ANSWER_TO_LABEL_MAP = {'A': '0', 'B': '1'}