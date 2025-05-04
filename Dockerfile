FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

WORKDIR /usr/app

# install python dependencies
COPY ./requirements.txt /usr/app/

RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY ./app /usr/app/

EXPOSE 4030

# start the server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4030", "--proxy-headers"]