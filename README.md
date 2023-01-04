# start.io-coding-assignment-solution

# Prometheus Exporter
This is a Prometheus exporter that exposes the top 100 crypto coins by market capitalization. It includes three metrics:

current_price: The current price of the coin in USD
high: The 24-hour high of the coin in USD
low: The 24-hour low of the coin in USD

# Prerequisites
A Kubernetes cluster
The kubectl command-line tool
The helm package manager

# Installing helm chart for prometheus-exporter
Use the helm install command to install the chart in a Kubernetes cluster:
helm install prometheus-exporter-0.1.0.tgz




