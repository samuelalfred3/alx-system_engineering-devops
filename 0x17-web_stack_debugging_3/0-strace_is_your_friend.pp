# This Puppet manifest ensures that Apache is running and no other service is using port 80

exec { 'stop_conflicting_service':
  command => '/usr/bin/sudo systemctl stop nginx',
  onlyif  => '/usr/bin/lsof -i :80 | grep nginx',
  path    => ['/bin', '/usr/bin'],
}

service { 'apache2':
  ensure     => 'running',
  enable     => true,
  require    => Exec['stop_conflicting_service'],
}

