FROM python:3.9.13
ENV PYTHONUNBUFFERED=1
WORKDIR /chess_api
COPY requirements.txt /chess_api
RUN pip install -r requirements.txt
RUN python -m pip install --upgrade pip
