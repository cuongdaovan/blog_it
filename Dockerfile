FROM python:3.6

WORKDIR /blog
COPY . /blog

COPY requirements.txt ./
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python3","test_runner.py", "runserver", "0.0.0.0:8000"]
