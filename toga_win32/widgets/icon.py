from __future__ import print_function, absolute_import, division, unicode_literals

import os
import toga

from ..libs import user32
from ..libs.constants import NULL, IDI_WINLOGO


class Icon(object):
    app_icon = None

    def __init__(self, path, system=False):
        self.path = path
        self.system = system

        if self.system:
            filename = os.path.join(os.path.dirname(toga.__file__), 'resources', self.path)
        else:
            filename = self.path

        #self._impl = user32.LoadIconW(NULL, IDI_WINLOGO)  # FIXME: *actually* load the specified resource

    @staticmethod
    def load(path_or_icon, default=None):
        if path_or_icon:
            if isinstance(path_or_icon, Icon):
                obj = path_or_icon
            else:
                obj = Icon(path_or_icon)
        elif default:
            obj = default
        return obj


TIBERIUS_ICON = Icon('tiberius.icns', system=True)
