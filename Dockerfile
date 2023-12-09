FROM python:3.10.4
WORKDIR /app
COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn