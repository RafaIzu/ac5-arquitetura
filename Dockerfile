  
FROM python:3.8.1
RUN pip install psycopg2-binary
RUN pip install SQLAlchemy
RUN pip install flask
RUN pip install greenlet
RUN pip install Flask-SQLAlchemy
RUN mkdir templates
RUN mkdir static
COPY check_connection.py /check_connection.py
COPY app.py /app.py
COPY templates/*  /templates/
COPY static/*  /static/
RUN chmod -R a+rwx static
RUN chmod -R a+rwx templates
CMD ["python","app.py"]