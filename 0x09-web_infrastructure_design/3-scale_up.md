# Additional Components
- One Additional Server:
The addition of one more server introduces even greater redundancy and load distribution. In case one of the servers becomes unavailable or experiences high traffic load, the additional server ensures continuous website availability.

- Load-Balancers (HAProxy) Configured as a Cluster:
To distribute incoming web traffic efficiently and prevent overloading a single load balancer (preventing it from being a single point of failure), two load balancers are configured as a cluster. This approach provides high availability and load-balancing capabilities.

- Split Components into Dedicated Servers:
To optimize performance and resource allocation, each key component, including the web server, application server, and database, is hosted on its dedicated server. This separation ensures that each component can scale independently and prevents resource bottlenecks.
