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
            return "yes"
         else:
            return "Incorrect Password"

      elif n == 'mi2':
         if p == '1234':
            return "Yes"
         else:
            return "Incorrect Password"

      elif n=='knt3':
         if p=='12345':
            return "Yes"
         else:
            return "Incorrect Password"

      elif n=='srh4':
         if p=='123456':
            return "Yes"
         else:
            return "Incorrect Password"

      elif n=='rr5':
         if p=='1234567':
            return "Yes"
         else:
            return "Incorrect Password"

      elif n=='rcb6':
         if p=='12345678':
            return "Yes"
         else:
            return "Incorrect Password"

      elif n=='kixp7':
         if p=='123456789':
            return "Yes"
         else:
            return "Incorrect Password"

      elif n=='dd8':
         if p=='1234567890':
            return "Yes"
         else:
            return "Incorrect Password"
      else:
         return "Incorrcet user"

      # elif n=='mi2':
      #    if p=='1234':
      #       return "Yes"
      #
      # elif n=='knt3':
      #    if p==''



if __name__ == '__main__':
   app.run(debug = True)