FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN chmod 777 start.sh
CMD ["./start.sh"]