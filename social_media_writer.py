
class SocialMediaWriter:
    def __init__(self):
        pass

    def create_snippets(self, edited_md):
        # Extract title and first paragraph for a LinkedIn/Twitter snippet
        lines = edited_md.splitlines()
        title = lines[0] if lines else 'Pharmacy PA Predictor'
        snippet = ' '.join([ln for ln in lines[1:5] if ln])
        twitter = (title + ' - ' + snippet)[:280]
        linkedin = title + '\n\n' + (snippet[:600])
        return {'twitter': twitter, 'linkedin': linkedin}
