import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        if ticker in self.portfolio:
            self.portfolio[ticker] += shares
        else:
            self.portfolio[ticker] = shares
        print(f"Added {shares} shares of {ticker} to your portfolio.")

    def remove_stock(self, ticker, shares):
        if ticker in self.portfolio:
            if shares >= self.portfolio[ticker]:
                del self.portfolio[ticker]
                print(f"Removed all shares of {ticker} from your portfolio.")
            else:
                self.portfolio[ticker] -= shares
                print(f"Removed {shares} shares of {ticker} from your portfolio.")
        else:
            print(f"{ticker} is not in your portfolio.")

    def get_portfolio(self):
        return self.portfolio

    def get_stock_price(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.history(period="1d")['Close'][0]

    def display_portfolio(self):
        print("\nYour Portfolio:")
        total_value = 0
        for ticker, shares in self.portfolio.items():
            price = self.get_stock_price(ticker)
            value = price * shares
            total_value += value
            print(f"{ticker}: {shares} shares @ ${price:.2f} = ${value:.2f}")
        print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main():
    portfolio = StockPortfolio()

    while True:
        print("Options: ")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            ticker = input("Enter the stock ticker symbol: ").upper()
            shares = int(input("Enter the number of shares: "))
            portfolio.add_stock(ticker, shares)
        elif choice == '2':
            ticker = input("Enter the stock ticker symbol: ").upper()
            shares = int(input("Enter the number of shares: "))
            portfolio.remove_stock(ticker, shares)
        elif choice == '3':
            portfolio.display_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
