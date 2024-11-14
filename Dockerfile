FROM apache/airflow:2.10.2
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN install unzip
RUN install curl
RUN pip install --no-cache-dir -r /requirements.txt