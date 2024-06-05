# Evaluation approach

## Evaluation metrics

### Unsupervised
The evalutation will look at the following metrics:

- **Topic Coherence**: how closely related the words of the topics are and how interpretable that is for a human. 

It specifically uses C_v, which segments the top words of a topic into subsets. It then calculates co-occurence within a sliding window. This is converted to PMI (Pointwise Mutual Information), assessing the rate of co-occurence in comparison to chance. These are used to produce vectors which are compared to one-another using cosine similarity. The outputs are then aggregated into a single score.

- **Topic Diversity**: how unique are the words between topics and is there overlap. Expressed as a number between 0 and 1, where 1 is maximum diversity.


### Supervised
Where there is ground truth data (human-coded data), it can also provide a classification style evaluation with the following metrics:

- **NMI**: A metric borrowed from information theory, which observes the shared information content between the two sets. Used for comparing clustering.
- **ARI**: Adjusted random index allows you to compare clustering between results, and account for assignment by chance.
- **Precision**: The ratio of correctly predicted positives to predicted positives.
- **Recall**: The ratio of true positives to all possible positives.
- **f1 score: The harmonic mean of the precision and recall.

These can be produced in two approaches: 

1. Ask an LLM to map the BERTopic topics and corresponding tags, back to their closest human equivalent.
2. Generate embeddings and compute the cosine simarity between the topics. Then compute the optimal mapping using the Hungarian method. The output from this mapping is fed into the classification evaluation metrics.