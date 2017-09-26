from flask import Flask, render_template
from occ import toDictionary, pickOccupation

app = Flask(__name__)

#render_template(<file>,<var1>,<var2>,...) returns a html template file as a string
def dicToTable(dic):
    

@app.route("/occupations")
def occupations():
    occ_table = ''
    dic = toDictionary("occupations.csv")
    pickedOcc = pickOccupation(dic)
    occ_table = dicToTable(dic)
    return render_template('tableTemp.html',table=occ_table,occupation=pickedOcc)


if __name__ == '__main__':
	app.debug = True
	app.run()
