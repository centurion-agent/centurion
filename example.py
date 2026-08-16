from agent import CenturionAgent
from inference import (
    MockInferenceProvider,
    InferenceRequest,
    build_intelligence_prompt,
)


def main():
    agent = CenturionAgent()
    inference = MockInferenceProvider()

    raw_information = [
        "Autonomous agent activity increased significantly.",
        "A new infrastructure protocol entered the agent economy.",
        "Routine market commentary with no material change.",
    ]

    # OBSERVE
    signals = agent.observe(raw_information)

    # ANALYZE
    ranked_signals = agent.analyze(signals)

    # INFERENCE
    primary_signal = ranked_signals[0]

    request = InferenceRequest(
        prompt=build_intelligence_prompt(
            primary_signal.content
        )
    )

    intelligence = inference.generate(request)

    # DECIDE
    decision = agent.decide(ranked_signals)

    print("CENTURION")
    print("Observe. Analyze. Decide.")
    print()
    print("Primary signal:", primary_signal.content)
    print("Inference:", intelligence.text)
    print("Decision:", decision)


if __name__ == "__main__":
    main()
