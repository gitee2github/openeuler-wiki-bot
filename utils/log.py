#!/usr/bin/env python3

import logging.handlers
from datetime import datetime
import shutil
import gzip
import os

from utils.conf import LOG_FILE_DIR
from utils.conf import LOG_FILE_NAME
from utils.conf import MAX_BYTES
from utils.conf import BACKUP_COUNT


class CompressedRotatingFileHandler(logging.handlers.RotatingFileHandler):
    def do_rollover(self):
        if self.stream:
            self.stream.close()
        if self.backupCount > 0:
            now = datetime.utcnow()
            dfn = self.baseFilename + now.strftime('%Y-%m-%d_%H_%M') + ".gz"
            with open(self.baseFilename, 'rb') \
                    as f_in, gzip.open(dfn, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        self.mode = 'w'
        self.stream = self._open()


def logging_init(logdir, filename, maxbytes, backupcount):
    if not os.path.exists(logdir):
        os.makedirs(logdir, mode=0o644)

    filename = os.path.join(
        logdir,
        filename + "_" + "runtime" + ".log"
    )
    log_object = logging.getLogger(filename)
    log_object.propagate = False
    log_object.setLevel(logging.DEBUG)

    file_handler = CompressedRotatingFileHandler(filename=filename,
                                                 maxBytes=int(maxbytes),
                                                 backupCount=int(backupcount))

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s -"
        " %(filename)s:%(lineno)d - %(message)s")
    file_handler.setFormatter(formatter)
    log_object.addHandler(file_handler)
    return log_object


logger = logging_init(LOG_FILE_DIR, LOG_FILE_NAME, MAX_BYTES, BACKUP_COUNT)