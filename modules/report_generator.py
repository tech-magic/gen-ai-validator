def generate_test_report(test_results, test_metrics):
    # Aggregate and print results
    print("\n=== Evaluation Results ===")
    total_scores = {name: 0.0 for name in test_metrics.keys()}
    num_cases = len(test_results)

    for idx, r in enumerate(test_results, 1):
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