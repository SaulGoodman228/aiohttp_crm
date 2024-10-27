
import typing

from apps.store.crm.accessor import CrmAccessor

if typing.TYPE_CHECKING:
    from apps.web.app import Application

def setup_accessor(app):
    app.crm_accessor = CrmAccessor()

    #Сигналы - спецальные события обозначающие жизненные циклы приложения
    app.on_startup.append(app.crm_accessor.connect)
    app.on_cleanup.append(app.crm_accessor.disconnect)