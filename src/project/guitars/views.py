from flask import Blueprint, render_template

from project        import db
from project.views  import login_required
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

# todo: figure out how to make these URLs case insensitive

# e.g. /guitars/Gibson
@guitars_blueprint.route('/<brand>')
def browse_by_brand(brand):
    guitars = Guitar.query.filter_by(brand=brand).all()

    return render_template('browse_specific_brand.jinja.html',
                            guitars=guitars,
                            brand=brand)

# e.g. /guitars/Gibson/SG
@guitars_blueprint.route('/<brand>/<model>')
def browse_by_model(brand, model):
    guitars = Guitar.query.filter_by(brand=brand, model=model).all()

    return render_template('browse_specific_brand-model.jinja.html',
                            guitars=guitars,
                            brand=brand,
                            model=model)

# e.g. /guitars/Gibson/SG/2015
@guitars_blueprint.route('/<brand>/<model>/<int:year>')
def browse_by_year(brand, model, year):
    guitar = Guitar.query.filter_by(
        brand=brand,
        model=model,
        year=year
    ).first()

    return render_template('browse_specific_brand-model-year.jinja.html',
                            guitar=guitar,
                            brand=brand,
                            model=model,
                            year=year)
