from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio_uno():
    result=average= None
    note1=note2=note3=assistance= None
    if request.method == 'POST':
        note1 = int(request.form['note1'])
        note2 = int(request.form['note2'])
        note3 = int(request.form['note3'])
        assistance = int(request.form['assistance'])
        average, result = isPass(note1, note2, note3, assistance)

    return render_template('ejercicio_uno.html', result=result, average=average,  note1=note1, note2=note2, note3=note3, assistance=assistance)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio_dos():
    name_result = name_count = nameone = nametwo = namethree = ""

    if request.method == 'POST':
        nameone = request.form.get('nameone')
        nametwo = request.form.get('nametwo')
        namethree = request.form.get('namethree')

        if nameone is not None and nametwo is not None and namethree is not None:
            name_result, name_count = isLargerThan(nameone, nametwo, namethree)

    return render_template('ejercicio_dos.html', name_count=name_count, name_result=name_result, nameone=nameone, nametwo=nametwo, namethree=namethree)

def isPass(x,y,z,assistance):
    average=((x+y+z)/3)
    assistance = assistance
    if average >= 40 and assistance >= 75:
        result = 'APROBADO'
    else:
        result = 'REPROBADO'
    return "{:.2f}".format(average), result


def isLargerThan(a, b, c):
    name_strings = [a, b, c]
    max_length = max(len(s) for s in name_strings)

    if all(len(s) == max_length for s in name_strings):
        name_result = 'No hay nombre más largo que otro'
        name_count = 'El nombre tiene: ' + str(max_length) + ' caracteres'
    else:
        longest_name = max(name_strings, key=len)
        name_result = 'El nombre con mayor cantidad de caracteres es: ' + longest_name
        name_count = 'El nombre tiene: ' + str(len(longest_name)) + ' caracteres'

    return name_result, name_count