def generate_report(trend_df):

    trend_df.to_csv(
        "reports/trend_report.csv",
        index=False
    )

    print("Trend report generated successfully!")