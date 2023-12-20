FROM python:3.10.13
RUN mkdir /flask-app
ADD . /flask-app
WORKDIR /flask-app
RUN pip install -r requirements.txt
CMD ["python","/flask-app/app.py"]

