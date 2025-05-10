FROM python:latest
RUN mkdir /flask-app
ADD . /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt
CMD ["python","/flask-app/app.py"]

