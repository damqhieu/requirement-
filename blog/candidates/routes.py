from flask import Blueprint, url_for, render_template, flash,redirect, request
from blog.candidates.forms import AddCandidateForm, EditCandidateForm
from blog.models import Plan, Candidate
from flask_login import login_required
from blog import db

candidates = Blueprint('candidates',__name__)


@candidates.route("/candidate")
@login_required
def index():
    candidates = Candidate.query.all()
    return render_template('candidate/index.html', candidates=candidates)


@candidates.route("/candidate/create", methods=['GET', 'POST'])
def create():
    form = AddCandidateForm()
    form.plan_id.choices = [(row.id, row.title) for row in Plan.query.all()]
    if form.validate_on_submit():
        candidate = Candidate(
            name=form.name.data, 
            email=form.email.data,
            address=form.address.data,
            phone=form.phone.data,
            position=form.position.data,
            plan_id=form.plan_id.data,
        )
        db.session.add(candidate)
        db.session.commit()
        flash('Your candidate has been created!', 'success')
        return redirect(url_for('candidates.index'))
    return render_template('candidate/create.html', form = form)



@candidates.route("/candidate/<int:candidate_id>/edit", methods=['GET', 'POST'])
@login_required
def update(candidate_id):
    candidate = Candidate.query.get_or_404(candidate_id)
    form = EditCandidateForm()
    form.plan_id.choices = [(row.id, row.title) for row in Plan.query.all()]
    if form.validate_on_submit():
        candidate.name = form.name.data
        candidate.email = form.email.data
        candidate.address = form.address.data
        candidate.phone = form.phone.data
        candidate.position = form.position.data
        candidate.plan_id = form.plan_id.data
        db.session.commit()
        flash('Your candidate has been updated!', 'success')
        return redirect(url_for('candidates.update', candidate_id=candidate.id))
    elif request.method == 'GET':
        form.id.data = candidate.id
        form.name.data = candidate.name
        form.email.data = candidate.email
        form.phone.data = candidate.phone
        form.address.data = candidate.address
        form.position.data = candidate.position
        form.plan_id.data = candidate.plan_id
    return render_template('candidate/edit.html', title='Update Post',
                           form=form)

@candidates.route("/candidate/<int:candidate_id>/delete", methods=['POST'])
@login_required
def delete_candidate(candidate_id):
    candidate = Candidate.query.get_or_404(candidate_id)
    db.session.delete(candidate)
    db.session.commit()
    flash('Your candidate has been deleted!', 'success')
    return redirect(url_for('candidates.index'))