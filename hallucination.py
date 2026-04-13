def detect_hallucination(answer, context):
    if answer.lower() in context.lower():
        return False
    return True


def verify_answer(question, answer, context):
    if answer.lower() in context.lower():
        return "YES"
    return "NO"