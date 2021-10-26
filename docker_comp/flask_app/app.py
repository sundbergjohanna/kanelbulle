from celery import Celery
from flask import Flask, jsonify, render_template
from celery.execute import send_task

app = Flask(__name__)
simple_app = Celery('worker',
                    broker='amqp://admin:admin@rabbit:5672',
                    backend='rpc://')


# ------ Testing only flask ------ # WORKS!
@app.route('/proc/<name>')
def proc(name):
    return name

# ------ Testing celery + flask ------ #
@app.route('/string/<name>')
def process(name):
    res = simple_app.send_task('cel.print_str', [name])
    return res.get()

# Running celery in flask
@app.route('/test')
def app_test():
    #res = test.delay()
    res = simple_app.send_task('cel.test')
    return res.get()

# Testing running airfoil with flask+celery
@app.route('/murtazo')
def mur_test():
    #res = test.delay()
    file = 'r0a0n200.xml'
    res = simple_app.send_task('cel_mur.calculate', [file])
    id = res.id
    # return res.get()
    list = res.get()
    return render_template("my_template.html", data=list)



# @app.route('/simple_start_task')
# def call_method():
#     app.logger.info("Invoking Method ")
#     r = simple_app.send_task('tasks.longtime_add', kwargs={'x': 1, 'y': 2})
#     app.logger.info(r.backend)
#     return r.id
#
#
# @app.route('/simple_task_status/<task_id>')
# def get_status(task_id):
#     status = simple_app.AsyncResult(task_id, app=simple_app)
#     print("Invoking Method ")
#     return "Status of the Task " + str(status.state)
#
#
# @app.route('/simple_task_result/<task_id>')
# def task_result(task_id):
#     result = simple_app.AsyncResult(task_id).result
#     return "Result of the Task " + str(result)
