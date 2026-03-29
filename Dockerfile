FROM python:3.12-slim

LABEL maintainer="Kevin Feasel"

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

RUN uv pip install --system \
    jupyter \
    pandas \
    scikit-learn \
    matplotlib \
    seaborn \
    streamlit

COPY code/ ./code/

EXPOSE 8888 8501

CMD bash -c "jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.password='argon2:\$argon2id\$v=19\$m=10240,t=10,p=8\$4eWCdoZdVVX+Iom9kQMCUw\$6KN4knj9GBEJp42WhQ+S8FYYMajZ8nxPTw++wCPHoII' & streamlit run code/app.py --server.port=8501 --server.address=0.0.0.0 --server.headless=true"
