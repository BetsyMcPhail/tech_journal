#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
#  Copyright 2016 Open Source Electronic Health Record Alliance.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
###############################################################################
import six

from girder import events
from girder.models.model_base import ValidationException
from . import constants


def validateSettings(event):
    key, val = event.info['key'], event.info['value']

    if key == constants.PluginSettings.admin_email:
        if val:
            if not isinstance(val, six.string_types):
                raise ValidationException(
                    'Provenance Resources must be a string.', 'value')
            # accept comma or space separated lists
            resources = val.replace(",", " ").strip().split()
            # reformat to a comma-separated list
            event.info["value"] = ",".join(resources)
    event.preventDefault().stopPropagation()


def load(info):
  events.bind('model.setting.validate', 'journalMain', validateSettings)
  print "blah"
  print "balh"
