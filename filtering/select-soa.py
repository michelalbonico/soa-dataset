import pandas as pd
import time
from openai import OpenAI
import os

API_KEY = os.getenv("API_KEY")

# Initialize client
client = OpenAI(api_key=API_KEY)

INPUT_FILE = "./repos/github_java_repos.csv"
OUTPUT_FILE = "./repos/github_java_repos_soa_classified.csv"

df = pd.read_csv(INPUT_FILE)

def classify_repo(description, readme):

    text = f"""
Repository description:
{description}

README:
{readme}
"""

    prompt = """
You are analyzing GitHub repositories.

Determine whether the project implements or clearly describes a
Service-Oriented Architecture (SOA) or microservices architecture.

Criteria for SOA:
- multiple independent services
- services communicating via APIs (REST, gRPC, messaging)
- service-based or microservices architecture
- service registry, API gateway, distributed services

Return ONLY one of the following labels:

SOA
NOT_SOA
UNCLEAR
"""

    response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": text}
        ]
    )

    label = response.choices[0].message.content.strip()
    return label


results = []

for i, row in df.iterrows():

    description = str(row.get("description", ""))
    readme = str(row.get("readme", ""))

    try:
        label = classify_repo(description, readme)
    except Exception as e:
        print("Error:", e)
        label = "ERROR"

    results.append(label)

    print(i, row["name"], label)

    # avoid rate limits
    time.sleep(1)


df["soa_architecture"] = results
df.to_csv(OUTPUT_FILE, index=False)

print("Saved to", OUTPUT_FILE)