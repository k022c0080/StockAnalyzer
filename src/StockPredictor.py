import yfinance as yf
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

class StockPredictor:
    def __init__(self, query, period):
        self.query = query
        self.period = period

    def fetch_stock_data(self):
        try:
            ticker = yf.Ticker(self.query)
            return ticker.history(period=self.period)
        except Exception as e:
            print(f"Error fetching stock data: {e}")
            return None

    def train_model(self, X_train, y_train):
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model
