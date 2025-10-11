# GenAI Output Validation

## Concept

Suppose you've built your own custom LLM (for privacy or confidentiality reasons), or you want to evaluate a new LLM of interest against a mature LLM such as **ChatGPT**, **Gemini**, **LLaMA**, etc.

**Validating AI output** means measuring how accurate, relevant, or reliable an AI-generated response is for a given input prompt (from your LLM of interest), compared to a reference or ideal answer.

Using a `JudgeLLM` — a mature LLM that is widely accepted, such as ChatGPT, Gemini, LLaMA, etc. — allows you to automate this evaluation.

**Quantitative validation** often involves:
- Comparing against reference answers.
- Scoring AI-generated outputs quantitatively based on criteria enforced by a given quality metric.
- Aggregating results to produce a final quality score.
- Providing justified reasoning for the evaluation results.

---

### Metric Explanations

All metrics produce a score between **0.0** and **1.0**, where **1.0** indicates perfect alignment with the evaluation goal. Each metric includes a **Reason** to explain the score, highlighting what the AI did well or where it failed.

##### 1. AnswerRelevancy
- **Purpose:** Measures how relevant the AI-generated answer is to the original input prompt.
- **Scoring:** 0.0 – 1.0
- **Reason:** Explains whether the output directly addresses the user query. Low scores indicate off-topic or partially relevant answers.

##### 2. Faithfulness
- **Purpose:** Assesses whether the AI output is factually correct relative to the source/reference.
- **Scoring:** 0.0 – 1.0
- **Reason:** Highlights factual errors or unsupported claims. High scores indicate the answer faithfully reflects the expected content.

##### 3. ContextualPrecision
- **Purpose:** Measures the proportion of relevant content in the AI output compared to all content generated.
- **Scoring:** 0.0 – 1.0
- **Reason:** Indicates if irrelevant or extra content was produced. Low precision means the output contains unnecessary or inaccurate information.

##### 4. ContextualRecall
- **Purpose:** Measures how much of the expected information is actually present in the AI output.
- **Scoring:** 0.0 – 1.0
- **Reason:** Explains which key points were missing from the AI answer. High recall indicates most expected content was covered.

##### 5. ContextualRelevancy
- **Purpose:** Combines precision and recall to evaluate how relevant and complete the content is in context.
- **Scoring:** 0.0 – 1.0
- **Reason:** Highlights missing or irrelevant pieces, giving a holistic view of content quality.

##### 6. Hallucination
- **Purpose:** Detects whether the AI produced content that is fabricated or not supported by the source.
- **Scoring:** 0.0 – 1.0
- **Reason:** High score indicates no hallucinations; low score explains which portions are fabricated or speculative.

##### 7. Summarization
- **Purpose:** Evaluates how well the AI output summarizes the provided context or expected answer.
- **Scoring:** 0.0 – 1.0
- **Reason:** Indicates whether key points were retained or lost, and if the summary is concise and coherent.


---

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
