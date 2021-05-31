from website import create_app
import os 

env_name = os.getenv('FLASK_ENV')

app = create_app(env_name)


if __name__ == '__main__':
    app.run()
