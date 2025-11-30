
import os
from tools.analyze_codebase import analyze_codebase
from tools.save_blog_post_to_file import save_blog_post_to_file
from agents.robust_blog_planner import RobustBlogPlanner
from agents.robust_blog_writer import RobustBlogWriter
from agents.blog_editor import BlogEditor
from agents.social_media_writer import SocialMediaWriter
from tools.validators import OutlineValidationChecker, BlogPostValidationChecker

class BloggerAgent:
    """Master orchestrator that uses sub-agents to create a blog post."""
    def __init__(self, codebase_path='.'):
        self.codebase_path = codebase_path
        self.planner = RobustBlogPlanner()
        self.writer = RobustBlogWriter()
        self.editor = BlogEditor()
        self.social = SocialMediaWriter()
        self.outline_validator = OutlineValidationChecker()
        self.post_validator = BlogPostValidationChecker()

    def generate_blog(self, topic, metadata=None):
        # 1. Analyze codebase
        context = analyze_codebase(self.codebase_path)

        # 2. Planner creates outline
        outline = self.planner.create_outline(topic, context, metadata or {})
        if not self.outline_validator.validate(outline):
            raise ValueError('Outline validation failed')

        # 3. Writer drafts content
        draft = self.writer.write_from_outline(outline, context, metadata or {})
        if not self.post_validator.validate(draft):
            raise ValueError('Draft validation failed')

        # 4. Editor polishes
        edited = self.editor.edit(draft)

        # 5. Social media snippets
        social_snips = self.social.create_snippets(edited)

        # 6. Save blog as markdown
        md_path = save_blog_post_to_file(topic, outline, edited, output_dir='docs')
        return {
            'title': topic,
            'outline': outline,
            'draft': draft,
            'edited': edited,
            'social': social_snips,
            'md_path': md_path
        }
