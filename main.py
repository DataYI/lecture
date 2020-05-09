from flask import Flask, render_template, request, abort
from update import update
from logger import logger_hander
from config import Config

app = Flask(__name__)
app.logger.addHandler(logger_hander)

def read_md(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None


@app.route('/class/<num>')
def class_(num):
    try:
        update(f'class_{num.zfill(2)}')
    except Exception as e:
        app.logger.exception('%s', e)
    ip = request.remote_addr
    if ip not in Config.allowable_ips:
        return 'Error', 500
    md = read_md(f'files/class_{num.zfill(2)}.md')
    if not md:
        abort(404)
    title = f'class_{num.zfill(2)}'
    return render_template('lecture.html', md=md, title=title)


@app.errorhandler(404)
def page_not_found(error):
    return '走错房间了！'

if __name__ == '__main__':
    app.run(host='0.0.0.0')