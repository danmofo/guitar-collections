from flask import Blueprint, render_template

from project import db
from project.views import login_required
from project.models import Guitar

guitars_blueprint = Blueprint(
    'guitars',
    __name__,
    url_prefix='/guitars',
    template_folder='../templates/guitars',
    static_folder='../assets'
)
@guitars_blueprint.route('/browse')
def browse():
    return render_template('browse_guitars.jinja.html')
