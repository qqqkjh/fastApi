FROM python:3.9.12

ENV APP_NAME "IN DOCKER APP"

WORKDIR /code
COPY app /code/app
COPY Pipfile /code
COPY Pipfile.lock /code
COPY scripts /code



RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev --system --deploy

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]