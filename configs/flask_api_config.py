from .flask_config import api
from controller.candidato_soportetecnico_notificacion_controller import *

api.add_resource(CandidatoSoporteTecnicoNotificacionController,
    '/v1/candidato_soportetecnico_notificar')
