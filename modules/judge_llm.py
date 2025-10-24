from deepeval.models.llms import AmazonBedrockModel

# AWS is not a mandatory requirement to run `deepeval` test cases.
# We're using `Amazon-Nova-Pro` as the `JudgeLLM` for this demo.

# You may select any LLM (that can be trusted as reliable) as your `JudgeLLM`, by using the below list of classes already available in the `deepeval` library.
# ```
# https://github.com/confident-ai/deepeval/tree/main/deepeval/models/llms
# ```
# The available options for choosing a `JudgeLLM` (as per the above link) includes:
# - OpenAI
# - Deepseek
# - Gemini
# - AWS
# - Azure
# - Ollama
# - and more...

# Also you can write your own custom `JudgeLLM`by extending from `deepeval.models.DeepEvalBaseModel` class.

def get_judge_llm():
    return AmazonBedrockModel(
        model_id="amazon.nova-pro-v1:0",
        region_name="us-east-1"
    )