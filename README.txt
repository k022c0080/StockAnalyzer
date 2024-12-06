README

株価予測と感情分析ツール

概要

このプロジェクトは、株式市場データとニュース記事の感情分析を組み合わせて、翌日の株価を予測するツールです。Pythonを使用し、以下の主要なライブラリと技術を活用しています：

NewsAPI: 最新ニュースの取得

VADER Sentiment Analyzer: ニュース記事の感情分析

yfinance: 株価データの取得

Random Forest Regressor: 株価予測モデル

Matplotlib: データの可視化

本ツールは、ニュースの感情スコアと株価データを組み合わせて学習し、翌日の株価を予測する機能を提供します。また、可視化機能により、モデルのパフォーマンスやデータの傾向を直感的に把握できます。ディレクトリ構成
Portfolio
│
├── /src
│   ├── main.py
│   ├── Visualizer.py
│   └── その他のコードファイル
│
└── /images
    ├── Stock_Price_vs_Sentiment_Score_with_Today.png
    ├── Residual_Plot.png
    └── その他の画像ファイル



出力されるグラフとその意味

1. Residual Plot (残差プロット)

概要: 予測値と実際の値の差（残差）を可視化したグラフ。

意味: モデルの予測がどの程度実際の値と一致しているかを示します。

残差が0に近いほど予測精度が高い。

データがランダムに分布していれば、モデルが適切であることを示します。

保存先: images/Residual_Plot.png

2. Feature Importance Plot (特徴量の重要度プロット)

概要: モデルが予測においてどの特徴量を重視しているかを示したグラフ。

意味: 株価の予測において、感情スコアや株価データのどちらが重要かを理解するのに役立ちます。

保存先: images/Feature_Importance.png

3. Stock Price vs Sentiment Score (株価と感情スコアの比較プロット)

概要: 株価と感情スコアの推移を同じグラフ上で可視化。

意味: 感情スコアの変化が株価に与える影響を直感的に把握できます。

青色の線: 実際の株価データ（終値）。

緑色の線: ニュース記事の感情スコア（compound平均）。

赤色の破線: 予測された翌日の株価。

紫色の縦線: 今日の日付を示します。

保存先: images/Stock_Price_vs_Sentiment_Score_with_Today.png



