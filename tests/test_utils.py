from consult_evaluation.utils import tokenize_docs


def test_tokenize_docs():
	input = ["First document.", "The sky is blue.", "The sun is shining."]
	expected = [["first", "document."], ["the", "sky", "is", "blue."], ["the", "sun", "is", "shining."]]
	actual = tokenize_docs(input)
	assert actual == expected
