import pytest


@pytest.fixture
def question_responses():
    docs = [
        "Great food and drinks, pizza is on point!",
        "Super tasty food, lovely pizza.",
        "Actually surprised how good the drinks were, strong cocktails!",
        "I really liked the cheese on the pizza.",
        "The beer was alright, but I've had nicer lagers.",
        "Enjoyed the atmosphere, great vibe!",
        "Pleasant customer service and always attentive.",
        "The no pepperoni vegan option was fantastic, would definietly recommend!",
        "The crust was pretty yummy!",
        "I had an ale with my pizza, but it wasn't cold enough.",
        "The service staff were very friendly and I always felt like I had their attention.",
        "I would go back again, the cozy decor made it feel like home.",
        "Loved the atmosphere, great music!",
        "If I could ask for one thing it would be a stout or porter!",
        "Love the vibe!",
        "Really tasty, but the waiter was a bit slow to take our order.",
        "The waiter was very helpful with suggestions."
        "Loved the pizza crust and extra cheese!",
        "My kind of vibe, great atmosphere and music.",
        "Would go back just for beer, especially the lager!",
        "Not sure about the decor, perhaps not my taste. But the music and vibe was great.",
        "Couldn't get better service than that. The staff were super accomodating and friendly."
    ]
    return docs


@pytest.fixture
def bertopic_mapping():
    mapping = {
        "1": ["pizza", "cheese", "crust", "pepperoni", "tasty"],
        "2": ["beer", "brew", "lager", "stout", "porter"],
        "3": ["service", "waiter", "staff", "helpful", "prompt"],
        "4": ["atmosphere", "decor", "music", "cozy", "vibe"],
    }
    return mapping
