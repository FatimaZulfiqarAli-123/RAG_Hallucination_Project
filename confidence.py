def confidence_score(answer, context):
    if not answer or not context:
        return 0.0

    answer_words = set(answer.lower().split())
    context_words = set(context.lower().split())

    overlap = len(answer_words & context_words)

    return round(overlap / max(len(answer_words), 1), 2)