# Adding Additional Elements:
- Additional elements such as firewalls, HTTPS, and monitoring tools are added to enhance the security, reliability, and performance of the web infrastructure.
- Firewalls help control and filter incoming and outgoing network traffic to protect against unauthorized access, malicious attacks, and data breaches.
- HTTPS encrypts the data transmitted between the client (user) and the server, ensuring confidentiality and integrity of the information exchanged.
- Monitoring tools provide visibility into the performance, availability, and health of the web infrastructure, allowing administrators to detect and address issues proactively.

# Firewalls:

- Firewalls are network security devices that monitor and control incoming and outgoing traffic based on predefined security rules.
- They act as a barrier between a trusted internal network and untrusted external networks (such as the Internet), blocking or allowing traffic based on security policies.
- Firewalls help protect against various network threats, including unauthorized access, malware, denial-of-service (DoS) attacks, and data exfiltration.

# HTTPS:

- Traffic is served over HTTPS (HTTP Secure) to encrypt the data transmitted between the client (user) and the server.
- HTTPS uses SSL/TLS encryption to secure the communication channel, protecting sensitive information (such as login credentials, personal data, and financial transactions) from eavesdropping and tampering.
- By encrypting traffic, HTTPS helps ensure the confidentiality, integrity, and authenticity of the data exchanged between the client and the server.

# Monitoring:

- Monitoring is used to continuously track and assess the performance, availability, and health of the web infrastructure.
- It involves collecting and analyzing various metrics, logs, and events from different components (such as servers, network devices, databases, and applications) to identify issues, trends, and anomalies.
- Monitoring helps administrators detect and diagnose problems, optimize resource utilization, and ensure that the infrastructure meets performance and reliability requirements.

# Data Collection by Monitoring Tool:

- The monitoring tool collects data from various sources within the web infrastructure, including:
- Server metrics (CPU usage, memory utilization, disk I/O, network traffic)
- Network metrics (bandwidth usage, latency, packet loss)
- Application metrics (response time, error rate, throughput)
- Log files (system logs, application logs, access logs)
- Data collection methods may include polling, agents, log parsing, APIs, and integrations with other systems and services.

# Monitoring Web Server QPS:
- To monitor the web server's QPS (Queries Per Second), you can configure the monitoring tool to collect and analyze relevant metrics related to HTTP requests and responses.
- Metrics such as request rate, response time, and error rate can be monitored to assess the server's performance and capacity.
- Additionally, you can set up alerts to notify administrators if the QPS exceeds predefined thresholds, indicating potential performance issues or increased traffic load.
- By monitoring QPS, administrators can ensure that the web server can handle incoming requests efficiently and scale resources as needed to meet demand.

## Issues with This Infrastructure:
- Terminating SSL at the Load Balancer Level:
Terminating SSL at the load balancer can be problematic as it may expose unencrypted traffic between the load balancer and the web servers. Encrypting traffic across the entire communication path is crucial for maintaining data integrity.

- Having Servers with All the Same Components:
Deploying servers with identical components for web, application, and database servers may lead to uneven resource consumption. Depending on the specific needs of each component, resource allocation should be tailored to optimize performance.

- Single MySQL Server for Writes:
Relying on a single MySQL server for write operations poses a single point of failure. Implementing a primary replica cluster for MySQL is advisable to ensure data availability and redundancy.
