from flask import Flask, render_template, request
from sqlalchemy import Column, Integer, String, Numeric, create_engine, text

app = Flask(__name__)

# initialize database
# connection string is in the format mysql://user:password@server/database
conn_str = "mysql://root:5676@localhost/cset"
engine = create_engine(conn_str, echo=True)
conn = engine.connect()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hello')
def great_name():
    return render_template("user.html")


@app.route('/boats')
def get_boats():
    boats = conn.execute(text("select * from boats")).all()
    print(boats)
    return render_template('boats.html', boats=boats[:10])


@app.route('/create', methods=['GET'])
def create_get_request():
    return render_template('boats_create.html')


@app.route('/create', methods=['POST'])
def create_boats():
    conn.execute(text("INSERT INTO boats VALUES (:id, :name, :type, :owner_id, :rental_price)"), request.form)
    conn.commit()
    return render_template('boats_create.html')


@app.route('/delete', methods=['GET'])
def delete_get_request():
    return render_template('boats_delete.html')


@app.route('/delete', methods=['POST'])
def delete_boats():
    conn.execute(text("DELETE from boats where id = :id"), request.form)
    conn.commit()
    return render_template('boats_delete.html')


if __name__ == '__main__':
    app.run(debug=True)
