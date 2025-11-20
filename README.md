# DORA-Mimir-GCP
Built a scalable DORA metrics pipeline. Docker simulates metrics (DF, CFR, MTTR) &amp; Prometheus streams them via remote write to a monolithic Mimir instance on GCP. Mimir uses GCS for durable storage, decoupling local collection from production persistence. This enables centralized, high-availability DORA analytics in Grafana.
