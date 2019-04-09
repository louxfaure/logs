#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import logs
import test_module_aux

def Monmodule(texte) :
    log_module.warning(texte)

programme = 'test_log'
mode = 'INFO' #Niveau des messages à écrire dans les logs : DEBUG, INFO, WARNING, ERROR, CRITICAL
logs.init_logs('/home/loux/.Alma',programme,mode)
log_module = logging.getLogger(programme)

log_module.debug('debug')
log_module.info('Hello')
log_module.warning('Attention ! %s a planté dans %s' % ('machin','truc'))
Monmodule("Prout !")
log_module.info("Traitement en cours déxecution ({}%)".format(99))
test_module_aux.test_module_aux(programme)