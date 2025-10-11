# AI-Validator
Explaining how to validate the quality of an AI generated output quantitatively.

## Pre-requisites
- Install Python3
- Ensure that you have an AWS account and valid AWS credentials.
- Configure your AWS credentials to your default AWS profile using `aws configure` command inside the $HOME/.aws folder.

## Notes
AWS is not a mandatory requirement to run `deepeval` test cases.
It is ONLY listed as a pre-requisite here since Amazon-Nova-Pro is being used as the `JudgeLLM` during this project.

You may select any LLM (which can be trusted as reliable) as your JudgeLLM, by using the below list of classes already available in the `deepeval` library in the below link.
```
https://github.com/confident-ai/deepeval/tree/main/deepeval/models/llms
```
The available options for choosing a `JudgeLLM` (as per the above link) includes:
- OpenAI
- Deepseek
- Gemini
- AWS
- Azure
- Ollama
- and more...

Also you can write your own custom `JudgeLLM`by extending from `deepeval.models.DeepEvalBaseModel` class.


# how to run

```
python3 -m venv llm-testing-venv
source llm-testing-venv/bin/activate
pip install -r requirements.txt
python main.py
```
python main.py
```
