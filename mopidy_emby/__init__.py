from __future__ import unicode_literals

import logging
import os

from mopidy import config, ext


__version__ = '0.2.6'

logger = logging.getLogger(__name__)


class Extension(ext.Extension):

    dist_name = 'Mopidy-Emby'
    ext_name = 'emby'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(Extension, self).get_config_schema()
        schema['username'] = config.String()
        schema['user_id'] = config.String(optional=True)
        schema['password'] = config.Secret()
        schema['hostname'] = config.String()
        schema['port'] = config.Port()
        schema['album_format'] = config.String(optional=True)

        return schema

    def setup(self, registry):
        from .backend import EmbyBackend
        registry.add('backend', EmbyBackend)
