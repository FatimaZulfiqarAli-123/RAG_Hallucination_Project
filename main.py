from qa_basic import basic_qa
from qa_rag import rag_qa
from hallucination import detect_hallucination, verify_answer
from confidence import confidence_score

questions = [
    "Where is the Eiffel Tower?",
    "What is the capital of Germany?",
    "Who invented the internet?"
]

for question in questions:
    print("\n==============================")
    print("Question:", question)

    # Basic QA
    basic_answer = basic_qa(question)
    print("\n=== WITHOUT RETRIEVAL ===")
    print(basic_answer)

    # RAG QA
    rag_answer, context = rag_qa(question)
    print("\n=== WITH RETRIEVAL ===")
    print(rag_answer)

    # Hallucination check
    print("\n=== HALLUCINATION CHECK ===")
    print("Rule-based:", detect_hallucination(rag_answer, context))
    print("Verification:", verify_answer(question, rag_answer, context))

    # Confidence score
    print("\n=== CONFIDENCE SCORE ===")
    print(confidence_score(rag_answer, context))

print("\n✅ DONE")