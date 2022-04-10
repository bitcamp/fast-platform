FROM python

EXPOSE 8080

WORKDIR /platform/

# Only copy over the requirments.txt for now (helps with Docker layer caching)
COPY ./requirements.txt /platform/requirements.txt

RUN python -m pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /platform/
