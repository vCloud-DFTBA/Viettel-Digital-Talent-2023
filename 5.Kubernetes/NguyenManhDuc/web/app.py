from flask import Flask, render_template, request, redirect, url_for # For catching InvalidId exception for ObjectId
import os
import requests

title = "my dream"
heading = "THE ADVENTURE OF VIETTEL DIGITAL TALENT"


base_host =  os.environ.get('API_HOST','0.0.0.0')
base_port =  os.environ.get('API_POST','5500')


app = Flask(__name__)


def redirect_url():
    return request.args.get('next') or \
        request.referrer or \
        url_for('index')


@app.route("/")
@app.route("/list", methods=['GET'])
def list():
    
    data = requests.get(f'http://{base_host}:{base_port}/')

    todos_l = data.json()
    return render_template('index.html', todos=todos_l, t=title, h=heading)

# this function use to direct to add a new candicate 
@app.route("/add_candidate")
def add_candidate():
    data = requests.get(f'http://{base_host}:{base_port}/')
    todos_l = data.json()
    return render_template('add.html', todos=todos_l, t=title, h=heading)


# this function use to direct to remove a new candicate 
@app.route("/remove")
def remove():
    id = request.values.get("_id")
    # listCandi.delete_one({"_id": ObjectId(id)})
    response = requests.delete(f'http://{base_host}:{base_port}/candidates/{id}')
    return redirect("/")


@app.route("/update")
def update():
    id = request.values.get("_id")
    response = requests.get(f'http://{base_host}:{base_port}/candidates/{id}')
    data =response.json()
    print(data)
    # id = request.values.get("_id")
    # data = listCandi.find({"_id": ObjectId(id)})
    print(data)
    return render_template('update.html',candidates=data,h=heading,t=title)



# this function use to add anew candidate after user click to the button
@app.route("/action", methods=["POST"])
def action_add():
    # Stt = listCandi.count_documents({}) + 1
    fullname = request.values.get("fullname")
    username = request.values.get("username")
    year = request.values.get("year")
    unversity = request.values.get("university")
    field = request.values.get("field")
    gender = request.values.get("gender")
    data = {
        "STT": 0,
        "fullname": fullname,
        "year of birth": year,
        "gender": gender,
        "university": unversity,
        "Username": username,
        "field": field
    }
    print(data)
    
    mess = requests.post(f'http://{base_host}:{base_port}/candidates',json=data)
    # print(mess)
    
    return redirect("/add_candidate")


# this function use to update new info of candidate after user click to the button
@app.route("/action3", methods=["POST"])
def action_update():
    stt = request.values.get("STT")
    print(stt)
    name = request.values.get("name")
    username = request.values.get("Username")
    year=request.values.get("year")
    gender = request.values.get("gender")
    university = request.values.get("university")
    field = request.values.get("field")
    id = request.values.get("_id")
    
    data = {
            "STT": stt,
            "fullname": name,
            "year of birth": year,
            "gender": gender,
            "university": university,
            "Username": username,
            "field": field
    }
    print(data)
    requests.put(f"http://{base_host}:{base_port}/candidates/update/{id}",json=data)
    return redirect("/")



@app.route("/search", methods=["GET"])
def action_search():
    key=request.values.get("key")
    refer=request.values.get("refer")
    
    if refer == 'id':
        response=requests.get(f'http://{base_host}:{base_port}/candidates/{key}')
        data=response.json()
        return render_template('searchlist.html',todos=data,t=title,h=heading)
    else:   
        response=requests.get(f'http://{base_host}:{base_port}/candidates/search',json={refer:key})
        data=response.json()
        return render_template('searchlist.html',todos=data,t=title,h=heading)



if __name__ == "__main__":  # checking if __name__'s value is '__main__'. __name__ is an python environment variable who's value will always be '__main__' till this is the first instatnce of app.py running
    env = os.environ.get('FLASK_ENV', 'development')
    app.run(debug=True, port=5000, host="0.0.0.0")
