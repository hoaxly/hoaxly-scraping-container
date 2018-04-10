FROM scrapinghub/portia:latest

RUN set -xe \
    && apt-get update \
    && dpkg --configure -a \
    && apt-get install -f -y gcc \
                          python3-dev python-dev \
                          curl bash \
                          make build-essential libxslt1-dev libtool xml-core libxml2 libxml2-dev libxslt-dev libffi-dev \
                          python-software-properties software-properties-common

# the file with our requirements
COPY portia_projects/requirements.txt .
# our helper package
COPY portia_projects/packages /app/data/projects/packages
# our current spiders
COPY portia_projects/hoaxlyPortia /app/data/projects/hoaxlyPortia


RUN pip3 install setuptools --upgrade
RUN pip3 install scrapyd-client
RUN pip3 install scrapyd-deploy

RUN pip install -r requirements.txt
RUN pip3 install -e /app/data/projects/packages

COPY ./scrapyd.conf /etc/scrapyd/
VOLUME /etc/scrapyd/ /var/lib/scrapyd/
EXPOSE 6800
