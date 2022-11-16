from flask import Flask, render_template

from flask import Flask
app=Flask("alo mundo")
@app.route("/")
def alunos():
   return render_template("hello.html")