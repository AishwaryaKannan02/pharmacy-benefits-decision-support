
import os, sys
# add project root to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.blogger_agent import BloggerAgent

def main():
    agent = BloggerAgent(codebase_path='.')  # point to project root to include files
    result = agent.generate_blog('Pharmacy Prior Authorization Predictor - System Overview', metadata={'author':'AutoGen'})
    print('Markdown saved to:', result['md_path'])
    print('\n--- Social Snippets ---\n')
    for k,v in result['social'].items():
        print(f"{k}:\n{v}\n")

if __name__ == '__main__':
    main()
