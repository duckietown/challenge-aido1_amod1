FROM duckietown/amod:aido2-01

WORKDIR /project

COPY requirements.txt .
RUN pip3.7 install -r requirements.txt

COPY eval.py .
COPY read_scores.py .



ENV PYTHONPATH=/project

CMD python3.7 /project/eval.py
