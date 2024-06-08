# Puppet script to fix bad `phpp` extensions to `php` in wp-setings.php

exec { 'fix the php extension bug':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
