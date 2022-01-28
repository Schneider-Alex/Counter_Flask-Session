from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
# our index route will handle rendering our form
app.secret_key = 'keep it secret, keep it safe'



@app.route('/')
def index():
    if "counterval" not in session:
        session['counterval'] = 0
    else:
        session['counterval'] += 1
    return render_template("index.html")


@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

@app.route('/plustwo', methods=['POST'])
def plustwo():
    session['counterval']+=1
    return redirect('/')

# @app.route('/userchoice',methods=['POST'])
# def userinput():
#     session['counterval']+= int(index.userval)
#     return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)