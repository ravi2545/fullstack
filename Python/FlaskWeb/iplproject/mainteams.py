from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('login.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      n=request.form['name']
      p=request.form['psw']
      if n=='csk1':
         if p=='123':
            return render_template('homepage.html')
         else:
            return "Incorrect Password"

      elif n == 'mi2':
         if p == '1234':
            return render_template('homepage.html')
         else:
            return "Incorrect Password"

      elif n=='knt3':
         if p=='12345':
            return render_template('homepage.html')
         else:
            return "Incorrect Password"

      elif n=='srh4':
         if p=='123456':
            return render_template('homepage.html')
         else:
            return "Incorrect Password"

      elif n=='rr5':
         if p=='1234567':
            return render_template('homepage.html')
         else:
            return "Incorrect Password"

      elif n=='rcb6':
         if p=='12345678':
            return render_template('homepage.html')
         else:
            return "Incorrect Password"

      elif n=='kixp7':
         if p=='123456789':
            return render_template('homepage.html')
         else:
            return "Incorrect Password"

      elif n=='dd8':
         if p=='1234567890':
            return render_template('homepage.html')
         else:
            return "Incorrect Password"
      else:
         return "Incorrcet user"

@app.route('/add')
def ad():
    return render_template("add.html");


@app.route('/matches')
def mat():
   return render_template("add.html");


@app.route('/results')
def res():
   return render_template("add.html");


@app.route('/topruns')
def toprun():
    return render_template("add.html");

@app.route('/topbowls')
def topbowl():
   return render_template("add.html")

@app.route('/addplayerruns')
def addplayerrun():
   return render_template("add.html")

@app.route('/addplayerbowlings')
def addplayerbowling():
   return render_template("add.html")

@app.route('/viewplayer')
def viewplayers():
   return render_template("add.html")

@app.route('/addplayer',methods = ['POST', 'GET'])
def addpalyer():
   if request.method=='POST':
      pn=request.form['name']
      ids=request.form['idname']
      ty=request.form['tname']

if __name__ == '__main__':
   app.run(debug = True)