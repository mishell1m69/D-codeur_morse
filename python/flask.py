from flask import Flask, render_template, request

selected = None

app = Flask(__name__)

@app.route('index')
def index():
    return render_template("index.html")

@app.route('/decoder')
def decoder():
    return render_template("decoder.html")

@app.route('/encoder')
def encoder():
    return render_template("encoder.html")


@app.route('/editInfo2', methods=['GET', 'POST'])
def edit_info_2():
    if request.method == "POST":
        global selected
        first_name = request.form.get("fname") if not request.form.get("fname")=="" else None
        last_name = request.form.get("lname") if not request.form.get("lname")=="" else None
        job = request.form.get("job") if not request.form.get("job")=="" else None
        birth = 2024 - int(request.form.get("age")) if not request.form.get("age")=="" else None
        selected = people_correspondant([first_name,last_name,job,birth])
        if len(selected)>0:
            return render_template("editInfo2.html", selected = selected, len = len(selected))
        else:
            return render_template("lbozo.html")
    else:
        return render_template("index.html")
    

@app.route('/delettedSave', methods=['GET', 'POST'])
def deletted_save():
    if request.method == "POST":
        global selected
        sel = request.form.get("ppl")
        delete([sel])
        return render_template("delettedSave.html")
    else:
        return render_template("index.html")
    
@app.route('/delInfo2', methods=['GET', 'POST'])
def del_info_2():
    if request.method == "POST":
        global selected
        first_name = request.form.get("fname") if not request.form.get("fname")=="" else None
        last_name = request.form.get("lname") if not request.form.get("lname")=="" else None
        job = request.form.get("job") if not request.form.get("job")=="" else None
        birth = 2024 - int(request.form.get("age")) if not request.form.get("age")=="" else None
        selected = people_correspondant([first_name,last_name,job,birth])
        if len(selected)>0:
            return render_template("delInfo2.html", selected = selected, len = len(selected))
        else:
            return render_template("lbozo.html")
    else:
        return render_template("index.html")

@app.route('/deletedInfo', methods=['GET', 'POST'])
def deleted_info():
    if request.method == "POST":
        global selected
        sel = request.form.get("ppl")
        dinfo = request.form.get("dinfo") if not request.form.get("dinfo")=="" else None
        if dinfo in ["Indicatif","Mobile","Fixe","Domicile","Travail"]:
            CHANGE_num([None,sel],dinfo)
        else:
            CHANGE_people([None,sel],dinfo)
        return render_template("deletedInfo.html")
    else:
        return render_template("index.html")


@app.route('/numsFromPpl', methods=['GET', 'POST'])
def nums_found():
    if request.method == "POST":
        global selected
        first_name = request.form.get("fname") if not request.form.get("fname")=="" else None
        last_name = request.form.get("lname") if not request.form.get("lname")=="" else None
        job = request.form.get("job") if not request.form.get("job")=="" else None
        birth = 2024 - int(request.form.get("age")) if not request.form.get("age")=="" else None
        selected = people_correspondant([first_name,last_name,job,birth])
        if len(selected)>0:
            nb=[]
            for x in selected:
                nb.append(num_correspondant([x[5]]))
            return render_template("numsFromPpl.html", selected = selected, len = len(selected), nb = nb)
        else:
            return render_template("lbozo.html")
    else:
        return render_template("index.html")

@app.route('/addNum2', methods=['GET', 'POST'])
def add_num_2():
    if request.method == "POST":
        global selected
        first_name = request.form.get("fname") if not request.form.get("fname")=="" else None
        last_name = request.form.get("lname") if not request.form.get("lname")=="" else None
        job = request.form.get("job") if not request.form.get("job")=="" else None
        birth = 2024 - int(request.form.get("age")) if not request.form.get("age")=="" else None
        selected = people_correspondant([first_name,last_name,job,birth])
        if len(selected)>0:
            return render_template("addNum2.html", selected = selected, len = len(selected))
        else:
            return render_template("lbozo.html")
    else:
        return render_template("index.html")

@app.route('/addedNum', methods=['GET', 'POST'])
def added_num():
    if request.method == "POST":
        global selected
        sel = request.form.get("ppl")
        ind = request.form.get("ind") if not request.form.get("ind")=="" else None
        mobile = request.form.get("mobile") if not request.form.get("mobile")=="" else None
        fixe = request.form.get("fixe") if not request.form.get("fixe")=="" else None
        domicile = request.form.get("domicile") if not request.form.get("domicile")=="" else None
        travail = request.form.get("travail") if not request.form.get("travail")=="" else None
        CHANGE_num([ind,sel],"Indicatif")
        CHANGE_num([mobile,sel],"Mobile")
        CHANGE_num([fixe,sel],"Fixe")
        CHANGE_num([domicile,sel],"Domicile")
        CHANGE_num([travail,sel],"Travail")
        return render_template("addedNum.html")
    else:
        return render_template("index.html")

@app.route('/addedPpl', methods=['GET', 'POST'])
def added_ppl():
    if request.method == "POST":
        global selected
        first_name = request.form.get("fname") if not request.form.get("fname")=="" else None
        last_name = request.form.get("lname") if not request.form.get("lname")=="" else None
        job = request.form.get("job") if not request.form.get("job")=="" else None
        birth = 2024 - int(request.form.get("age")) if not request.form.get("age")=="" else None
        ADD_people([first_name,last_name,job,birth],[None,None,None,None,None])
        
        return render_template("addedPpl.html")
    else:
        return render_template("index.html")
     
@app.route('/addedBoth', methods=['GET', 'POST'])
def added_both():
    if request.method == "POST":
        global selected
        first_name = request.form.get("fname") if not request.form.get("fname")=="" else None
        last_name = request.form.get("lname") if not request.form.get("lname")=="" else None
        job = request.form.get("job") if not request.form.get("job")=="" else None
        birth = 2024 - int(request.form.get("age")) if not request.form.get("age")=="" else None
        ind = request.form.get("ind") if not request.form.get("ind")=="" else None
        mobile = request.form.get("mobile") if not request.form.get("mobile")=="" else None
        fixe = request.form.get("fixe") if not request.form.get("fixe")=="" else None
        domicile = request.form.get("domicile") if not request.form.get("domicile")=="" else None
        travail = request.form.get("travail") if not request.form.get("travail")=="" else None
        ADD_people([first_name,last_name,job,birth],[ind,mobile,fixe,domicile,travail])
        
        return render_template("addedBoth.html")
    else:
        return render_template("index.html")

app.run(debug=True)