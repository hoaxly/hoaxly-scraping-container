FROM scrapinghub/portia

RUN set -xe \
    && apt-get update \
    && dpkg --configure -a \
    && apt-get install -f -y gcc \
                          python3-dev python-dev \
                          curl bash \
                          make build-essential libffi-dev \
                          python-software-properties software-properties-common

# the file with our requirements
COPY portia_projects/requirements.txt .
# our helper package
COPY portia_projects/packages /app/data/projects/packages
# our current spiders
COPY portia_projects/hoaxlyPortia /app/data/projects/hoaxlyPortia


RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir /app/data/projects/packages


COPY ./scrapyd.conf /etc/scrapyd/
VOLUME /etc/scrapyd/ /var/lib/scrapyd/
EXPOSE 6800
