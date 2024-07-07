**A proposed framework for build LLM pipline tests**
The basic building blocks of piplines are:
PipelineStep - perform a singel logical operation.
Pipeline - Perform a series of PipelineSteps.

Using these basic building blocks, a more complex pipelines can be composed, such as ConditionalLoopPipelineStep and more.

In order to activate the following key will be requierd:
    GOOGLE_CLOUD_API_KEY = "YOUR_GOOGLE_CLOUD_API_KEY"
    SEARCH_ENGINE_ID = "YOUR_SEARCH_ENGINE_ID"
    GOOGLE_AI_STUDIO_API_KEY = "YOUR_GOOGLE_AI_STUDIO_API_KEY"
