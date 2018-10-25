from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/shop')
def shopping_page():
    return render_template("shop.html")
   
   
@app.route('/support')
def contactus_page():
    return render_template("support.html")

if __name__ == '__main__':
   app.run(debug = True)