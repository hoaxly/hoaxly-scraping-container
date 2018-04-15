FROM scrapinghub/portia


# the file with our requirements
COPY portia_projects/requirements.txt .
# our helper package
COPY portia_projects/packages /app/data/projects/packages
# our current spiders
COPY portia_projects/hoaxlyPortia /app/data/projects/hoaxlyPortia


# and our own requirements
RUN pip install  --no-cache-dir -r requirements.txt
# finally our own helperPackage
RUN pip install -e /app/data/projects/packages
