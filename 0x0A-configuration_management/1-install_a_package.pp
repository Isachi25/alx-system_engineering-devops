#!/usr/bin/puppet

# Installs a specific flask version from pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

