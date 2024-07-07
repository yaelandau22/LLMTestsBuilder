from typing import Dict
import requests
from bs4 import BeautifulSoup
from pipeline.pipeline_steps.PipelineStep import PipelineStep
from constants.Secrets import Secrets

class GoogleSearchStep(PipelineStep):
    URL = f"https://www.googleapis.com/customsearch/v1"

    def __init__(self, input_key, output_key):
        self.input_key = input_key
        self.output_key = output_key
        self.api_key = Secrets.GOOGLE_CLOUD_API_KEY,
        self.search_engine_id = Secrets.SEARCH_ENGINE_ID

    def run(self, input_data: Dict[str, str]) -> Dict[str, str]:
        params = {
            'q': input_data[self.input_key],
            'key': self.api_key,
            'cx': self.search_engine_id
        }

        response = requests.get(self.URL, params=params)
        results = response.json()

        soup = ""
        if 'items' in results:
            first_link = results['items'][0]['link']

            page_content = requests.get(first_link).text
            soup = BeautifulSoup(page_content, 'html.parser')

        return input_data | {self.output_key: soup}
