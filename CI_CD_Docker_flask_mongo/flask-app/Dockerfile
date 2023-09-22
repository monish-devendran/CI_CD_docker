FROM python:3.8.18
RUN mkdir /flask-app
ADD . /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt
CMD ["python","/flask-app/app.py"]

