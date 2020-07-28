FROM continuumio/miniconda3

# Install python packages
RUN mkdir /opt/api
COPY requirements.txt /opt/api/
RUN pip install -r /opt/api/requirements.txt

WORKDIR /opt/api
COPY . /opt/api

EXPOSE 5000
ENV FLASK_ENV="docker"
CMD ["python3","webapp.py"]
