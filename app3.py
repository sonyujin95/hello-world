from flask import Flask, request, render_template
from emp_mysql import empall2

app = Flask(__name__)

@app.route('/', methods=['get'])
def get():
    return render_template('reqres_mysql.html')  


@app.route("/empall2", methods=['get'])
def empall():
    return empall2()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")