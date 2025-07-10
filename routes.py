import string
import random
from flask import Blueprint, request, redirect, jsonify
from database import get_connection

bp = Blueprint('routes', __name__)

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@bp.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url:
        return jsonify({'error': 'URL is required'}), 400

    short_code = generate_code()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO urls (original_url, short_code) VALUES (?, ?)', (original_url, short_code))
    conn.commit()
    conn.close()

    return jsonify({'short_url': f'http://localhost:5000/{short_code}'}), 201

@bp.route('/<short_code>')
def redirect_to_original(short_code):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, original_url FROM urls WHERE short_code = ?', (short_code,))
    row = cur.fetchone()

    if not row:
        return jsonify({'error': 'URL not found'}), 404

    cur.execute('INSERT INTO clicks (url_id, ip_address) VALUES (?, ?)', (row['id'], request.remote_addr))
    conn.commit()
    conn.close()

    return redirect(row['original_url'])

@bp.route('/stats/<short_code>')
def get_stats(short_code):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT id FROM urls WHERE short_code = ?', (short_code,))
    url = cur.fetchone()

    if not url:
        return jsonify({'error': 'URL not found'}), 404

    cur.execute('SELECT COUNT(*) as clicks FROM clicks WHERE url_id = ?', (url['id'],))
    count = cur.fetchone()['clicks']
    conn.close()

    return jsonify({'short_code': short_code, 'clicks': count})