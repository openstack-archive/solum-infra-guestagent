# Copyright 2014 - Numergy
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import os
import sys

from oslo_config import cfg

from solum_guestagent.openstack.common import log as logging

QUEUE_ID_OPTS = [
    cfg.StrOpt(
        'queue_id', default=None,
        help='Identifier of the queue consumed by the agent.')]


CONF = cfg.CONF
CONF.register_opts(QUEUE_ID_OPTS)


LOG = logging.getLogger(__name__)


def main():
    cfg.CONF(sys.argv[1:], project='solum_guestagent')
    logging.setup('solum_guestagent')

    LOG.info('Starting solum_guestagent in PID %s with %s as queue_id.'
             % os.getpid(), CONF.queue_id)

    # TODO(stannie): Add marconi queues consumption by queue_id
