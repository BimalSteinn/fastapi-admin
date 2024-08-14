from fastapi_app.logger import logger


def fastapi_app_help(args):

    help_text = open("fastapi_app/static/help.txt", "r").read()
    logger.info(help_text)
