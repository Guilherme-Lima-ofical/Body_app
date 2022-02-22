#from crypt import methods
from flask import Flask, render_template, request

import pickle

with open ('model/bodyfatmodel.pkl', 'rb') as file:
    model = pickle.load(file)
file.close()



app = Flask(__name__,template_folder='templates')


@app.route('/', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        my_dict = request.form

        density = float(my_dict['density'])
        abdomen = float(my_dict['abdomen'])
        chest = float(my_dict['chest'])
        weight = float((my_dict['weight']))
        hip = float(my_dict['hip'])

        input_features = [[density, abdomen, chest, weight, hip]]
        prediction = model.predict(input_features)[0].round(2)
        
        string = 'O seu percentual de gordura corporal é de: ' + str(prediction)+'%'
        return render_template('show.html', string=string)

    return render_template('home.html')


if __name__ == "__main__":
    app.run()