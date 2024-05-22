#!/usr/bin/env python3
"""Authentication Blueprint"""

import functools

from flask import (
    Blueprint, render_template, request, url_for
)

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    """Register endpoint."""
    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    """Login endpoint."""
    return render_template('auth/login.html')
