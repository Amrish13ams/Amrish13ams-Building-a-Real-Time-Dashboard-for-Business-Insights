import pandas as pd

def get_metrics():
    # Replace this with real-time data fetching logic
    data = pd.read_csv('data/sample_data.csv')
    metrics = {
        "total_sales": data['sales'].sum(),
        "total_visitors": data['visitors'].sum(),
        "conversion_rate": (data['sales'].sum() / data['visitors'].sum()) * 100 if data['visitors'].sum() > 0 else 0,
    }
    return metrics
