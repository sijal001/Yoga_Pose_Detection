from flask import Flask,render_template,url_for,request
import pandas as pd 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def dash_board():
    if request.method == 'GET':
        return render_template("index.html")
    
    elif request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        age = request.form['age']
        weight = request.form['weight']
        height = request.form['height']
        feed_type = request.form['feed_type']
        return render_template('Dashboard.html',f_name=first_name,l_name=last_name,age_info=age,weight_info=weight,height_info=height)


if __name__ == '__main__':
	app.run(debug=True)