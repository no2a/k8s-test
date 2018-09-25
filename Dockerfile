FROM python:2.7
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY api.py /
CMD python api.py
EXPOSE 3000
