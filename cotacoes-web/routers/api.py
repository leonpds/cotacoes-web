'''
    Routes for the /api subpath
'''

from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from ..db import db, crud
from .. import models

router = APIRouter(prefix='/api')
