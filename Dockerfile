FROM python:3.9
RUN pip install mitmproxy
CMD ["mitmdump", "--mode", "transparent", "--listen-host", "0.0.0.0", "--listen-port", "5001", "-s", "proxy_script.py"]
