FROM c3h3/pyenv

MAINTAINER fantaneo.orange@gmail.com

RUN apt-get upgrade && apt-get update

RUN apt-get -yV install \
    cmake \
    libeigen3-dev \
    libgtk2.0-dev \
    libgtkglext1-dev \
    libqt4-dev \
    freeglut3-dev \
    opencl-headers \
    libtbb-dev \
    libjpeg-dev \
    libjasper-dev \
    libpng++-dev \
    libtiff-dev \
    libopenexr-dev \
    libwebp-dev

RUN cd /root/.pyenv/plugins/python-build/../.. && git pull origin master && cd -

RUN yes | pyenv install anaconda-2.4.0 && \
    pyenv global anaconda-2.4.0 && \
    export PATH="/home/root/anaconda/bin:$PATH" && \
    yes | conda install -c https://conda.binstar.org/menpo opencv

WORKDIR /mls-itoc

