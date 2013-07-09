import subprocess
import tempfile
import os

import sublime
import sublime_plugin


class HgAnnotateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_path = self.view.file_name()

        if not file_path:
            return

        proc = subprocess.Popen(
            ['hg', 'annotate', '-vudcl', file_path],
            stdout=subprocess.PIPE
        )
        result = proc.stdout.read()

        if not result:
            return

        file_name = os.path.basename(file_path)
        annotate_file_path = os.path.join(tempfile.gettempdir(), file_name)

        print(annotate_file_path)

        with open(annotate_file_path, 'wb') as f:
            f.write(result)

        self.view.window().open_file(annotate_file_path)
