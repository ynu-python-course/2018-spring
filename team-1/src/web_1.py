from flask import Flask,render_template,request,redirect,url_for,session
import config
import pymysql.cursors
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash


app = Flask(__name__)
app.config.from_object(config)
# 连接MySQL数据库
connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='web_1', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
db= SQLAlchemy()
cursor = connection.cursor()
User = "SELECT `username`, `password` FROM `user`"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        data= "SELECT * FROM `user` WHERE `username` = '%s'" % username
        cursor.execute(data)
        user = cursor.fetchone()
        if check_password_hash(user['password'],password):
            session['user_id'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login_wrong.html')

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        data = "SELECT * FROM `user` WHERE `username` = '%s'" % username
        cursor.execute(data)
        user = cursor.fetchone()
        if password1 != password2:
            return render_template('wrongcode.html')
        elif user['username'] == username:
            return render_template('had_user.html')
        else:
            user = "INSERT INTO `user` (`username`, `password`) VALUES ('%s', '%s')"%(username,generate_password_hash(password1))
            cursor.execute(user)
            connection.commit()
            connection.close()
            return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/search/',methods=['GET','POST'])
def search():
    if request.method == 'GET':
        return render_template('search.html')
    else:
        for i in ['law_name','sort','release_date','clause','content']:
            search = request.form.get('search')
            data = "SELECT * FROM `laws` WHERE `{}`like '%{}%'".format(i,search)
            cursor.execute(data)
            search = cursor.fetchall()
            print(search)
            if search:
                return render_template('s_result.html',results = search)
    return None

#钩子函数，判断是否登陆
@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = "SELECT * FROM `user` WHERE `username` = '%s'" % user_id
        cursor.execute(user)
        user = cursor.fetchone()
        if user:
            return {'user':user}
    return {}


if __name__ == '__main__':
    app.run()
