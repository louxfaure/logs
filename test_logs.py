#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logs 
programme = 'test_log'
mode = 'INFO'
logs.init_logs('/home/loux/.Alma',programme,mode)
log_module = logging.getLogger(programme)

log_module.debug('debug')
log_module.info('Hello')
log_module.warning('Atention')