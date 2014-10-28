import logging
from ringo.model.modul import ActionItem, ACTIONS
from ringo.lib.extension import register_modul
from ringo.lib.helpers import dynamic_import

import ringo_evaluation.views
from ringo_evaluation.model import Extension

log = logging.getLogger(__name__)

modul_config = {
    "name": "evaluation",
    "label": "",
    "clazzpath": "ringo_evaluation.model.Extension",
    "label_plural": "",
    "str_repr": "",
    "display": "",
    "actions": ["list", "read", "update", "create", "delete"]
}


def includeme(config):
    """Registers a new modul for ringo.

    :config: Dictionary with configuration of the new modul

    """
    modul = register_modul(config, modul_config)
    Extension._modul_id = modul.get_value("id")
