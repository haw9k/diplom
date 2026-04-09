from django import template
register = template.Library()

@register.filter
def stage_label(value):
    labels = {
        'a1': 'Сбор и синхронизация',
        'a2': 'Предобработка и верификация',
        'a3': 'ML/NLP-анализ',
        'a4': 'Оценка модели',
        'a5': 'Развертывание',
        'a6': 'Аналитика и UI',
        'a7': 'Мониторинг',
    }
    return labels.get(value, value)
