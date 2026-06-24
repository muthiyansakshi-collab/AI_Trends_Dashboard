from news_fetcher import fetch_ai_news
from trend_analyzer import analyze_trends
from report_generator import generate_report
from llm_summarizer import generate_summary


def main():

    print("\n===== AI TRENDS DASHBOARD =====")

    fetch_ai_news()

    trend_df = analyze_trends()

    print("\nTrending Keywords:\n")
    print(trend_df)

    generate_report(trend_df)

    print("\nLLM Summary:\n")

    summary = generate_summary()

    print(summary)

    print("\nDashboard Completed Successfully!")


if __name__ == "__main__":
    main()