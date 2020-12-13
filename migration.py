def migration(config):
    return migration5to6(config)

def migration6to7(config):
    new_config = config
    return new_config

def migration5to6(config):
    new_config = config
    new_config['version'] = 6 
    return new_config