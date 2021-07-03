from flask import Flask, request,render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/', methods=['GET', 'POST'])
def form():
    # ２回目以降データが送られてきた時の処理です
    if request.method == 'POST':
        print("POSTされたIDは？" + str(request.form['id']))
        print("POSTされたPASSWORDは？" + str(request.form['pwd']))
        return render_template('index.html')
    # １回目のデータが何も送られてこなかった時の処理です。
    else:
        #return render_template('index.html')
        return '''
        <!DOCTYPE html>
        <html>
        <head>
        <title> form練習 </title>
        </head>
        <body>
        <form method="POST">
            <input type="text" name="id" placeholder="userID">
            <input type="password" name="pwd" placeholder="Password">
            <input type="submit" value="送信">
        </form>
        </body>
        </html>
        '''

#@app.route('/')
#def hello():
#    count = redis.incr('hits')
#    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)