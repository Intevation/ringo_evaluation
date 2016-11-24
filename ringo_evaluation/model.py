import sqlalchemy as sa
from ringo.model import Base
from ringo.model.base import BaseItem, BaseFactory
from ringo.model.mixins import Mixin, Owned, Meta
from ringo.model.modul import ActionItem

class Evaluable(Mixin):
    @classmethod
    def get_mixin_actions(cls):
        actions = []
        # Add Evaluation action
        action = ActionItem()
        action.name = 'Evaluate'
        action.url = 'evaluate/{id}'
        action.icon = 'glyphicon glyphicon-stats'
        action.bundle = True
        actions.append(action)
        return actions

class ExtensionFactory(BaseFactory):

    def create(self, user=None, values=None):
        new_item = BaseFactory.create(self, user, values)
        return new_item


class Extension(Owned, Meta, BaseItem, Base):
    """Docstring for evaluation extension"""

    __tablename__ = 'evaluations'
    """Name of the table in the database for this modul. Do not
    change!"""
    _modul_id = None
    """Will be set dynamically. See include me of this modul"""

    # Define columns of the table in the database
    id = sa.Column(sa.Integer, primary_key=True)
    modul_id = sa.Column('modul_id', sa.Integer, sa.ForeignKey("modules.id"))
    name = sa.Column('name', sa.Text)
    data = sa.Column('data', sa.LargeBinary)
    description = sa.Column('description', sa.Text)
    configuration = sa.Column('configuration', sa.Text)
    size = sa.Column('size', sa.Integer)
    mime = sa.Column('mime', sa.Text)

    # Define relations to other tables
    modul = sa.orm.relationship("ModulItem", backref="evaluations")

    @classmethod
    def get_item_factory(cls):
        return ExtensionFactory(cls)
