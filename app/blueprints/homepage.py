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

@bp.route('/contact', methods=('GET', 'POST'))
def contact():
    """Contact endpoint."""
    return render_template('homepage/contact.html')

@bp.route('/terms_of_service', methods=('GET', 'POST'))
def terms_of_service():
    """Terms Of Service endpoint."""
    return render_template('homepage/terms_of_service.html')

@bp.route('/privacy_policy', methods=('GET', 'POST'))
def privacy_policy():
    """Privacy Policy endpoint."""
    return render_template('homepage/privacy_policy.html')
