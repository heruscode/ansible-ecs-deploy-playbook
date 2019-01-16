# From python base image
FROM python:3.6.7-slim-jessie

# Defines the container workdir
WORKDIR /opt/simple_python_app

# Installs system dependencies
RUN apt-get update && apt-get install -y git

# Clones the app git repository
RUN git clone https://github.com/heruscoder/ansible-ecs-deploy-playbook.git .

# Installs base dependencies
RUN cd app && \
python3 -m pip install -r requirements.txt

# Exposes the volume and app port
VOLUME /opt/simple_python_app/app
EXPOSE 80

# Runs the app
CMD ["python3","app/app.py"]