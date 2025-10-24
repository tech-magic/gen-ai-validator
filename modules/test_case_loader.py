import json
import os
import sys

def load_test_cases(test_cases_file):
    """
    Load and validate test cases from a JSON file.
    Exits the program if validation errors are found.

    Args:
        test_cases_file (str): Path to the JSON file containing test cases.

    Returns:
        list: A validated list of test case dictionaries.
    """
    # --- Step 1: Load file ---
    if not os.path.exists(test_cases_file):
        print(f"❌ Error: JSON file not found: {test_cases_file}")
        sys.exit(1)

    try:
        with open(test_cases_file, "r", encoding="utf-8") as f:
            test_cases = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Failed to parse JSON file: {e}")
        sys.exit(1)

    # --- Step 2: Validate structure ---
    if not isinstance(test_cases, list):
        print("❌ Error: JSON root must be a list of test case objects.")
        sys.exit(1)

    validation_errors = []
    validated_cases = []

    # --- Step 3: Validate each test case ---
    for idx, case in enumerate(test_cases, start=1):
        if not isinstance(case, dict):
            validation_errors.append(f"Test case #{idx}: must be a dictionary.")
            continue

        # Required fields
        required_fields = ["input_prompt", "expected_answer", "ai_generated_answer"]
        for field in required_fields:
            if field not in case or not isinstance(case[field], str) or not case[field].strip():
                validation_errors.append(f"Test case #{idx}: missing or invalid '{field}'.")
        
        # Skip further processing if required fields missing
        if any(f"#{idx}" in err for err in validation_errors):
            continue

        # Assign default optional fields
        prompt = case["input_prompt"]
        expected_answer = case["expected_answer"]
        ai_generated_answer = case["ai_generated_answer"]

        case["test_case_group"] = case.get("test_case_group", "default")
        case["test_case_name"] = case.get("test_case_name", prompt)
        case["background_context"] = case.get(
            "background_context",
            f"# Input Prompt:\n{prompt}\n\n---\n\n# Expected Answer:\n{expected_answer}"
        )
        case["ai_inferred_context"] = case.get(
            "ai_inferred_context",
            f"# Input Prompt:\n{prompt}\n\n---\n\n# AI-generated Answer:\n{ai_generated_answer}"
        )

        validated_cases.append(case)

    # --- Step 4: Report validation results ---
    if validation_errors:
        print("❌ Validation failed. The following issues were found in the test case definition file {test_cases_file}:\n")
        for err in validation_errors:
            print(f"  - {err}")
        sys.exit(1)

    print(f"✅ Successfully loaded {len(validated_cases)} test case(s).")
    return validated_cases

