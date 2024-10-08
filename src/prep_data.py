import pandas as pd

df = pd.read_csv("s3://connor-dev/autoarena-qlora/train/judge_votes.csv")

# Instruction should be system prompt
df["instruction"] = """You are a human preference judge tasked with deciding which of the two assistant responses, A or B, better responds to the user's prompt.
Respond with ONLY "A" if assistant A is better, "B" if assistant B is better, or "-" if neither is better than the other."""
# Input should a string containing the input, response A and response B.
# TODO: Experiment with different token seperators e.g. descriptive XML like tags
df["input"] = df.apply(lambda x: f"[INST]{x["prompt"]}[/INST]\n[A]{x["responseA"]}[/A]\n[B]{x["responseB"]}[/B]", axis=1)
df.drop(columns=["prompt", "responseA", "responseB"], inplace=True)
# Output should be the models prediction
df.rename(columns={"winner": "output"}, inplace=True)
# NOTE: Truncated to 250 datapoints while iterating
df[:250].to_json("../data/judge_votes_250.jsonl", orient="records", lines=True)
