# Why Additional Elements are Added:
- Each additional element in the infrastructure is added to improve reliability, scalability, and performance.
- For example, adding a load balancer helps distribute incoming traffic across multiple servers, reducing the load on any single server and improving overall performance.
- Similarly, implementing a database Primary-Replica cluster enhances data availability and fault tolerance by replicating data across multiple nodes.


# Load Balancer Distribution Algorithm:
- The load balancer is configured with a round-robin distribution algorithm.
- This algorithm distributes incoming requests evenly across the available backend servers in a circular manner.
- Each request is forwarded to the next server in the rotation, ensuring that no single server becomes overloaded with traffic.

# Active-Active vs. Active-Passive Setup:
- The load balancer enables an Active-Active setup.
- In an Active-Active setup, all backend servers actively handle incoming requests simultaneously.
- This setup provides higher scalability and availability because all servers are utilized to serve traffic.
- In contrast, an Active-Passive setup involves one server (active) handling incoming requests while the other server (passive) remains idle unless the active server fails.
- Active-Passive setups are less efficient in terms of resource utilization but can provide higher fault tolerance as a backup server is available to take over if the active server fails.

# Primary-Replica (Master-Slave) Database Cluster:
- In a Primary-Replica cluster, the primary node (master) is responsible for handling read and write operations.
- Write operations (inserts, updates, deletes) are performed on the primary node, and the changes are replicated to one or more replica nodes (slaves).
- Replica nodes synchronize data with the primary node through replication processes.
- Read operations can be distributed across both the primary and replica nodes to improve performance and scalability.

# Difference Between Primary and Replica Nodes:
- The primary node handles write operations and serves as the authoritative source of data.
- Write operations are performed directly on the primary node, ensuring consistency and data integrity.
- Replica nodes receive replicated data from the primary node and can serve read operations to offload read traffic from the primary node.
- Replica nodes can also be promoted to the primary role in the event of a primary node failure, ensuring high availability and fault tolerance.

## Issues with This Infrastructure:
- Single Point of Failure (SPOF): A potential SPOF exists in the load balancer. If the load balancer fails, traffic distribution is disrupted. Implementing a redundant load balancer can mitigate this issue.

- Security Issues: The infrastructure doesn't include a firewall or HTTPS. A firewall should be added to filter and secure incoming traffic, and enabling HTTPS is essential for encrypting data in transit.

- Monitoring: The infrastructure lacks monitoring capabilities, making it challenging to detect and address issues proactively. Implementing monitoring tools is crucial for maintaining system health and performance.
