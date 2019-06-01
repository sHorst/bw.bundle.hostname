files = {
    "/etc/hostname": {
        'content': node.hostname + "\n",
        'content_type': 'text',
        'owner': "root",
        'group': "root",
        'mode': "0444",
        'triggers': [
            "action:update_hostname",
        ],
    },
    "/etc/hosts": {
        'source': "hosts",
        'content_type': 'mako',
        'owner': "root",
        'group': "root",
        'mode': "0444",
    },
}

actions = {
    "update_hostname": {
        "command": "hostname -F /etc/hostname",
        'triggered': True,
    },
}

if node.has_bundle('rsyslog'):
    actions['update_hostname']['triggers'] = ["svc_upstart:rsyslog:restart"]
