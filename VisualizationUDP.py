import matplotlib.pyplot as plt

# Data for the tests
test_names = ['Baseline', 'Normal Scenario', 'High Latency', 'Packet Loss Test', 
              'Reordering & Duplication', 'Throttling', 'Severe Throttling', 'Extreme Conditions']

latency_values = [168.36, 106.08, 199.57, 166.73, 103.47, 191.81, 108.52, 152.26]
packet_loss_values = [25.00, 0.00, 20.00, 14.29, 33.33, 0.00, 50.00, 50.00]
bandwidth_values = [1253.27, 4524.78, 1332.85, 2189.14, 1507.60, 1068.75, 949.14, 676.49]

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

# Latency Test
axs[0].plot(test_names, latency_values, marker='o', color='blue')
axs[0].set_title('Latency Test (ms)')
axs[0].set_xlabel('Test Type')
axs[0].set_ylabel('Latency (ms)')
axs[0].grid()

# Packet Loss Test
axs[1].plot(test_names, packet_loss_values, marker='o', color='orange')
axs[1].set_title('Packet Loss Test (%)')
axs[1].set_xlabel('Test Type')
axs[1].set_ylabel('Packet Loss (%)')
axs[1].grid()

# Bandwidth Test (Throughput)
axs[2].plot(test_names, bandwidth_values, marker='o', color='green')
axs[2].set_title('Bandwidth Test (Bytes/sec)')
axs[2].set_xlabel('Test Type')
axs[2].set_ylabel('Throughput (Bytes/sec)')
axs[2].grid()

plt.tight_layout()
plt.show()

