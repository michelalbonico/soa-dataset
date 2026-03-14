# soa-dataset
A dataset with service-oriented software on GitHub implemented on the top-5 programming languages.

## Set up your Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements
```

## Mining the top repositories

Set your GitHub Token:

```bash
export GITHUB_TOKEN=yourtoken
```

Then, mine the repositories:

```bash
python3 mining/mine-language-repo.py
```

The results are stored in the repos repository.

## GPT-based Classification

Set your OpenAI API Key:

```bash
export API_KEY=yourkey
```

Then, classify the repositories (ONLY A SINGLE FILE SO FAR):

```bash
python3 filtering/select-soa.py
```

The results are stored in the repos repository, with the tag `classified`.
