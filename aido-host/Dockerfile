FROM duckietown/amod:aido002

RUN apt-get update
RUN apt-get install -y python-pip

RUN wget https://www.princexml.com/download/prince_12.2-1_debian9.1_amd64.deb && dpkg -i prince_12.2-1_debian9.1_amd64.deb

COPY requirements.txt /project/requirements.txt
RUN pip install -r /project/requirements.txt

COPY eval.py /project/eval.py


WORKDIR /project
CMD python /project/eval.py
