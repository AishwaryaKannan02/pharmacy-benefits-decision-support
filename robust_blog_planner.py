
class RobustBlogPlanner:
    def __init__(self):
        pass

    def create_outline(self, topic, codebase_context, metadata):
        # Basic planner that uses topic + context to make an outline
        outline = {
            'title': topic,
            'sections': [
                {'heading': 'Project Overview', 'points': ['Purpose', 'Scope']},
                {'heading': 'Dataset and Model', 'points': ['Dataset description', 'Model architecture', 'Performance']},
                {'heading': 'System Architecture', 'points': ['Components', 'Flow']},
                {'heading': 'How to Run', 'points': ['Notebook', 'API', 'Files']},
                {'heading': 'Conclusion', 'points': ['Outcomes', 'Next steps']}
            ],
            'metadata': metadata
        }
        # incorporate small hint from codebase_context
        if codebase_context.get('files'):
            outline['notes'] = f"Codebase has {len(codebase_context['files'])} files.""
        return outline
