from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    ContextualPrecisionMetric,
    ContextualRecallMetric,
    ContextualRelevancyMetric,
    HallucinationMetric,
    SummarizationMetric
)

from modules.judge_llm import get_judge_llm

def get_standard_genai_metrics():
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