import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    """Функция для настройки логирования."""
    # Убедитесь, что папка для логов существует
    if not os.path.exists('logs'):
        os.makedirs('logs')

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
