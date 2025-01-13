FROM python:3.12-slim
LABEL authors="andesec"

WORKDIR /app

COPY . /app

# Install Poetry
RUN pip install poetry
# RUN pip install --no-cache-dir poetry

# Copy only the dependency files first for caching
COPY pyproject.toml poetry.lock* ./

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Expose the Flask app's port
EXPOSE 5000

# Start the Flask app
CMD ["poetry", "run", "python", "app.py"]
