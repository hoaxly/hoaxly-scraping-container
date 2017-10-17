FROM scrapinghub/portia

RUN set -xe \
    && apt-get update \
    && apt-get install -y gcc \
                          python3-dev python-dev \
                          curl bash \
                          make build-essential libssl-dev libffi-dev python-software-properties software-properties-common


COPY portia_projects/requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY ./scrapyd.conf /etc/scrapyd/
VOLUME /etc/scrapyd/ /var/lib/scrapyd/
EXPOSE 6800
