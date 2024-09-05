from flask import render_template, redirect, url_for
from app import app, db
from app.forms import SiteForm
from app.models import Site
from flask_login import login_required, current_user

@app.route('/')
@login_required
def index():
    sites = Site.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', sites=sites)

@app.route('/add_site', methods=['GET', 'POST'])
@login_required
def add_site():
    form = SiteForm()
    if form.validate_on_submit():
        site_url = form.url.data
        if not site_url.startswith('http://'):
            site_url = 'http://' + site_url
        site = Site(url=site_url, user_id=current_user.id)
        db.session.add(site)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_site.html', form=form)

@app.route('/edit_site/<int:site_id>', methods=['GET', 'POST'])
@login_required
def edit_site(site_id):
    site = Site.query.get_or_404(site_id)
    if site.user_id != current_user.id:
        abort(403)
    form = SiteForm()
    if form.validate_on_submit():
        site.url = form.url.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.url.data = site.url
    return render_template('edit_site.html', form=form)

@app.route('/delete_site/<int:site_id>')
@login_required
def delete_site(site_id):
    site = Site.query.get_or_404(site_id)
    if site.user_id != current_user.id:
        abort(403)
    db.session.delete(site)
    db.session.commit()
    return redirect(url_for('index'))
