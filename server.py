
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

if __name__=="__main__":
    print('Starting Python Flask server For Home Pricing Prediction....')
    app.run()