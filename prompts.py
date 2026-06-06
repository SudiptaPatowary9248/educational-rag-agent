def build_prompt(strategy, context, query):

    if strategy == "simple":
        return f"""
        You are an educational AI assistant.

        Use the provided context as the PRIMARY source.

        Give a short and beginner-friendly explanation.

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

    elif strategy == "example":
        return f"""
        You are an educational AI assistant.

        Use the provided context as the PRIMARY source.

        Explain clearly using a simple example.

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

    elif strategy == "detailed":
        return f"""
        You are an educational AI assistant.

        Use the provided context as the PRIMARY source.

        Give a detailed conceptual explanation.

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

    else:
        return f"""
        You are an educational AI assistant.

        Use the provided context as the PRIMARY source.

        Explain clearly and accurately.

        Context:
        {context}

        Question:
        {query}

        Answer:
        """
