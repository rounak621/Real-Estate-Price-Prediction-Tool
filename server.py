
from flask import flask; request; jsonify
import util

app=flask(__name__)

@app.route('/Get_location_name')
def Get_location_name():
    response=jsonify({
        'Locations':util.get_location_names()
    })
    response.headers.add('Access-control-allow-origin', '*')

    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft=float(request.form['total_sqft'])
    location=request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    return response

if __name__=="__main__":
    print('Starting Python Flask server For Home Pricing Prediction....')
    app.run()