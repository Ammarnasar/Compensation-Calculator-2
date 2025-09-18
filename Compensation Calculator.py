from flask import Flask, render_template, request

app = Flask(__name__)

# Compensation rates
compensation_rates = {
    "Main Dish": 0.8,
    "Side Dish": 0.5,
    "Drink": 0.3,
    "Cutlery": 0.1,
    "Sauce": 0.0
}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            combo_price = float(request.form["combo_price"])
            missing_item = request.form["missing_item"]
            compensation_type = request.form["compensation_type"]
            status = request.form["status"]

            rate = compensation_rates.get(missing_item, 0)
            compensation = combo_price * rate

            result = {
                "Missing Item": missing_item,
                "Combo Price": f"{combo_price:.2f} SAR",
                "Status": status,
                "Compensation Type": compensation_type,
                "Compensation Rate": f"{rate*100:.0f}%",
                "Compensation Amount": f"{compensation:.2f} SAR"
            }
        except ValueError:
            result = {"Error": "Please enter a valid price"}

    return render_template("index.html", result=result)

if __name__ == "__main__":
    # تشغيل السيرفر على localhost فقط، بدون رابط الشبكة
    app.run(debug=True)
