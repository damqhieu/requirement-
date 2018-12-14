FROM python:3.7.1
COPY . /code
WORKDIR /code
RUN pip install -r requirements.txt

RUN export FLASK_ENV=development

CMD ["python", "app.py"]