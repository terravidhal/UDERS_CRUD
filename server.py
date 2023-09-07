from flask import Flask, render_template,redirect, request #add request
# import the class from user.py
from user import Users 

app = Flask(__name__)


@app.route("/")
def home():
   return redirect('/users')


@app.route("/users")
def index():
   users = Users.get_all()
   return render_template("index.html",all_Users = users)


@app.route("/users/new")
def create_new_user():
   return render_template("create.html")



@app.route('/new', methods=["POST"])
def create():
    datass = {
        "fname": request.form["inputName4"],
        "lname": request.form["inputlast_name4"],
        "eml": request.form["inputEmail"]
    }
    Users.create_user(datass)
    return redirect('/')


@app.route('/user/show/<int:user_id>')
def show(user_id):
    data = {'id': user_id}
    user = Users.get_one(data)
    return render_template("show_user.html", User = user)
    


@app.route('/user/update/<int:user_id>')
def show_update_page(user_id):
    data = {'id': user_id}
    user = Users.get_one(data)
    return render_template("update_user.html", User = user)


@app.route('/edit/<int:user_id>',methods=['POST'])
def update(user_id):
    data = {
        'fname': request.form['NewFirstName'],
        'lname': request.form['NewLastName'],
        'eml': request.form['NewEmail'],
        'id': user_id
    }
    Users.update(data)
    return redirect(f'/user/show/{user_id}')



@app.route('/user/delete/<int:user_id>')
def delete(user_id):
    data = {"id": user_id}
    Users.delete(data)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

