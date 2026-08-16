"""
CENTURION inference layer.

This module defines the interface between Centurion's
reasoning pipeline and external high-performance model inference.
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass
class InferenceRequest:
    prompt: str
    context: str = ""
    temperature: float = 0.2


@dataclass
class InferenceResponse:
    text: str
    model: str
    confidence: float | None = None


class InferenceProvider(Protocol):
    def generate(self, request: InferenceRequest) -> InferenceResponse:
        ...


class MockInferenceProvider:
    """
    Safe local placeholder used during development.

    This provider performs no external API call and spends no credits.
    It exists so Centurion's architecture can be tested before
    connecting a production inference backend.
    """

    model_name = "mock-centurion-v0"

    def generate(self, request: InferenceRequest) -> InferenceResponse:
        text = (
            "Mock inference result. "
            "Production inference provider not configured yet."
        )

        return InferenceResponse(
            text=text,
            model=self.model_name,
            confidence=None,
        )


def build_intelligence_prompt(
    signal: str,
    objective: str = "Produce concise decision intelligence.",
) -> str:
    return f"""
You are Centurion, an autonomous intelligence agent.

OBJECTIVE:
{objective}

SIGNAL:
{signal}

Analyze:
1. What happened?
2. Why does it matter?
3. What are the strongest signals?
4. What uncertainty remains?
5. What action or monitoring priority follows?

Return a concise, evidence-oriented intelligence assessment.
""".strip()


if __name__ == "__main__":
    provider = MockInferenceProvider()

    request = InferenceRequest(
        prompt=build_intelligence_prompt(
            "Agent-to-agent transaction activity increased sharply."
        )
    )

    response = provider.generate(request)

    print(response)
