import pandas as pd


def analyze_trends():

    df = pd.read_csv("data/ai_news.csv")

    keywords = [
        "AI",
        "GPT",
        "Gemini",
        "OpenAI",
        "NVIDIA",
        "Meta",
        "Anthropic"
    ]

    trend_counts = {}

    for keyword in keywords:

        count = df["Title"].str.contains(
            keyword,
            case=False
        ).sum()

        trend_counts[keyword] = count

    trend_df = pd.DataFrame(
        list(trend_counts.items()),
        columns=["Keyword", "Count"]
    )

    return trend_df