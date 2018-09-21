# fix server
exec { 'script':
  command => '/bin/sed -i "s/15/3000/g" /etc/default/nginx; sudo service nginx restart'
}
