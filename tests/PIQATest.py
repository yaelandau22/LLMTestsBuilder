from pipeline.Pipeline import Pipeline
from utils.FilesUtils import read_jsonl_file, sample_objects, extract_values_by_key, read_lst_file


class PIQATest:
    QUESTIONS_KEY = 'goal'
    SOLUTION1_KEY = 'sol1'
    SOLUTION2_KEY = 'sol2'

    def __init__(self, data_file_path, labels_file_path, sample_size, pipline: Pipeline, final_answer_key, init_keys, seed=None):
        self.data_file_path = data_file_path
        self.labels_file_path = labels_file_path
        self.sample_size = sample_size
        self.pipline = pipline
        self.final_answer_key = final_answer_key
        self.seed = seed
        self.init_keys = init_keys

    def run(self, should_log=False):
        sampled_questions, sampled_labels, sampled_questions_sol1, sampled_questions_sol2 = self.load_data(self.data_file_path, self.labels_file_path, self.sample_size, self.seed)
        results_list = []
        labels_list = []

        for index, (sampled_question, question_label, sampled_question_sol1, sampled_question_sol2) in enumerate(zip(sampled_questions, sampled_labels, sampled_questions_sol1, sampled_questions_sol2)):
            if should_log:
                print(f"At interation {index+1} ...")

            init_input_map = self.get_init_input_map(sampled_question, sampled_question_sol1, sampled_question_sol2)
            output = self.pipline.run(init_input_map)
            results_list.append(output[self.final_answer_key])
            labels_list.append(question_label)

        return self.get_succes_rate(results_list, labels_list)


    def load_data(self, data_file_path, labels_file_path, sample_size, seed):
        questions_jsons = read_jsonl_file(data_file_path)
        sampled_questions_jsons = sample_objects(questions_jsons, sample_size, seed)
        labels_data = read_lst_file(labels_file_path)
        sampled_questions = extract_values_by_key(sampled_questions_jsons, PIQATest.QUESTIONS_KEY)
        sampled_labels = sample_objects(labels_data, self.sample_size, self.seed)
        sampled_questions_sol1 = extract_values_by_key(sampled_questions_jsons, self.SOLUTION1_KEY)
        sampled_questions_sol2 = extract_values_by_key(sampled_questions_jsons, self.SOLUTION2_KEY)
        return sampled_questions, sampled_labels, sampled_questions_sol1, sampled_questions_sol2

    def get_init_input_map(self, sampled_question, sampled_question_sol1, sampled_question_sol2):
        return {
            self.init_keys[0]: sampled_question,
            self.init_keys[1]: sampled_question_sol1,
            self.init_keys[2]: sampled_question_sol2
        }

    def get_succes_rate(self, results_list, labels_list):
        success_counter = 0
        for result, label in zip(results_list, labels_list):
            if result == label:
                success_counter += 1

        success_rate = (success_counter / len(labels_list)) * 100
        return success_rate
