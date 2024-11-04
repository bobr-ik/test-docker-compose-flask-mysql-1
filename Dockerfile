FROM python:3.12

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y \
    build-essential \
    rustc \
    cargo \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Обновляем PATH
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "python", "app.py" ]