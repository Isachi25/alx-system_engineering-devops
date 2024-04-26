# Kills a process named killmenow using pkill

exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => ['/usr/bin', '/usr/sbin', '/bin'],
  refreshonly => true,
}

