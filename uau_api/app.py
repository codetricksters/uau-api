import pandas as pd
import numpy as np
from uau_api.models import Process, User
from uau_api.schemas import ProcessSchema, UserSchema
from uau_api.database import get_session
from uau_api.settings import Settings
from uau_api import UauAPI
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from sqlalchemy import text, select

import locale
import logging


uau = UauAPI(Settings().API_URL, Settings().API_KEY)

uau.authenticate(Settings().API_URL, Settings().API_KEY)
