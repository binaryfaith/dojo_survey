from flask import Flask,render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result',methods = ['GET','POST'] )
def user_info():

    name = request.form['name']
    email = request.form['email']
    textbox = request.form['textbox']


    return  render_template("result.html", name = name,email=email,textbox=textbox)
    return  redirect("/")


app.run(debug=True)



       
