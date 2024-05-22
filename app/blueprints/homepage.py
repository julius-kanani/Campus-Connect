#!/usr/bin/env python3
"""The homepage blueprint."""

import functools

from flask import (
    Blueprint, render_template, request, url_for
)

bp = Blueprint('home', __name__,)


@bp.route('/', methods=('GET', 'POST'))
def index():
    """index endpoint."""
    return render_template('homepage/index.html')


@bp.route('/about', methods=('GET', 'POST'))
def about():
    """about endpoint."""
    return render_template('homepage/about.html')
