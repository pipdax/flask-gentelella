from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint(
    'data_blueprint',
    __name__,
    url_prefix='/data',
    template_folder='templates',
    static_folder='static'
)

from .my_script.get_data import *
@blueprint.route('/get_<script>')
@login_required
def get_data(script):
    try:
        return eval(script + '()')
    except Exception as e:
        pass

@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')
