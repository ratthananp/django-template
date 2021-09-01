FROM python:3.9
ENV PYTHONUNBUFFERED 1

# Change Timezone to GMT+7
ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install additional packages
RUN apt update
RUN apt install -y gettext

# Upgrade pip
RUN pip install -U pip

# Location of source code
ENV PROJECT_ROOT /opt/app
RUN mkdir -p $PROJECT_ROOT
WORKDIR $PROJECT_ROOT

# Copying requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copying manage.py file
COPY ./manage.py .

# Copying pylint/coverage config file
COPY ./.pylintrc .
COPY ./.coveragerc .

# Copying static file
COPY ./static ./static

# Copying source files
COPY ./main ./main
