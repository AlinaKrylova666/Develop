import logging
import os


def setup_logger(name, log_file, level=logging.INFO):
    """Функция для настройки логирования."""
    # Убедитесь, что папка для логов существует
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Настроить формат логов
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Создать обработчик для записи в файл
    handler = logging.FileHandler(log_file, mode='w')  # 'w' для перезаписи при каждом запуске
    handler.setFormatter(formatter)

    # Создать логгер
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# Пример использования:
logger = setup_logger('example_logger', '../../logs/example.log')
logger.info('This is an informational message.')
