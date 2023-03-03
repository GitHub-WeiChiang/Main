from loguru import logger

def format_log():
    trace = logger.add('sample.log', format="{time:YYYY-MM-DD HH:mm:ss} {extra[ip]}  {extra[username]} {level} From {module}.{function} : {message}")
    
    extra_logger = logger.bind(ip="192.168.0.1", username="albert")
    extra_logger.info('This is info information')

    extra_logger.bind(
        ip="192.168.0.2",
        username="albert2"
    ).info('This is warn information')

if __name__ == '__main__':
    format_log()
