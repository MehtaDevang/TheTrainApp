FROM python:3.7-slim-buster AS base

FROM base AS compiler

RUN echo "This is A test for github actions workflow"
RUN docker --help
