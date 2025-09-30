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

def get_item_component(item_text):
    safe_text = escape(item_text)
    return f"""
        <li>
        <form action="/items" method="post" style="display:inline">
            <input type="hidden" name="item_del" value="{safe_text}">
            <input type="submit" value="Mark Complete">
            <span>{safe_text}</span>
        </form>
        </li>
    """

@app.route("/", methods=["GET","POST"])
def stocks() -> str:
     global Stock_Items
     if request.method == "POST":
        ticker = request.form.get("item_add")
        del_item = request.form.get("item_del")

        if ticker:
            ticker = ticker.strip()
            if ticker:
                new_transaction = {
                    "date": datetime.now(tz=ZoneInfo("America/Indiana/Indianapolis")),
                    "price": 0.0,
                    "ticker": ticker.upper,
                    "quantity": 0,
                    "transaction_id": len(Stock_Items),
                    }
                Stock_Items.append(new_transaction)

        elif del_item:
            try:
                del_item = int(del_item)
                Stock_Items = [item for item in Stock_Items if item["transaction_id"] != del_item]
            except ValueError:
                pass
        return redirect("/")
     
     return render_template("stocks.html", data=Stock_Items)


@app.route("/transactions/<int:transaction_id>", methods=["GET","POST"], methods=["GET"])
def transactions(transaction_id) -> str:

    if 0 <= transaction_id < len(Stock_Items):
        transaction_details = Stock_Items[transaction_id]
        return render_template("transactions.html", transaction=transaction_details, transaction_id=transaction_id)
    return abort(404)



if __name__ == "__main__":
    app.run(debug=True)
