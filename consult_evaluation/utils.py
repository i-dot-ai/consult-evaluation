from typing import List


# TODO - should punctuation be removed?
def tokenize_docs(docs: List[str]) -> List[List[str]]:
    return [doc.lower().split() for doc in docs]
