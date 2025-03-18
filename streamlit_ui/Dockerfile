# Use official Python image
FROM python:3.11

# Set working directory
WORKDIR /streamlit_ui

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Streamlit application code
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
