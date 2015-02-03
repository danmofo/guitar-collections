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
    guitars = Guitar.query.all()
    return render_template('browse_guitars.jinja.html', guitars=guitars)

@guitars_blueprint.route('/browse/<int:guitar_id>')
def browse_specific(guitar_id):
    pass
