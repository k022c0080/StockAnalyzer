import matplotlib.pyplot as plt
import os

class Visualizer:
    def __init__(self):
        # 保存先ディレクトリ
        self.image_dir = "../images"
        # ディレクトリが存在しない場合は作成
        os.makedirs(self.image_dir, exist_ok=True)

    def plot_residuals(self, y_pred, residuals):
        plt.scatter(y_pred, residuals)
        plt.axhline(0, color="red", linestyle="--")
        plt.xlabel("Predicted Stock Price")
        plt.ylabel("Residuals")
        plt.title("Residual Plot")
        output_path = os.path.join(self.image_dir, "Residual_Plot.png")
        plt.savefig(output_path)  # 正しいディレクトリに保存
        plt.show()

    def plot_feature_importance(self, importances, features):
        plt.barh(features, importances, color="green")
        plt.xlabel("Feature Importance")
        plt.ylabel("Features")
        plt.title("Feature Importance in Stock Price Prediction")
        output_path = os.path.join(self.image_dir, "Feature_Importance.png")
        plt.savefig(output_path)  # 正しいディレクトリに保存
        plt.show()

    def plot_stock_vs_sentiment(self, dates, stock_data, predicted_price, current_date):
        fig, ax1 = plt.subplots(figsize=(10, 6))

        # 株価のプロット
        ax1.set_xlabel("Date")
        ax1.set_ylabel("Stock Price (USD)", color="blue")
        ax1.plot(dates, stock_data["Close"], label="Actual Close Price", color="blue")
        ax1.tick_params(axis="y", labelcolor="blue")

        # 感情スコアのプロット (右のy軸)
        ax2 = ax1.twinx()
        ax2.set_ylabel("Sentiment Score", color="green")
        ax2.plot(dates, stock_data["compound_average"], label="Sentiment Score", color="green")
        ax2.tick_params(axis="y", labelcolor="green")

        # 予測された株価を赤い破線で表示
        ax1.axhline(y=predicted_price, color="red", linestyle="--", label="Predicted Close Price", alpha=0.5)

        # 今日の日付に縦線を引く
        ax1.axvline(x=current_date, color="purple", linestyle="--", label="Today", alpha=0.7)

        # グラフのタイトルと凡例
        fig.suptitle("Stock Price vs Sentiment Score")
        ax1.legend(loc="upper left")
        ax2.legend(loc="upper right")

        # 日付のフォーマットを調整
        fig.autofmt_xdate()

        # グラフを保存
        output_path = os.path.join(self.image_dir, "Stock_Price_vs_Sentiment_Score_with_Today.png")
        plt.savefig(output_path)  # 正しいディレクトリに保存
        plt.grid(True)
        plt.show()
