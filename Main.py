"""Stock Manager.

Resources:
# https://docs.python.org/3/library/csv.html
# https://note.nkmk.me/en/python-datetime-isoformat-fromisoformat/
# https://stackoverflow.com/questions/2570269/output-alternatives-in-python
# https://docs.python.org/3/library/zoneinfo.html

Directions:
1. Download Flask
2. Open a terminal inside the unzipped folder
3. This Applications can only be used with MacOS.
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, render_template, abort
app = Flask(__name__)

Stock_Items = [
    {
        "date": datetime(2025, 9, 15, tzinfo=ZoneInfo("America/Indiana/Indianapolis")),
        "price": 249.99,
        "ticker": "GOOG",
        "quantity": 100,
        "transaction_id": 0,
    },
    {
        "date": datetime(2025, 9, 15, tzinfo=ZoneInfo("America/Indiana/Indianapolis")),
        "price": 239.71,
        "ticker": "AAPL",
        "quantity": 1200,
        "transaction_id": 1,
    },
    {
        "date": datetime(2025, 9, 16, tzinfo=ZoneInfo("America/Indiana/Indianapolis")),
        "price": 591.46,
        "ticker": "QQQ",
        "quantity": 800,
        "transaction_id": 2,
    },
    {
        "date": datetime(2025, 9, 16, tzinfo=ZoneInfo("America/Indiana/Indianapolis")),
        "price": 513.22,
        "ticker": "MSFT",
        "quantity": 900,
        "transaction_id": 3,
    },
]


@app.route("/")
def stocks() -> str:
    return render_template("stocks.html", data=Stock_Items)


@app.route("/transactions/<int:transaction_id>")
def transactions(transaction_id) -> str:
    if 0 <= transaction_id < len(Stock_Items):
        transaction_details = Stock_Items[transaction_id]
        return render_template("transactions.html", transaction=transaction_details, transaction_id=transaction_id)
    return abort(404)


if __name__ == "__main__":
    app.run(debug=True)
