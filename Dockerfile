# Use a slim, stable Python base image
FROM python:3.10.16

# Set a working directory
WORKDIR /app

# Copy dependency list first (leverages Docker layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Install bash and git prompt for enhanced shell experience
RUN curl -o /usr/share/git-prompt.sh \
    https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh
RUN apt update && \
    apt install -y bash bash-completion

# Copy your application code
COPY pytest.ini /app/
COPY src/ /app/src/
COPY test/ /app/test/
COPY .bashrc /root/.bashrc

# Default command
CMD ["python", "src/Games.py"]