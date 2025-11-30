# Pharmacy Prior Authorization Predictor + Multi-Agent Blogging System

This project contains:
- Synthetic dataset and Logistic Regression model (see /data and /models)
- Inference code
- A lightweight multi-agent blogging system that generates technical blog posts
  from codebase/context and model metadata.

Folders:
- agents/        : agent implementations (blogger_agent and sub-agents)
- tools/         : utility tools (save_blog_post_to_file, analyze_codebase, validators)
- src/           : example inference and orchestration scripts
- data/          : synthetic dataset (generated separately)
- models/        : model file (generated separately)
- notebooks/     : example notebooks
- docs/          : architecture and documentation

Run example:
```bash
python3 src/run_blog_generation.py
```
