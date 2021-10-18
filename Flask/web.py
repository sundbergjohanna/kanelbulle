from flask import Flask, render_template

app = Flask(__name__)


# -------- Present result with Flask -------- #
@app.route('/simulation/<int:id>')
def simulation(id):
    lift = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    drag = ['high', 'low', 'medium', 'small', 'high', 'low', 'medium', 'high', 'small', 'small']
    result = dict(zip(lift, drag))
    return render_template('test.html', 'style.css', sim_spec=id, results=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
