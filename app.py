import io
import base64
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import yfinance as yf
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    graph_url = None
    stock_info = None
    error_message = None
    
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        try:
            stock = yf.Ticker(symbol)
            history = stock.history(period="6mo")
            
            if history.empty:
                error_message = f"{symbol} Data not found for this. Please enter a valid stock symbol."
            else:
                stock_info = {
                    "name": stock.info.get("longName", "Unknown Company"),
                    "current_price": stock.info.get("currentPrice", "Current Price Unknown"),
                    "currency": stock.info.get("currency", "N/A")
                }

                plt.figure(figsize=(10, 6))
                history['Close'].plot(title=f"{symbol} Price Chart", color='blue', lw=2)
                plt.xlabel("Date")
                plt.ylabel(f"Price ({stock_info['currency']})")
                plt.grid(visible=True, linestyle='--', alpha=0.7)
                plt.tight_layout()

                img = io.BytesIO()
                plt.savefig(img, format="png")
                img.seek(0)
                graph_url = base64.b64encode(img.getvalue()).decode()  
                plt.close()

        except Exception as e:
            error_message = f"An error occurred: {e}. Please make sure you entered a valid symbol.."

    return render_template("index.html", graph_url=graph_url, stock_info=stock_info, error_message=error_message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
 
 
 
 
    
