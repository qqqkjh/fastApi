import logging
import os
import time
from fastapi import Request
from app.utils.path import get_app_path

# find log setting file
logging.config.fileConfig(os.path.join(get_app_path(), 'logging.conf'), disable_existing_loggers=False)
# for root
logger = logging.getLogger(__name__)
# for title
title_logger = logging.getLogger("title")
# for content
content_logger = logging.getLogger("content")


# logger = logging.getLogger("app.api")

async def log_http(request: Request, call_next):
    title_logger.info(f"[{request.method}] Path= \"{request.url.path}\"")

    start_time = time.time()

    response = await call_next(request)

    end_time = time.time()

    process_time = (end_time - start_time) * 1000

    formatted_process_time = '{0:.2f}'.format(process_time)

    content_logger.info(
        f"completed_in={formatted_process_time}ms status_code={response.status_code} \n")

    return response
