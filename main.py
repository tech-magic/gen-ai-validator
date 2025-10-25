# pip install deepeval boto3 langchain_aws aioboto3 asyncio pandas altair

import asyncio

from modules.test_case_loader import load_test_cases
from modules.genai_metrics import get_standard_genai_metrics
from modules.test_case_evaluator import evaluate_llm_test_case
from modules.report_generator import generate_test_report

# -------------------------------
# Main async runner
# -------------------------------
async def main_async(test_case_file):

    # Validate test case file + Load test cases
    llm_test_cases = load_test_cases(test_case_file)

    # Get all standard metrics
    genai_test_metrics = get_standard_genai_metrics()

    # Run all test cases concurrently
    tasks = [evaluate_llm_test_case(case, genai_test_metrics) for case in llm_test_cases]
    test_results = await asyncio.gather(*tasks)

    # Generate test report
    generate_test_report(test_results, genai_test_metrics)

# -------------------------------
# Run the async main
# -------------------------------
if __name__ == "__main__":
    test_case_file = "test_cases/test_cases.json"
    asyncio.run(main_async(test_case_file))
