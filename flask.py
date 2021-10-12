from flask import Flask, jsonify

app = Flask(__name__)

# -------- Present result with Flask -------- #
@app.route('/result')
def process():
    lift = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    drag = ['high', 'low', 'medium', 'small', 'high', 'low', 'medium', 'high', 'small', 'small']
    result = dict(zip(lift, drag))
    # time.sleep(10)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)