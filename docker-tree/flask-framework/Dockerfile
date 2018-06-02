FROM heroku/miniconda
RUN apt-get update && apt-get install libgl1-mesa-glx -y

ADD ./app/requirements.txt /tmp/requirements.txt
ADD ./app/conda-requirements.txt /tmp/conda-requirements.txt

RUN pip install -qr /tmp/requirements.txt 

ADD ./app /opt/app/
WORKDIR /opt/app

RUN conda install --yes --file /tmp/conda-requirements.txt

RUN conda install -c conda-forge fbprophet

RUN conda install -c anaconda quandl

CMD gunicorn --bind 0.0.0.0:$PORT wsgi
