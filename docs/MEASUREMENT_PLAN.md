# Measurement plan for the RAG case study

The case study currently states sub-500 ms latency in low-connectivity conditions and a 40 per cent
retrieval time reduction. Both are carried over from the original build notes. Neither is published
here with a method yet, and the case study says so. This plan closes that gap without inventing
numbers.

1. Run bench/latency_bench.py from a Nairobi residential connection and from a throttled connection
   capped at 3G speeds, because the low-connectivity claim is conditional on it.
2. Record p50, p90 and p95 over at least 90 calls across the three payload classes, after three
   warm-up calls, against the deployed Lambda endpoint.
3. Record cold-start latency separately, as its own distribution, because serverless p50 hides it.
4. Re-measure the manual baseline: time five programme staff locating the same answers in the
   document set unaided, twice, and report the median of the paired differences.
5. Publish all of it in the case study numbers section with date, endpoint, payload list and
   connection profile. If a figure does not reproduce, the case study is corrected rather than
   defended.

Cost per query: read Lambda duration and memory from the account billing export for the benchmark
window and divide by call count. Publish the currency and the date.
