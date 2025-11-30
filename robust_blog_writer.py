
class RobustBlogWriter:
    def __init__(self):
        pass

    def write_from_outline(self, outline, codebase_context, metadata):
        # Create a simple markdown draft from outline
        lines = []
        lines.append(f"# {outline['title']}")
        lines.append("\n")
        if 'notes' in outline:
            lines.append(f"_Note: {outline['notes']}_\n")
        for sec in outline['sections']:
            lines.append(f"## {sec['heading']}")
            for p in sec['points']:
                lines.append(f"- {p}")
            lines.append('\n')
        # Add a short auto-generated codebase summary
        files = codebase_context.get('files', [])
        if files:
            lines.append('### Codebase files\n')
            for f in files[:20]:
                lines.append(f"- {f}")
        return '\n'.join(lines)
