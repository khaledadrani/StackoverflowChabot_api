<h1 align="center">Stackoverflow Chatbot API</h1>

# Description

<p align="center">This project is a prototype of a chatbot that will quickly find the best answer for any programming question you have through the dataset of Stackoverflow. We worked only with the portion of Stackoverflow dataset that covers 2016. This repository is only the Backend for the project.
</p>

<p align="center">
</p>


# Live Demo

Check the live version:
<a href="https://stackoverflow-chatbot-api.herokuapp.com">APP Home Page </a>

It is possible that we will add screenshots in the future.

Note: If there is an application error, it musb that the free dyno for the current month had ended.


# Built with:

- Python
- Keras
- Flask
- MongoDB
- Heroku


# How to reproduce the development environment:

To reproduce the api correctly as a fork, please follow these steps:

1. Make sure you have this python-version==3.8.10 and the virtualenv package

    ```bash
    python --version 
    pip install virtualenv
    ```

2. Create your python environment

    ```
    python -m venv py_env
    ```

3. Activate your virtual environment and make sure the pip version is 20.2.4:

    ```
    source py_env/bin/activate #in Ubuntu 20.04 
    ./py_env/Scripts/activate #in Windows 10

    python -m pip install pip==20.2.4
    ```

4. While the py_env is active, use the requirements.txt with pip or these commands:

    ```
    pip install flask nltk flask_cors python-dotenv pymongo  flask_limiter keras tensorflow-cpu==2.5.0 numpy==1.19.2 six==1.15.0 gunicorn

    pip install "pymongo[srv]" 
    ```

5. Create an .env file and put these pieces of information:

    * DATABASE_CONNECTION: "mongodb cluster connection string"
    * ENV: 'production' | 'development'

5. To test the app:
    ```
    python app.py
    ```

    Check also that the app works with gunicorn. It is necessary if you want to work with Heroku with $PORT being the port. Put it to 5000 for example.

    ```
    gunicorn --bind 0.0.0.0:$PORT app:app
    ```

# Database:

You should create a mongo cluster and put a portion of Stackoverflow questions in it. Then connect using your cluster connection string to the app. 

# Future updates:

- [x] Basic working prototype
- [ ] Add more documentation about the database
- [ ] Authentication 
- [ ] Expand the chatbot functionality

# Resources

* Kaggle Stackoverflow dataset: https://www.kaggle.com/stackoverflow/stacksample 

# Contributors:

- Khaled Adrani: https://github.com/khaledadrani => Database and API
- Oussema Guedri: https://github.com/guedriOussema => Chatbot model and FrontEnd


