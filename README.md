# A proposed framework for building LLM piplines
The basic building blocks of piplines are:<br>
* PipelineStep - perform a singel logical operation.
* Pipeline - Perform a series of PipelineSteps.

Using these basic building blocks, a more complex pipelines can be composed, such as ConditionalLoopPipelineStep and more.<br><br>
![Untitled Diagram drawio](https://github.com/yaelandau22/LLMTestsBuilder/assets/16151631/91eab800-05b7-47a6-a00c-64aee661176b)
<br><br>
In order to activate the following key will be requierd:<br>
    GOOGLE_CLOUD_API_KEY = "YOUR_GOOGLE_CLOUD_API_KEY"<br>
    SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"<br>
    GOOGLE_AI_STUDIO_API_KEY = "YOUR_GOOGLE_AI_STUDIO_API_KEY"<br>

