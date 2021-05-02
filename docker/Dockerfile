ARG BASE_CONTAINER=jupyter/base-notebook
FROM $BASE_CONTAINER

LABEL maintainer="Mahyar Osanlouy<m.osanlouy@auckland.ac.nz>"
ARG NB_USER="jovyan"
ARG NB_UID="1000"
ARG NB_GID="100"

USER root

# Install all OS dependencies for fully functional notebook server.
RUN apt-get update && apt-get install -yq --no-install-recommends \
    build-essential \
    wget \
    bzip2 \
    ca-certificates \
    sudo \
    locales \
    fonts-liberation \
    run-one \
    libpthread-stubs0-dev \
    libmpich-dev \
    mpich \
    libmpich12 \
    gcc \
    gfortran \
    g++ \
    libblas-dev \
    liblapack-dev \
    git \
    make \
    libssl-dev \
    libglew-dev \
    swig \
    sudo \
    cifs-utils \
    systemd \
    openssh-server \
    liblzma-dev \
    libxml2-dev \
    libusb-dev \
    zlib1g-dev \
    software-properties-common \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install cmake.
ENV CMAKE_VERSION=3.16.3 \
    CMAKE_DIR=/cmake

RUN wget --quiet https://cmake.org/files/v3.16/cmake-${CMAKE_VERSION}-Linux-x86_64.sh && \
    mkdir $CMAKE_DIR && \
    /bin/bash cmake-${CMAKE_VERSION}-Linux-x86_64.sh --skip-license --prefix=$CMAKE_DIR && \
    rm cmake-${CMAKE_VERSION}-Linux-x86_64.sh
ENV PATH=$CMAKE_DIR/bin:$PATH

# Install Zinc.

# Make RUN commands use the new miniconda environment:
SHELL ["conda", "run", "/bin/bash", "-o", "pipefail", "-c"]
RUN mkdir /home/$NB_USER/opencmiss-build
WORKDIR /home/$NB_USER/opencmiss-build
RUN mkdir opencmiss && \
    mkdir setup-build && \
    git clone https://github.com/OpenCMISS/setup.git && \
    cd setup-build && \
    cmake -DOPENCMISS_LIBRARIES=zinc -DOPENCMISS_DEPENDENCIES_ROOT=../opencmiss -DOPENCMISS_SETUP_TYPE=dependencies ../setup && \
    make && \
    cd .. && \
    git clone https://github.com/mahyar-osn/zinc.git -b develop_mahyar && \
    mkdir build-zinc-release && \
    cd build-zinc-release && \
    cmake -DNEW_CONFIGURATION_STYLE=True -DOPENCMISSDEPENDENCIES_DIR=../opencmiss/install ../zinc && \
    make && \
    pip install -e bindings/python/ && \
    rm -rf ../opencmiss/build

# Switch back to jovyan to avoid accidental container runs as root
USER $NB_UID