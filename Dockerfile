FROM python:3.6

RUN mkdir /blog
WORKDIR /blog
COPY . /blog

COPY requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python","test_runner.py", "runserver", "0.0.0.0:8000"]
