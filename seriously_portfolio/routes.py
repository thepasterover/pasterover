from flask import render_template, url_for, flash, redirect
from seriously_portfolio import app, db
from seriously_portfolio.models import Client
from seriously_portfolio.form import ContactForm

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        client = Client(name=form.name.data, email=form.email.data, message=form.message.data)
        db.session.add(client)
        db.session.commit()
        flash(f'Form Successfully submitted!', 'success')
        return redirect(url_for('work'))
    return render_template("index.html", form=form)


@app.route("/work")
def work():
    return render_template('work.html')