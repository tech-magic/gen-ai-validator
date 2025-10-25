import os
import pandas as pd
import altair as alt

def generate_test_report(test_results, test_metrics, output_dir="reports"):
    os.makedirs(output_dir, exist_ok=True)

    print("\n=== Generating Reports ===")

    # Collect scores for all metrics (for aggregated report)
    all_metric_scores = []

    total_scores = {name: 0.0 for name in test_metrics.keys()}
    num_cases = len(test_results)

    for idx, r in enumerate(test_results, 1):
        # === Individual Report ===
        case_filename = os.path.join(output_dir, f"test_case_{idx}.md")
        with open(case_filename, "w", encoding="utf-8") as f:
            f.write(f"# 🧪 Test Case {idx}\n\n")
            f.write(f"### 🧾 Input Prompt\n```text\n{r['input_prompt']}\n```\n")
            f.write(f"### ✅ Expected Answer\n```text\n{r['expected_answer']}\n```\n")
            f.write(f"### 🤖 AI-generated Answer\n```text\n{r['ai_generated_answer']}\n```\n")
            f.write(f"### 📘 Source of Truth\n```text\n{r['source_of_truth']}\n```\n")
            f.write(f"### 🔍 AI-inferred Truth\n```text\n{r['ai_inferred_truth']}\n```\n")

            f.write("## 📊 Evaluation Metrics\n\n")
            for m in r["metrics"]:
                metric_name = m["metric"]
                score = m["score"]
                reason = m["reason"]

                f.write(f"### {metric_name}\n")
                f.write(f"- **Score:** {score:.2f}\n")
                f.write(f"- **Reason:** {reason}\n\n")

                # accumulate for aggregation
                total_scores[metric_name] += score
                all_metric_scores.append({
                    "Test Case": idx,
                    "Metric": metric_name,
                    "Score": score
                })

        print(f"✅ Generated individual report: {case_filename}")

    # === Summary of averages ===
    summary_filename = os.path.join(output_dir, "summary_metrics.md")
    with open(summary_filename, "w", encoding="utf-8") as f:
        f.write("# 📈 Average Metric Scores\n\n")
        for metric_name, total in total_scores.items():
            avg = total / num_cases
            f.write(f"- **{metric_name}:** {avg:.2f}\n")
        f.write("\n")
    print(f"✅ Generated summary metrics: {summary_filename}")

    # === Aggregated Report (Horizontal Box Plot) ===
    df = pd.DataFrame(all_metric_scores)
    if not df.empty:
        chart = (
            alt.Chart(df)
            .mark_boxplot(extent="min-max", size=30)
            .encode(
                y=alt.Y("Metric:N", title="Metric Name", sort="-x"),
                x=alt.X("Score:Q", title="Score", scale=alt.Scale(domain=[-0.2, 1.2])),
                color=alt.Color("Metric:N", legend=None)
            )
            .properties(
                title="📊 Distribution of Metric Scores Across All Test Cases",
                width=700,
                height=400
            )
        )

        html_file = os.path.join(output_dir, "aggregated_metrics.html")
        chart.save(html_file)
        print(f"✅ Generated aggregated box plot: {html_file}")
    else:
        print("⚠️ No metrics found to plot.")

    print("\n=== All reports generated successfully! ===")
