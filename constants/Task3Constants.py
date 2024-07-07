
class Task3Constants:
    PROMPT_QUESTION_TEMPLATE = """
        SYSTEM: I will give you a task: 
        1. I will give you a question or sentence to complete and two possible answers. 
        2. If you sure what is the right answer then please answer either A or B, depending on which answer is better. please write your final answer (either A or B) between the <answer> and </answer> tags. 
        2. But if you are not sure what is the right answer, give me instead a google search term, as accurate as possible, that will assist to find the answer on a google search. In that case please write your final answer between <search> and </search> tags.  
        QUESTION: {question_input}           
        OPTION A: {sol_1}
        OPTION B: {sol_2}
        ANSWER:
        """

    PROMPT_QUESTION_WITH_GOOGLE_RESULT_TEMPLATE = """
        SYSTEM: I will give you a task: 
        1. I will give you a question or sentence to complete and two possible answers. Please answer either A or B, depending on which answer is better. please write your final answer (either A or B) between the <answer> and </answer> tags. 
        2. In order to assist you answer the question, I provided some data from the internet that can be helpful. The data in an HTML site content, provided under the section 'DATA'. The provided data is not guaranteed to be relevant, it is just the content of the first site on google search on the search term '{search_term}'.  
        QUESTION: {question_input}           
        OPTION A: {sol_1}
        OPTION B: {sol_2}
        DATA: {search_content}
        ANSWER:
        """

    GEMINI_MODEL_NAME = "gemini-pro"
    FINAL_ANSWER_KEY = "output"
    SEARCH_TERM_KEY = "search_term"
    SEARCH_CONTENT_KEY = "search_content"
    DATA_FILE_PATH = 'data/train.jsonl'
    LABELS_FILE_PATH = 'data/train-labels.lst'
    INIT_KEYS = ["question_input", "sol_1", "sol_2"]
    ANSWER_REGEX = r"<answer>(.*?)</answer>"
    SEARCH_REGEX = r"<search>(.*?)</search>"
    ANSWER_TO_LABEL_MAP = {'A': '0', 'B': '1'}
