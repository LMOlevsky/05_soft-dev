from flask import Flask, render_template

app = Flask(__name__)

#render_template(<file>,<var1>,<var2>,...) returns a html template file as a string

@app.route("/")
def root():
    return render_template('base1.html')


if __name__ == '__main__':
	app.debug = True
	app.run()
