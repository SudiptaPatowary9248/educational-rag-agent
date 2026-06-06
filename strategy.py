def detect_strategy(query):
    q = query.lower()
    if any(word in q for word in [
        "example",
        "how does",
        "how do"
    ]):
        return "example"
    elif any(word in q for word in [
        "roc",
        "auc",
        "confusion matrix"
    ]):
        return "detailed"
    elif any(word in q for word in [
        "what is",
        "define"
    ]):
        return "simple"
    else:
        return "general"
