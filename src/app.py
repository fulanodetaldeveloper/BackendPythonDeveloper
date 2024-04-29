from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from database.model import db
from routes.solicitud_routes import api_solicitud_bp
from routes.asignacion_grimorio_routes import api_asignacion_grimorios_bp


def make_app(): 
    app = Flask(__name__) 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://dev_user:Compile365@127.0.0.1:33061/caso_practico'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    
    app.register_blueprint(api_solicitud_bp, url_prefix='/solicitud')
    app.register_blueprint(api_asignacion_grimorios_bp, url_prefix='/asignaciones')
    
    # Configuración de Swagger UI
    SWAGGER_URL = '/docs'  # URL para acceder a la documentación de la API
    API_URL = '/static/swagger.json'  # Ruta del archivo swagger.json
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "API REST Academia de Magia"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    
    return app


app = make_app()
if __name__ == '__main__':
    app.run(debug=True)