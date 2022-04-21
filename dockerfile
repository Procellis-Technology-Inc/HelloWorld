FROM python:slim

COPY . .
RUN apt-get update
RUN pip install -r requirements.txt

EXPOSE 10243
ENTRYPOINT ["python"]
CMD ["helloWorld.py"]