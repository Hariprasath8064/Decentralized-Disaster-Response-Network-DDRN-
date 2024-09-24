import matplotlib.pyplot as plt

# Data for Latency Test
lag_values = [50, 100, 500, 1000]
latency_values = [2807.7, 2817.98, 3207.43, 3705.65]

# Data for Packet Loss Test
packet_loss_values = [1, 5, 10, 20]
latency_packet_loss = [2699.26, 2695, 2670, 2670.10]

# Data for Bandwidth Test
bandwidth_values = [100, 500, 1000]
latency_bandwidth = [2708.71, 2688.99, 2824.53]

# Data for Combined Test
combined_conditions = ['Combined Test', 'Baseline Test', 'High Latency Test']
combined_latencies = [3207.38, 2835.12, 2889.41]

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Latency Test
axs[0, 0].plot(lag_values, latency_values, marker='o')
axs[0, 0].set_title('Latency vs. Lag (ms)')
axs[0, 0].set_xlabel('Lag (ms)')
axs[0, 0].set_ylabel('Latency (ms)')
axs[0, 0].grid()

# Packet Loss Test
axs[0, 1].plot(packet_loss_values, latency_packet_loss, marker='o', color='orange')
axs[0, 1].set_title('Latency vs. Packet Loss (%)')
axs[0, 1].set_xlabel('Packet Loss (%)')
axs[0, 1].set_ylabel('Latency (ms)')
axs[0, 1].grid()

# Bandwidth Test
axs[1, 0].plot(bandwidth_values, latency_bandwidth, marker='o', color='green')
axs[1, 0].set_title('Latency vs. Bandwidth (KB/s)')
axs[1, 0].set_xlabel('Bandwidth (KB/s)')
axs[1, 0].set_ylabel('Latency (ms)')
axs[1, 0].grid()

# Combined Test
axs[1, 1].plot(combined_conditions, combined_latencies, marker='o', color='red')
axs[1, 1].set_title('Latency vs. Combined Conditions')
axs[1, 1].set_xlabel('Test Type')
axs[1, 1].set_ylabel('Latency (ms)')
axs[1, 1].grid()

plt.tight_layout()
plt.show()

