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

from flask import Flask, render_template

app = Flask(__name__)

Stock_Items = [
    {
        "date": datetime(2025, 9, 15, tzinfo=ZoneInfo("America/Indiana/Indianapolis")),
        "price": 249.99,
        "ticker": "GOOG",
        "quantity": 100,
    },
    {
        "date": datetime(2025, 9, 15, tzinfo=ZoneInfo("America/Indiana/Indianapolis")),
        "price": 239.71,
        "ticker": "AAPL",
        "quantity": 1200,
    },
    {
        "date": datetime(2025, 9, 16, tzinfo=ZoneInfo("America/Indiana/Indianapolis")),
        "price": 591.46,
        "ticker": "QQQ",
        "quantity": 800,
    },
    {
        "date": datetime(2025, 9, 16, tzinfo=ZoneInfo("America/Indiana/Indianapolis")),
        "price": 513.22,
        "ticker": "MSFT",
        "quantity": 900,
    },
]


@app.route("/")
def stocks():
    return render_template("stocks.html", data=Stock_Items)


if __name__ == "__main__":
    app.run(debug=True)
