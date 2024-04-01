# Puppet manifest to create a custom HTTP header response

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Define a file resource for Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('/root/alx-system_engineering-devops/0x0F-load_balancer/default.erb'),
  notify  => Service['nginx'],
}

# Define Nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

