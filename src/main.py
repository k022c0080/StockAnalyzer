from NewsFetcher import NewsFetcher
from SentimentAnalyzer import SentimentAnalyzer
from StockPredictor import StockPredictor
from Visualizer import Visualizer
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd
from sklearn.model_selection import train_test_split

# 定数定義
API_KEY = "1fb313cf0c4b49658908852a2950e8dc"
QUERY = "AAPL"
PERIOD = "1mo"
current_date = datetime.today()
one_month_ago = current_date - relativedelta(months=1)

# 各クラスのインスタンス作成
news_fetcher = NewsFetcher(API_KEY)
sentiment_analyzer = SentimentAnalyzer()
stock_predictor = StockPredictor(QUERY, PERIOD)
visualizer = Visualizer()

# ニュースと株価データを取得
articles = news_fetcher.fetch_news(QUERY, one_month_ago, current_date)
stock_data = stock_predictor.fetch_stock_data()

if __name__ == '__main__':
    if stock_data is not None:
        start_date = current_date - relativedelta(months=1)
        compound_averages = []
        
        for i in range(len(stock_data)):
            date = start_date + timedelta(days=i)
            date_str = date.strftime("%Y-%m-%d")
            next_day_str = (date + timedelta(days=1)).strftime("%Y-%m-%d")
            
            daily_articles = news_fetcher.fetch_news(QUERY, date_str, next_day_str)
            compound_avg = sentiment_analyzer.analyze_sentiment(daily_articles)
            compound_averages.append(compound_avg)
        
        stock_data["compound_average"] = compound_averages
        stock_data["Tomorrow"] = stock_data["Close"].shift(-1)
        stock_data = stock_data.dropna()

        X = stock_data[["Close", "compound_average"]]
        y = stock_data["Tomorrow"]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = stock_predictor.train_model(X_train, y_train)
        y_pred = model.predict(X_test)
        residuals = y_test - y_pred

        # プロット
        visualizer.plot_residuals(y_pred, residuals)
        visualizer.plot_feature_importance(model.feature_importances_, ["Close", "compound_average"])
        
        predicted_price = model.predict(pd.DataFrame([stock_data[["Close", "compound_average"]].iloc[-1].values], 
                                                    columns=["Close", "compound_average"]))[0]
        visualizer.plot_stock_vs_sentiment(stock_data.index, stock_data, predicted_price,current_date)
        print(f"予測された翌日の株価: {predicted_price}")