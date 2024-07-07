from langchain_google_genai import ChatGoogleGenerativeAI

from .Model import Model
from constants.Secrets import Secrets


class GeminiModel(Model):
    def __init__(self, model_name):
        super().__init__(model_name)
        self.llm_model = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=Secrets.GOOGLE_AI_STUDIO_API_KEY
        )

    def invoke(self, prompt):
        response = self.llm_model.invoke(prompt)
        return response.content