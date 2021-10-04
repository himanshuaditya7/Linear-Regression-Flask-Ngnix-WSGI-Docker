# from flask import Flask
import pandas as pd
import numpy as np
import sklearn
import joblib
from flask import Flask,render_template,request,jsonify
app = Flask(__name__)
# from app import app


@app.route('/', methods=['GET'])
def server_is_up():
	if request.method == 'GET':
		return 'server is up'

# @app.route('/predict',methods=['GET','POST'])
# def predict(): 
# 	if request.method == 'POST':
# 		print(request.form.get('var_1'))
# 		print(request.form.get('var_2'))
# 		print(request.form.get('var_3'))
# 		print(request.form.get('var_4'))
# 		print(request.form.get('var_5'))
# 		try:
# 			var_1 = float(request.form['var_1'])
# 			var_2 = float(request.form['var_2'])
# 			var_3 = float(request.form['var_3'])
# 			var_4 = float(request.form['var_4'])
# 			var_5 = float(request.form['var_5'])
# 			pred_args = [var_1, var_2, var_3, var_4, var_5]
# 			pred_arr = np.array(pred_args)
# 			preds = pred_arr.reshape(1, -1)
# 			model = open("inear_regression_model.pkl","rb")
# 			lr_model = joblib.load(model)
# 			model_prediction = lr_model.predict(preds)
# 			model_prediction = round(float(model_prediction), 2)
# 			return jsonify(model_prediction)
# 		except ValueError:
# 			return "Please Enter valid values"


@app.route('/check',methods=['GET','POST'])
def check():
	if request.method == "POST":
		in_varibale = [float(i) for i in request.form.values()]
		pred_arr = np.array(in_varibale)
		preds = pred_arr.reshape(1,-1)
		model = open("inear_regression_model.pkl","rb")
		lr_model = joblib.load(model)
		model_prediction = lr_model.predict(preds)
		model_prediction = round(float(model_prediction),2)
		return jsonify(model_prediction)


if __name__ == '__main__':
	app.run(debug=True)
