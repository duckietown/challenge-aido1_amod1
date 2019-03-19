FROM duckietown/amod:aido2-01


RUN wget https://www.princexml.com/download/prince_12.2-1_debian9.1_amd64.deb && dpkg -i prince_12.2-1_debian9.1_amd64.deb

WORKDIR /project

COPY requirements.txt .
RUN pip3.7 install -r requirements.txt

COPY eval.py .

CMD python3.7 /project/eval.py
