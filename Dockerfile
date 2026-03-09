FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    procps \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    "pulp<2.8.0" \
    snakemake \
    biopython \
    pandas \
    matplotlib \
    seaborn \
    NanoPlot

WORKDIR /workspace

CMD ["/bin/bash"]