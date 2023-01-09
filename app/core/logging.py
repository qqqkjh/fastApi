import logging
import time
from fastapi import Request

from app.utils.converter import time_float_to_str

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)
title = logging.getLogger("title")
#logger = logging.getLogger("app.api")

async def log_http(request: Request, call_next):
    title.info(f"[{request.method}] Path= \"{request.url.path}\"")

    start_time = time.time()

    response = await call_next(request)

    end_time = time.time()

    process_time = (end_time - start_time) * 1000

    formatted_process_time = '{0:.2f}'.format(process_time)
    formatted_check_time = f'{time_float_to_str(start_time)} ~ {time_float_to_str(end_time)}'

    logger.info(
        f"completed_in={formatted_process_time}ms status_code={response.status_code} \n")


    return response


