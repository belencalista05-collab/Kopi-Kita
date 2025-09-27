from flask import Flask, render_template, request
from datetime import datetime
import pytz

app = Flask(__name__)

menu_prices = {
    "Kopi Susu": 18000,
    "Americano": 15000,
    "Latte": 22000
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    tz = pytz.timezone("Asia/Jakarta")
    now = datetime.now(tz).strftime("%d-%m-%Y %H:%M:%S")
    if request.method == "POST":
        try:
            qty_susu = int(request.form.get("kopisusu", 0))
            qty_ame = int(request.form.get("americano", 0))
            qty_latte = int(request.form.get("latte", 0))
            day = request.form.get("day", "").lower()
            member = request.form.get("member") == "yes"

            subtotal = qty_susu*menu_prices["Kopi Susu"] + qty_ame*menu_prices["Americano"] + qty_latte*menu_prices["Latte"]

            promo = 5000 if subtotal > 50000 else 0
            after_promo = subtotal - promo

            disc_wed = 0
            if day in ["rabu", "wednesday"]:
                disc_wed = 0.10 * after_promo
            after_wed = after_promo - disc_wed

            disc_mem = 0
            if member:
                disc_mem = 0.05 * after_wed

            final_total = after_wed - disc_mem

            result = {
                "subtotal": subtotal,
                "promo": promo,
                "disc_wed": disc_wed,
                "disc_mem": disc_mem,
                "final_total": final_total,
                "kasir": "Belen",
                "tanggal": now
            }
        except Exception as e:
            result = {"error": str(e)}
    return render_template("index.html", menu=menu_prices, result=result)

if __name__ == "__main__":
    app.run(debug=True)
