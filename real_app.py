#It should be very simple: 1)user goes to app URL, user presses a button, 
#the script is run and the result is displayed in the browser, 
# button press again, new result.

from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import random
import csv

#DATABASE = 'immigration_vocabulary.csv' #configuration

app = Flask(__name__)

#app.config.from_object(__name__) # pulls in configurations by looking for UPPERCASE variables

#def connect_csv():
#    return csv.connect(app.config['DATABASE'])

@app.route('/main')
def main():
    file_name = 'immigration_vocabulary.csv' #this needs to be set to the current path
    dict_list = []

    with open(file_name, 'rb') as fd:
        reader = csv.DictReader(fd)
        for line in reader:
            dict_list.append(line)        
        
    ands = ['Through','Beyond','Eternal','When','Explorations of','The Origins of','The Future of'] 
    ors = ['and','or','without', 'since','under the','with']
    discp = ['A Hisory of','Gender and','The Political Economy of','A Discourse on','The Politics of','Outline of a Theory of']
    word1 = random.choice(dict_list)
    word2 = random.choice(dict_list)
    ands1 = random.choice(ands)
    disp1 = random.choice(discp)
    ors1 = random.choice(ors)
    word3 = random.choice(dict_list)


    choice = ' '+ands1+' '+ word1['Word']+' '+ors1+' '+word2['Word']+' - '+disp1+' '+ word3['Word']
    #print choice
    return render_template('main.html', choice=choice)

if __name__ == '__main__':
    app.run()
    #app.run(debug=True) # if you want to debug the flask app.