FROM python:3.6
RUN mkdir /flask-app
ADD ./flask-app /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt
CMD ["python","app.py"]
