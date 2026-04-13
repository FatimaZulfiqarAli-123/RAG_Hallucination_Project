def basic_qa(question):
    knowledge = {
        "Where is the Eiffel Tower?": "The Eiffel Tower is in Paris.",
        "What is the capital of Germany?": "Berlin is the capital of Germany.",
        "Who invented the internet?": "Vint Cerf contributed to the invention of the internet."
    }

    return knowledge.get(question, "I don't know.")