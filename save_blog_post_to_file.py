
import os
def save_blog_post_to_file(title, outline, md_content, output_dir='docs'):
    os.makedirs(output_dir, exist_ok=True)
    safe_title = title.replace(' ', '_').lower()
    path = os.path.join(output_dir, f"{safe_title}.md")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    return path
