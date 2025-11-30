
class OutlineValidationChecker:
    def validate(self, outline):
        # Ensure title and sections exist
        return bool(outline and 'title' in outline and 'sections' in outline and len(outline['sections'])>0)

class BlogPostValidationChecker:
    def validate(self, post_md):
        # Very simple checks: non-empty and at least 3 headings
        if not post_md or len(post_md) < 50:
            return False
        return post_md.count('\n## ') >= 2
