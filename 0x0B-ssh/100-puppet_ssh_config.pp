# Puppet manifest to configure SSH client

augeas { 'Declare identity file':
  context => '/files/etc/ssh/ssh_config',
  changes => [
    'set Host/*/IdentityFile ~/.ssh/school',
    'set Host/*/PasswordAuthentication no',
  ],
}
