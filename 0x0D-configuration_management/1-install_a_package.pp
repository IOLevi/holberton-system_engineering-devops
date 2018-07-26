# install puppet-lint
exec { 'run' :
    command  => 'gem install puppet-lint -v 2.1.1',
    provider => 'shell'
}

