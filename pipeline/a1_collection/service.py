from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

@dataclass
class StageResult:
    stage: str
    status: str
    produced_at: datetime = field(default_factory=datetime.utcnow)
    payload: dict[str, Any] = field(default_factory=dict)

class CollectionStage:
    """A1. Сбор и синхронизация данных. Получение данных из VK, hh.ru и локальных справочников; полная и инкрементальная синхронизация."""

    stage_code = 'a1'

    def describe(self) -> dict[str, str]:
        return {
            'stage': self.stage_code,
            'title': 'A1. Сбор и синхронизация данных',
            'description': 'Получение данных из VK, hh.ru и локальных справочников; полная и инкрементальная синхронизация.',
        }

    def run(self, **kwargs) -> StageResult:
        return StageResult(
            stage=self.stage_code,
            status='stub',
            payload={
                'message': 'Здесь начинается реализация a1. сбор и синхронизация данных.',
                'input': kwargs,
            },
        )
