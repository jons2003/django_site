FROM faucet/python3:11.0.0
WORKDIR /opt/site
COPY . /opt/site
RUN  pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]