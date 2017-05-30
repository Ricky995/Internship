#My first dockerfile

FROM ubuntu:16.04
LABEL description="This image is used to print to the console Hello Docker"
ADD hellodocker.py /home/
RUN apt-get update -y
RUN apt-get install -y python
CMD ["python","home/hellodocker.py"]
