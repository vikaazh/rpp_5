from route.region import region
from route.tax_param_route import tax
from route.tax_route import tax_route
from dbsef import db, app

app.config['SECRET_KEY'] = 'test for testing test'
db.init_app(app)

app.register_blueprint(region)
app.register_blueprint(tax)
app.register_blueprint(tax_route)
if __name__ == "__main__":
    app.run(debug=True)
