from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

@dataclass
class StageResult:
    stage: str
    status: str
    produced_at: datetime = field(default_factory=datetime.utcnow)
    payload: dict[str, Any] = field(default_factory=dict)

class MlStage:
    """A3. Обучение и применение ML/NLP-моделей. NER по постам, классификация поля работы, агрегация промежуточных результатов."""

    stage_code = 'a3'

    def describe(self) -> dict[str, str]:
        return {
            'stage': self.stage_code,
            'title': 'A3. Обучение и применение ML/NLP-моделей',
            'description': 'NER по постам, классификация поля работы, агрегация промежуточных результатов.',
        }

    def run(self, **kwargs) -> StageResult:
        return StageResult(
            stage=self.stage_code,
            status='stub',
            payload={
                'message': 'Здесь начинается реализация a3. обучение и применение ml/nlp-моделей.',
                'input': kwargs,
            },
        )
