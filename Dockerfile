FROM python:3.9.0-slim
WORKDIR /Workspace
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
COPY src/immo ./src/immo
COPY ./setup.cfg ./setup.cfg
COPY ./setup.py ./setup.py
RUN pip install -e .
CMD ["uvicorn", "immo.app:app", "--host", "0.0.0.0", "--port", "8000"]