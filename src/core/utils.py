from src.models.enums import Environment

def is_testing(value):
    return value.lower() == Environment.TEST.value

def is_production(value):
    return value.lower() == Environment.PRODUCTION.value

