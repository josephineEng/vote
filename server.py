from waitress import serve
    
from pollster.wsgi import application
    
if __name__ == '__main__':
    serve(application, port='8088')