"""Latency and cost benchmark for the SDG RAG system. Run on the deployment account.

This harness publishes no numbers of its own. It measures them where the system actually runs,
because a latency claim without a measurement location, payload and percentile is advertising.
Fill docs/MEASUREMENT_PLAN.md from its output.
"""
import json, statistics, time, urllib.request

ENDPOINT = "https://your-lambda-endpoint.example"   # replace with the deployed invoke URL
PAYLOADS = ["What does SDG 11 say about informal settlements?",
            "Summarise the monitoring framework for urban resilience.",
            "Which indicators cover public space and transport?"]
WARMUP, REPS = 3, 30


def call(payload):
    t0 = time.perf_counter()
    req = urllib.request.Request(ENDPOINT, data=json.dumps({"query": payload}).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        r.read()
    return (time.perf_counter() - t0) * 1000


def main():
    for _ in range(WARMUP):
        call(PAYLOADS[0])
    lat = sorted(call(p) for p in PAYLOADS for _ in range(REPS))
    out = {"n": len(lat), "p50_ms": round(statistics.median(lat), 1),
           "p90_ms": round(lat[int(.9 * len(lat)) - 1], 1),
           "p95_ms": round(lat[int(.95 * len(lat)) - 1], 1),
           "max_ms": round(lat[-1], 1), "measured_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "endpoint": ENDPOINT, "payloads": PAYLOADS}
    print(json.dumps(out, indent=2))
    with open("latency_result.json", "w") as f:
        json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
