from flask import Flask
from flask import render_template
/from models import *
app = Flask(__name__)

@app.route('/')
def index():
  schools=School.select().order_by(School.school_name.asc())
  return (render_template('index.html', schools=schools))


@app.route('/schools/clemente')
def school():
  return render_template ('school.html')

if __name__ == '__main__':
    app.run(debug=True)
