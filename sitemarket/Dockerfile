FROM django:python3
WORKDIR /opt/site
COPY . /opt/site
RUN  pip install --upgrade pip
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]