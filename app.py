from flask import Flask


app=Flask(__name__)

@app.route('/sai')



def fun():
    return "welcome to my world"


if __name__ =="__main__":
    app.run(debug=True)