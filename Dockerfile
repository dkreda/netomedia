# Image for Python Flask - Based on Python3 Image
FROM python:3

# install dependencies
RUN pip3 install --no-cache-dir Flask

# set Parameters
ENV EXSPort=8080

# Set WorkDir
WORKDIR /var/netomedia

# copy the web application code
COPY . .

# Ports to expose
EXPOSE ${EXSPort}
CMD python ./myServer.py ${EXSPort}
