#!/usr/bin/env python3
"""
Development server runner for the portfolio website.
Use this for local development.
"""

from app import app

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=9000)