# Ensure Nginx is installed
class { 'nginx':
  ensure => 'installed',
}

# Create necessary directories
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Create the index.html file with simple content
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><head></head><body>Holberton School</body></html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Create a symbolic link to /data/web_static/releases/test/
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/hbnb_static':
  ensure  => 'present',
  content => "server {
    listen 80;
    server_name mydomainname.tech;
    location /hbnb_static {
        alias /data/web_static/current;
    }
}
",
  owner   => 'root',
  group   => 'root',
}

# Create a symbolic link to enable the configuration
file { '/etc/nginx/sites-enabled/hbnb_static':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/hbnb_static',
  owner   => 'root',
  group   => 'root',
  require => File['/etc/nginx/sites-available/hbnb_static'],
}

# Restart Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => 'true',
  require => File['/etc/nginx/sites-enabled/hbnb_static'],
}
