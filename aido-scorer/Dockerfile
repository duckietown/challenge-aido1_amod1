FROM duckietown/amod:latest

RUN apt-get update
RUN apt-get install -y python-pip


COPY requirements.txt /project/requirements.txt
RUN pip install -r /project/requirements.txt

COPY eval.py /project/eval.py

WORKDIR /project
CMD python /project/eval.py
