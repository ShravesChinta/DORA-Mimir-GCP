from prometheus_client import CollectorRegistry, Gauge, push_to_gateway
import random
import datetime

# Pushgateway URL (use Docker hostname if running in container network)
PUSHGATEWAY_URL = "http://pushgateway:9091"

TEAM_NAMES = [
    "Payments_Core", "Payments_API", "Loans_Underwriting", "Loans_Processing",
    "Risk_Fraud", "Risk_CreditScoring", "Risk_Compliance",
    "Core_Banking_Ledger", "Core_Banking_Accounts",
    "Cards_Issuing", "Cards_Processing", "Cards_Fraud",
    "Customer_Experience_Web", "Customer_Experience_Mobile",
    "Customer_Experience_Chatbot",
    "Trading_Equities", "Trading_FixedIncome", "Trading_Derivatives",
    "Wealth_Management", "Treasury_Operations", "Identity_Access",
    "Security_AppSec", "Security_InfraSec",
    "DevOps_Platform", "DevOps_Tooling",
    "Cloud_Foundation", "Cloud_Migration",
    "Data_Engineering", "Data_Platform", "Data_Governance",
    "Analytics_ML", "Analytics_BI",
    "API_Gateway", "Integration_ESB",
    "Open_Banking", "Branch_Systems",
    "ATM_Services", "Corporate_Banking", "Merchant_Services"
]

# 1 year of metrics
start_date = datetime.datetime.now() - datetime.timedelta(days=365)

def generate_metrics(team):
    """Return a dict of DORA metrics for a single team"""
    return {
        "dora_deployment_frequency": random.randint(0, 10),
        "dora_lead_time_ms": random.randint(10, 2000),
        "dora_change_failure_rate": round(random.uniform(0.0, 0.3), 2),
        "dora_mttr_minutes": random.randint(10, 500)
    }

if __name__ == "__main__":
    print("Python generator started...")

    current = start_date
    for _ in range(365):
        registry = CollectorRegistry()

        gauges = {
            "dora_deployment_frequency": Gauge("dora_deployment_frequency", "Deployment frequency per team", ["team"], registry=registry),
            "dora_lead_time_ms": Gauge("dora_lead_time_ms", "Lead time in ms per team", ["team"], registry=registry),
            "dora_change_failure_rate": Gauge("dora_change_failure_rate", "Change failure rate per team", ["team"], registry=registry),
            "dora_mttr_minutes": Gauge("dora_mttr_minutes", "Mean time to recovery in minutes per team", ["team"], registry=registry)
        }

        for team in TEAM_NAMES:
            metrics = generate_metrics(team)
            for metric_name, value in metrics.items():
                gauges[metric_name].labels(team=team).set(value)

        push_to_gateway(
            PUSHGATEWAY_URL,
            job="dora_metrics",
            registry=registry
        )

        current += datetime.timedelta(days=1)

    print("Finished pushing 1 year of DORA metrics.")
