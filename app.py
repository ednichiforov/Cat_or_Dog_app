from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
git
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_SRI"]="sqlite:///test.db"
db = SQLAlchemy(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
