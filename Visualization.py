import matplotlib.pyplot as plt

# Data for tests
test_names_latencies = ['Baseline', 'Latency (50)', 'Latency (100)', 'Latency (500)', 'Latency (1000)']
latency_values_latencies = [2835.12, 2886.54, 2940.11, 3326.54, 3829.44]
response_times_latencies = [5670.23, 5773.07, 5880.22, 6653.07, 7658.88]

test_names_package_drop = ['Package Drop (0%)', 'Package Drop (1%)', 'Package Drop (5%)', 'Package Drop (10%)', 'Package Drop (20%)']
latency_values_package_drop = [2839.44, 2999.96, 3265.31, 2818.04, 3829.44]
response_times_package_drop = [5678.88, 5999.93, 6530.63, 5636.08, 7658.88]

test_names_bandwidth_combined = ['Bandwidth Test (1)', 'Bandwidth Test (2)', 'Bandwidth Test (3)', 'Combined Test', 'High Latency']
latency_values_bandwidth_combined = [2845.29, 2828.02, 2827.68, 2968.69, 3038.77]
response_times_bandwidth_combined = [5690.58, 5656.03, 5655.36, 5937.38, 6077.54]

# 1. Latency and Response Time for Baseline and Latencies
plt.figure(figsize=(10, 6))
plt.plot(test_names_latencies, latency_values_latencies, label="Latency (ms)", marker='o', color='b')
plt.plot(test_names_latencies, response_times_latencies, label="Response Time (ms)", marker='x', color='g')
plt.title('Latency and Response Time - Baseline and Latencies')
plt.xlabel('Tests')
plt.ylabel('Time (ms)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Latency and Response Time for Package Drops
plt.figure(figsize=(10, 6))
plt.plot(test_names_package_drop, latency_values_package_drop, label="Latency (ms)", marker='o', color='b')
plt.plot(test_names_package_drop, response_times_package_drop, label="Response Time (ms)", marker='x', color='g')
plt.title('Latency and Response Time - Package Drops')
plt.xlabel('Tests')
plt.ylabel('Time (ms)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 3. Latency and Response Time for Bandwidth and Combined Tests
plt.figure(figsize=(10, 6))
plt.plot(test_names_bandwidth_combined, latency_values_bandwidth_combined, label="Latency (ms)", marker='o', color='b')
plt.plot(test_names_bandwidth_combined, response_times_bandwidth_combined, label="Response Time (ms)", marker='x', color='g')
plt.title('Latency and Response Time - Bandwidth and Combined Tests')
plt.xlabel('Tests')
plt.ylabel('Time (ms)')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
