# webstack debugging 3
exec { 'run' :
    command  => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g"\
    /var/www/html/wp-settings.php; sudo service apache2 restart',
    provider => 'shell'
}

