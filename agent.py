"""
CENTURION
Trust Intelligence for the Agent Economy.

Core pipeline:
Observe -> Analyze -> Decide
"""

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class IntelligenceSignal:
    source: str
    content: str
    relevance: float = 0.0


class CenturionAgent:
    """
    Autonomous intelligence agent for transforming
    information streams into structured decision support.
    """

    def observe(self, inputs: List[str]) -> List[IntelligenceSignal]:
        """Convert raw inputs into structured intelligence signals."""
        signals = []

        for item in inputs:
            cleaned = item.strip()

            if cleaned:
                signals.append(
                    IntelligenceSignal(
                        source="input",
                        content=cleaned,
                    )
                )

        return signals

    def analyze(
        self,
        signals: List[IntelligenceSignal],
    ) -> List[IntelligenceSignal]:
        """
        Rank observed signals by relevance.

        This deterministic scoring layer is a prototype.
        High-performance model inference can later replace
        or augment this stage.
        """

        for signal in signals:
            signal.relevance = self._estimate_relevance(
                signal.content
            )

        return sorted(
            signals,
            key=lambda signal: signal.relevance,
            reverse=True,
        )

    def decide(
        self,
        signals: List[IntelligenceSignal],
    ) -> Dict:
        """Transform ranked intelligence into a structured output."""

        if not signals:
            return {
                "status": "NO_SIGNAL",
                "confidence": 0.0,
                "action": "Continue monitoring.",
            }

        primary = signals[0]

        return {
            "status": "SIGNAL_DETECTED",
            "confidence": round(primary.relevance, 2),
            "primary_signal": primary.content,
            "action": "Escalate for deeper inference analysis.",
        }

    @staticmethod
    def _estimate_relevance(content: str) -> float:
        """
        Temporary deterministic relevance estimator.

        Future versions will use inference-based
        semantic scoring and contextual reasoning.
        """

        word_count = len(content.split())

        return min(
            word_count / 100,
            1.0,
        )


if __name__ == "__main__":
    agent = CenturionAgent()

    observations = agent.observe(
        [
            "New development detected in the agent economy.",
            "Routine informational noise.",
            "Significant change observed in autonomous agent activity.",
        ]
    )

    analysis = agent.analyze(observations)
    decision = agent.decide(analysis)

    print(decision)
