FROM duckietown/amod:latest

RUN apt-get update
RUN apt-get install -y python-pip

ENV CACHE=2

COPY requirements.txt /project/requirements.txt
RUN pip install -r /project/requirements.txt

COPY eval.py /project/eval.py
COPY read_scores.py /project/read_scores.py

WORKDIR /project

ENV PYTHONPATH=/project

CMD python /project/eval.py
