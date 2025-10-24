import asyncio
from deepeval.test_case import LLMTestCase

# -------------------------------
# Evaluate a single test case with multiple genai metrics
# -------------------------------
async def evaluate_llm_test_case(llm_test_case, metrics_to_run):

    prompt = llm_test_case["input_prompt"]
    expected_answer = llm_test_case["expected_answer"]
    ai_generated_answer = llm_test_case["ai_generated_answer"]

    test_case_group = llm_test_case["test_case_group"]
    test_case_name = llm_test_case["test_case_name"]
    source_of_truth = llm_test_case["background_context"]
    ai_inferred_truth = llm_test_case["ai_inferred_context"]

    deepeval_test_case = LLMTestCase(
        input=prompt,
        actual_output=ai_generated_answer,
        expected_output=expected_answer,
        context=[source_of_truth],
        retrieval_context= [ai_inferred_truth],
        name=test_case_name
    )

    async def run_metric(metric_name, metric_instance):
        await metric_instance.a_measure(deepeval_test_case)
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