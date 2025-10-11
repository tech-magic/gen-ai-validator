# Concept: AI Output Validation

Validating AI output means measuring how accurate, relevant, or reliable a generated response is compared to a reference or ideal behavior.

Using a JudgeLLM allows you to automate this evaluation.

Quantitative validation often involves:
- Scoring outputs using metrics.
- Comparing against reference answers.
- Aggregating results to produce a final quality score.

## Pre-requisites
- Install Python3
- Ensure that you have an AWS account and valid AWS credentials.
- Configure your AWS credentials to your default AWS profile using `aws configure` command inside the `$HOME/.aws` folder.

## How to Run

```
python3 -m venv llm-testing-venv
source llm-testing-venv/bin/activate
pip install -r requirements.txt
python main.py
```

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
