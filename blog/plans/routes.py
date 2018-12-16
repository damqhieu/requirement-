from flask import Blueprint, url_for, render_template, flash,redirect, request
from blog.plans.forms import AddPlanForm, EditPlanForm
from blog.models import Plan
from flask_login import login_required
from blog import db

plans = Blueprint('plans',__name__)


@plans.route("/plan")
@login_required
def index():
    plans = Plan.query.all()
    return render_template('plan/index.html', plans=plans)


@plans.route("/plan/create", methods=['GET', 'POST'])
def create():
    form = AddPlanForm()
    if form.validate_on_submit():
        plan = Plan(
            title=form.title.data, 
            date_start=form.date_start.data,
            date_end=form.date_end.data,
            content=form.content.data,
        )
        db.session.add(plan)
        db.session.commit()
        flash('Your plan has been created!', 'success')
        return redirect(url_for('plans.index'))
    return render_template('plan/create.html', form = form)



@plans.route("/plan/<int:plan_id>/edit", methods=['GET', 'POST'])
@login_required
def update(plan_id):
    plan = Plan.query.get_or_404(plan_id)
    form = EditPlanForm()
    if form.validate_on_submit():
        plan.title = form.title.data
        plan.date_start = form.date_start.data
        plan.date_end = form.date_end.data
        plan.content = form.content.data
        db.session.commit()
        flash('Your plan has been updated!', 'success')
        return redirect(url_for('plans.update', plan_id=plan.id))
    elif request.method == 'GET':
        form.id.data = plan.id
        form.title.data = plan.title
        form.date_start.data = plan.date_start
        form.date_end.data = plan.date_end
        form.content.data = plan.content
    return render_template('plan/edit.html', title='Update Plan',
                           form=form)

@plans.route("/plan/<int:plan_id>/delete", methods=['POST'])
@login_required
def delete_plan(plan_id):
    plan = Plan.query.get_or_404(plan_id)
    db.session.delete(plan)
    db.session.commit()
    flash('Your plan has been deleted!', 'success')
    return redirect(url_for('plans.index'))