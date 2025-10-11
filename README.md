# AI Output Validation

## Concept

Suppose you've built your own custom LLM (for privacy or confidentiality reasons), or you want to evaluate a new LLM of interest against a mature LLM such as **ChatGPT**, **Gemini**, **LLaMA**, etc.

**Validating AI output** means measuring how accurate, relevant, or reliable an AI-generated response is for a given input prompt (from your LLM of interest), compared to a reference or ideal answer.

Using a `JudgeLLM` — a mature LLM that is widely accepted, such as ChatGPT, Gemini, LLaMA, etc. — allows you to automate this evaluation.

**Quantitative validation** often involves:
- Comparing against reference answers.
- Scoring AI-generated outputs quantitatively based on criteria enforced by a given quality metric.
- Aggregating results to produce a final quality score.
- Providing justified reasoning for the evaluation results.

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
