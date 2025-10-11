# pip install deepeval boto3 langchain_aws aioboto3 asyncio

import asyncio
from deepeval.test_case import LLMTestCase
from deepeval.models.llms import AmazonBedrockModel
from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    ContextualRelevancyMetric,
    HallucinationMetric,
    SummarizationMetric
)

# -------------------------------
# Define test cases
# -------------------------------
test_cases = [
    {
        "input_prompt": "Who wrote the book 1984?",
        "expected_answer": "George Orwell wrote the novel 1984.",
        "ai_generated_answer": "George Orwell wrote it."
    },
    {
        "input_prompt": "What is the capital of France?",
        "expected_answer": "The capital of France is Paris.",
        "ai_generated_answer": "Paris"
    },
    {
        "input_prompt": "What is 2 + 2?",
        "expected_answer": "4",
        "ai_generated_answer": "4"
    }
]

# -------------------------------
# Define standard metrics map (with internal Judge LLM initialization)
# -------------------------------

def get_judge_llm():
    return AmazonBedrockModel(
        model_id="amazon.nova-pro-v1:0",
        region_name="us-east-1"
    )

def get_standard_metrics():
    judge_llm = get_judge_llm()
    return {
        'AnswerRelevancy': lambda: AnswerRelevancyMetric(threshold=0.7, model=judge_llm),
        'Faithfulness': lambda: FaithfulnessMetric(threshold=0.7, model=judge_llm),
        'ContextualPrecision': lambda: ContextualPrecisionMetric(threshold=0.4, model=judge_llm),
        'ContextualRecall': lambda: ContextualRecallMetric(threshold=0.4, model=judge_llm),
        'ContextualRelevancy': lambda: ContextualRelevancyMetric(threshold=0.4, model=judge_llm),
        'Hallucination': lambda: HallucinationMetric(threshold=0.7, model=judge_llm),
        'Summarization': lambda: SummarizationMetric(threshold=0.7, model=judge_llm)
    }

# -------------------------------
# Evaluate a single test case with multiple metrics
# -------------------------------
async def evaluate_test_case(case, metrics_to_run):

    prompt = case["input_prompt"]
    expected_answer = case["expected_answer"]
    ai_generated_answer = case["ai_generated_answer"]

    test_case_group = case.get('test_case_group', 'default')
    test_case_name = case.get('test_case_name', prompt)
    source_of_truth = case.get('background_context', f"# Input Prompt: \n {prompt} \n\n --- \n\n # Expected Answer: \n {expected_answer}")
    ai_inferred_truth = case.get('ai_inferred_context', f"# Input Prompt: \n {prompt} \n\n --- \n\n # AI-generated Answer: \n {ai_generated_answer}")

    test_case = LLMTestCase(
        input=prompt,
        actual_output=ai_generated_answer,
        expected_output=expected_answer,
        context=[source_of_truth],
        retrieval_context= [ai_inferred_truth],
        name=test_case_name
    )

    async def run_metric(metric_name, metric_instance):
        await metric_instance.a_measure(test_case)
        return {
            "metric": metric_name,
            "score": metric_instance.score,
            "reason": metric_instance.reason
        }

    # Run all metrics concurrently
    tasks = [
        run_metric(name, factory())
        for name, factory in metrics_to_run.items()
    ]
    metric_results = await asyncio.gather(*tasks)

    return {
        "test_case_group": test_case_group,
        "test_case_name": test_case_name,
        "input_prompt": prompt,
        "expected_answer": expected_answer,
        "ai_generated_answer": ai_generated_answer,
        "source_of_truth": source_of_truth,
        "ai_inferred_truth": ai_inferred_truth,
        "metrics": metric_results
    }

# -------------------------------
# Main async runner
# -------------------------------
async def main_async():
    # Get all standard metrics (judge_llm declared internally)
    standard_metrics = get_standard_metrics()

    # Run all test cases concurrently
    tasks = [evaluate_test_case(case, standard_metrics) for case in test_cases]
    results = await asyncio.gather(*tasks)

    # Aggregate and print results
    print("\n=== Evaluation Results ===")
    total_scores = {name: 0.0 for name in standard_metrics.keys()}
    num_cases = len(results)

    for idx, r in enumerate(results, 1):
        print(f"\n####### Test Case {idx} #######\n")
        print(f"Input Prompt: {r['input_prompt']}")
        print(f"Expected Answer: {r['expected_answer']}")
        print(f"AI-generated Answer: {r['ai_generated_answer']}\n")

        print(f"==== Source of Truth ==== \n{r['source_of_truth']}\n")
        print(f"==== AI-inferred Truth ==== \n{r['ai_inferred_truth']}\n")

        print(f"==== Evaluation Metrics ====\n")
        for m in r["metrics"]:
            print(f"  {m['metric']} Score: {m['score']:.2f}")
            print(f"  Reason: {m['reason']}\n")
            total_scores[m["metric"]] += m["score"]

    print("=== Average Metric Scores ===")
    for metric_name, total in total_scores.items():
        avg = total / num_cases
        print(f"{metric_name}: {avg:.2f}")

# -------------------------------
# Run the async main
# -------------------------------
if __name__ == "__main__":
    asyncio.run(main_async())
