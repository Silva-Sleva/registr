from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def ind():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promo():
    countdown_list = [
        'Человечество вырастает из детства.',
        'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.',
        'И начнем с Марса!',
        'Присоединяйся!'
    ]
    return '</br>'.join(countdown_list)


@app.route('/bootstrap_sample')
def bootstrap():
    return f'''<!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
        <link rel="stylesheet" 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
        crossorigin="anonymous">
        <title>Привет, Яндекс!</title>
      </head>
      <body>
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                         alt="здесь должна была быть картинка, но не нашлась"> 
                    <div class="alert alert-secondary" role="alert">
                        Человечество вырастает из детства.<br>
                    </div>
                    <div class="alert alert-success" role="alert">
                        Человечеству мала одна планета.<br>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                        Мы сделаем обитаемыми безжизненные пока планеты.<br>
                    </div>
                    <div class="alert alert-warning" role="alert">
                        И начнем с Марса!<br>
                    </div>
                    <div class="alert alert-danger" role="alert">
                        Присоединяйся!
                    </div>
                </div>
            </div>
        </div>
      </body>
    </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f"""!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
          crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
    <title>Отбор астронавтов</title>
</head>
<body>
<div class="container">
<div class="row justify-content-center">
<div class="col-md-6">
<h1>Анкета претендента на участие в миссии</h1>
<div>
    <form class="login_form" method="post">

        <input type="text" class="form-control" placeholder="Введите Фамилию">
        <input type="text" class="form-control" placeholder="Введите имя">
        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
        <div class="form-group">
            <fieldset>
                <legend>Какое у вас образование?</legend>
                <select class="form-control" id="classSelect" name="class">
                    <option>Начальное</option>
                    <option>Среднее специальное</option>
                    <option>Высшее</option>
                </select>
            </fieldset>
        </div>
        <div class="form-group form-check">
            <fieldset>
                <legend>Какие у вас есть профессии?</legend>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label><br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Инженер-исследователь</label><br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Инженер-строитель</label><br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Пилот</label><br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Метеоролог</label><br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label><br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label><br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Врач</label><br>
                <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                <label class="form-check-label" for="acceptRules">Экзобиолог</label><br>
            </fieldset>
        </div>
        <div class="form-group">
            <fieldset>
            <legend>Укажите пол</legend>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                <label class="form-check-label" for="male">
                    Мужской
                </label>
            </div>
            <div class="form-check">
                <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                <label class="form-check-label" for="female">
                    Женский
                </label>
            </div>
            </fieldset>
        </div>
        <div class="form-group">
            <fieldset>
                <legend>Почему вы хотите принять участие в миссии?</legend>
                <textarea class="form-control" id="about" rows="3" name="about"></textarea>
            </fieldset>
        </div>
        <div class="form-group">
            <label for="photo">Приложите фотографию</label>
            <input type="file" class="form-control-file" id="photo" name="file">
        </div>
        <div class="form-group form-check">
            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
        </div>
        <button type="submit" class="btn btn-primary">Записаться</button>
    </form>
</div>
</div>
</div>
</div>
</body>
</html>
"""

    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8082, host='127.0.0.1')
