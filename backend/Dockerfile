FROM python:3.10

# python dependencies
COPY ./requirements.txt /
RUN pip install -r ./requirements.txt

# upload scripts
COPY ./scripts/entrypoint.sh ./scripts/start.sh /

# Fix windows docker bug, convert CRLF to LF
RUN sed -i 's/\r$//g' /start.sh && chmod +x /start.sh && sed -i 's/\r$//g' /entrypoint.sh && chmod +x /entrypoint.sh

WORKDIR /app
