import pandas as pd


def fetch_ai_news():

    news_data = [
        {
            "Title": "OpenAI launches new GPT model",
            "Source": "OpenAI"
        },

        {
            "Title": "Google Gemini AI expands capabilities",
            "Source": "Google"
        },

        {
            "Title": "NVIDIA introduces AI chips",
            "Source": "NVIDIA"
        },

        {
            "Title": "Meta invests heavily in Generative AI",
            "Source": "Meta"
        },

        {
            "Title": "Anthropic releases Claude updates",
            "Source": "Anthropic"
        }

    ]

    df = pd.DataFrame(news_data)

    df.to_csv(
        "data/ai_news.csv",
        index=False
    )

    print("AI news fetched successfully!")

    return df