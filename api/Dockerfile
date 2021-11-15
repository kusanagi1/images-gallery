FROM python:3.10

WORKDIR /app

EXPOSE 2222

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

COPY . ./
CMD ["python", "main.py"]