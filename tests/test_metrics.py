from consult_evaluation.utils import tokenize_docs
from consult_evaluation.unsupervised.metrics import calculate_coherence


def test_calculate_coherence_with_valid_inputs(bertopic_mapping, question_responses):
    texts = tokenize_docs(question_responses)
    coherence_score = calculate_coherence(bertopic_mapping, texts)
    assert coherence_score > 0
    assert coherence_score < 1
