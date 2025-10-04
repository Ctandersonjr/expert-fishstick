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
from html import escape

from zoneinfo import ZoneInfo

from flask import Flask, render_template, abort
from flask import request, redirect
from werkzeug.wrappers import Response as WerkzeugResponse

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


def get_item_component(transaction):
    return f"""
        <li>
        <form action="/" method="post" style="display:inline">
            <input type="hidden" name="del_item" value="{transaction["transaction_id"]}">
            <input type="submit" value="Mark Complete">
            <span>{escape(transaction["ticker"])} - {transaction["quantity"]} @ {transaction["price"]}</span>
        </form>
        </li>
    """


@app.get("/")
def stocks() -> str:
    return render_template("stocks.html", data=Stock_Items)


@app.post("/transactions/<int:transaction_id>")
def delete(transaction_id) -> WerkzeugResponse:
    deleted_id = [
        item for item in Stock_Items if item["transaction_id"] == transaction_id
    ][0]
    Stock_Items.remove(deleted_id)
    return redirect("/", code=302)


@app.post("/transactions")
def labels():
    ticker = request.form.get("ticker")
    price = request.form.get("price")
    quantity = request.form.get("quantity")



    new_transaction = {
        "date": datetime.now(tz=ZoneInfo("America/Indiana/Indianapolis")),
        "price": float(price),
        "ticker": ticker.upper().strip(),
        "quantity": int(quantity),
        "transaction_id": len(Stock_Items),
    }
    Stock_Items.append(new_transaction)
    return redirect("/", code=303)


@app.get("/transactions/<int:transaction_id>")
def transactions(transaction_id) -> str:
    transaction_details = next(
        iter(
            [item for item in Stock_Items if item["transaction_id"] == transaction_id]
        ),
        None,
    )
    if transaction_details:
        return render_template(
            "transactions.html",
            transaction=transaction_details,
            transaction_id=transaction_id,
        )
    return abort(404)


def greet(name: str) -> str:
    return f"hello, {name}"


if __name__ == "__main__":
    app.run(debug=True)
