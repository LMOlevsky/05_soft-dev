from flask import Flask, render_template
from occ import toDictionary, pickOccupation

app = Flask(__name__)

#render_template(<file>,<var1>,<var2>,...) returns a html template file as a string
def dicToTable(dic):
    table = '<table style="width:100%"><tr><th>Job Class</th><th>Percentage</th></th></tr>'
    for key in dic:
        if(not(key == "Job Class")):
            table += "<tr><td>" + key + "<\td><td>" + str(dic[key]) + "</td></tr>"
    table += "</table>"
    return table

@app.route("/occupations")
def occupations():
    occ_table = ''
    dic = toDictionary("occupations.csv")
    pickedOcc = "<h3>" + pickOccupation(dic) + "</h3>"
    occ_table = dicToTable(dic)
    #return render_template('tableTemp.html',table=occ_table,occupation=pickedOcc)
    x =  render_template('tableTemp2.html')
    x += '\n'
    x += occ_table
    x += pickedOcc
    x += '</body></html>'
    return x


if __name__ == '__main__':
	app.debug = True
	app.run()
