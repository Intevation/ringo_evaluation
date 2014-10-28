import os
import pkg_resources
from mako.lookup import TemplateLookup

from formbar.config import Config, load
from formbar.form import Form

from ringo.lib.renderer.dialogs import DialogRenderer
from ringo.lib.helpers import get_item_modul
from ringo.lib.form import get_path_to_form_config

base_dir = pkg_resources.get_distribution("ringo_evaluation").location
template_dir = os.path.join(base_dir, 'ringo_evaluation', 'templates')
template_lookup = TemplateLookup(directories=[template_dir])


class EvaluationDialogRenderer(DialogRenderer):
    """Docstring for ExportDialogRenderer"""

    def __init__(self, request, clazz):
        """@todo: to be defined """
        DialogRenderer.__init__(self, request, clazz, "evaluate")
        self.template = template_lookup.get_template("internal/evaluation.mako")
        config = Config(load(get_path_to_form_config('evaluations.xml', 'ringo_evaluation', location=".")))
        form_config = config.get_form('dialog')
        self.form = Form(form_config,
                         csrf_token=self._request.session.get_csrf_token())

    def render(self, items):
        values = {}
        values['request'] = self._request
        values['items'] = items
        values['body'] = self._render_body()
        values['modul'] = get_item_modul(self._request, self._item).get_label(plural=True)
        values['action'] = self._action.capitalize()
        values['ok_url'] = self._request.current_route_path()
        values['_'] = self._request.translate
        values['cancel_url'] = self._request.referrer
        return self.template.render(**values)

    def _render_body(self):
        out = []
        # Collect all available evaluations and provide the evaluations
        # for this modul to the form while rendering.
        evaluations = []
        modul = get_item_modul(self._request, self._item)
        for evaluation in modul.evaluations:
            if modul.id == evaluation.modul_id:
                evaluations.append((evaluation, evaluation.id))
        values = {"evaluations": evaluations}
        out.append(self.form.render(buttons=False, values=values))
        return "".join(out)
