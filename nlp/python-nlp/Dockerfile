FROM registry.cn-shanghai.aliyuncs.com/russell-hub/python-base:latest
MAINTAINER Floyd Labs "support@floydhub.com"

# SpaCy
RUN pip install -U spacy
RUN python -m spacy.en.download

# Textacy
RUN pip install textacy

# Pattern
# RUN pip install -U pattern