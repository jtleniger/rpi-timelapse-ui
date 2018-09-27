class Settings(object):
    def __init__(self, form):
        self.count = form['exposure-count']
        self.duration = form['exposure-duration']
        self.spacing = form['exposure-spacing']