import json
import random

def read_jsonl_file(file_path):
    with open(file_path, 'r') as file:
        return [json.loads(line) for line in file]

def read_lst_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().splitlines()
    return data

def sample_objects(json_objects, sample_size, seed=None):
    if seed is not None:
        random.seed(seed)
    return random.sample(json_objects, sample_size)


def extract_values_by_key(json_objects, key):
    return [json_obj.get(key, f'No {key} element found') for json_obj in json_objects]