from flask import Flask

app = Flask(__name__, static_folder='./public', template_folder='./static')
app.config['JSON_AS_ASCII'] = False

import templates.home.views
import templates.extract.views
import templates.product.views
import templates.charts.views
import templates.about.views