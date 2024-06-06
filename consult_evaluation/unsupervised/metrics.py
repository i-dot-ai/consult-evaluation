
from typing import List, Dict

from gensim.models import CoherenceModel
from gensim.corpora import Dictionary


def calculate_coherence(topics: Dict[str, List[str]], texts: List[List[str]]) -> float:
    """Calculate the c_v coherence of the topics and texts.

    This gives a sense of the interpretability of the topics generated.

    Args:
        topics: Mapping of BERTopic topic to keywords.
        texts: List of documents (free-text responses), each doc is a list of tokens.

    Returns:
        float: A coherence score.
    """
    # At the moment ID is a string - from data download can use UUID or topic_id
    # to identify.
    topic_keywords = list(topics.values())
    print(f"topic_keywords: {topic_keywords}")
    vocab = Dictionary(texts)
    coherence_model = CoherenceModel(
        topics=topic_keywords,
        texts=texts,
        dictionary=vocab,
        coherence="c_v",
    )
    coherence_score = coherence_model.get_coherence()
    return coherence_score
