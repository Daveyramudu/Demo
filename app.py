from logging import debug
from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("desk.db")    
c = conn.cursor()

#      c.execute("SELECT * FROM value")
#print(c.fetchall())

@app.route('/', methods=['GET',"POST"])
def home():
    conn = sqlite3.connect("desk.db")    
    c = conn.cursor()


    if request.method == "POST":
        num1 = request.form.get('num1')
        c.execute("INSERT INTO value (numbers) VALUES(?)",[num1])
        conn.commit
        num2 = request.form.get('num2')
        c.execute("INSERT INTO value (numbers) VALUES(?)",[num2])
        conn.commit
        
        add = int(num1) + int(num2)
        return render_template('result.html', add=add)
        c.execute("INSERT INTO value (numbers) VALUES(?)",[result])
        conn.commit
        
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True) 